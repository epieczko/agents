#!/usr/bin/env python3
"""
Extract Claude Code artifacts from the agents repository.
Creates JSON files for agents, commands, and skills that can be used with meta.agent task.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Parse YAML frontmatter from markdown file."""
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
    return frontmatter

def extract_agents(marketplace_file: Path) -> List[Dict[str, Any]]:
    """Extract all agents with their metadata."""
    with open(marketplace_file) as f:
        marketplace = json.load(f)

    agents_list = []

    for plugin in marketplace['plugins']:
        plugin_name = plugin['name']
        plugin_source = plugin['source']

        for agent_path in plugin.get('agents', []):
            # Construct full path - agent_path is relative to plugin source
            # plugin_source is like "./plugins/python-development"
            # agent_path is like "./agents/python-pro.md"
            full_path = Path(plugin_source) / agent_path
            # Remove leading "./"
            full_path = Path(str(full_path).replace('./', ''))

            if full_path.exists():
                with open(full_path) as f:
                    content = f.read()

                frontmatter = parse_frontmatter(content)

                agents_list.append({
                    'name': frontmatter.get('name', agent_path.replace('.md', '').split('/')[-1]),
                    'description': frontmatter.get('description', ''),
                    'model': frontmatter.get('model', 'sonnet'),
                    'plugin': plugin_name,
                    'source_path': str(full_path),
                    'category': plugin.get('category', 'general'),
                    'keywords': plugin.get('keywords', []),
                    'content': content  # Full markdown content
                })

    return agents_list

def extract_commands(marketplace_file: Path) -> List[Dict[str, Any]]:
    """Extract all commands with their metadata."""
    with open(marketplace_file) as f:
        marketplace = json.load(f)

    commands_list = []

    for plugin in marketplace['plugins']:
        plugin_name = plugin['name']
        plugin_source = plugin['source']

        for command_path in plugin.get('commands', []):
            # Construct full path
            full_path = Path(plugin_source) / command_path
            # Remove leading "./"
            full_path = Path(str(full_path).replace('./', ''))

            if full_path.exists():
                with open(full_path) as f:
                    content = f.read()

                # Extract title from first heading
                title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else command_path.replace('.md', '').split('/')[-1]

                # Extract description from content (first paragraph)
                desc_match = re.search(r'^(?!#)(.+)$', content, re.MULTILINE)
                description = desc_match.group(1).strip() if desc_match else ''

                command_name = command_path.replace('.md', '').replace('commands/', '').replace('./', '')

                commands_list.append({
                    'name': command_name,
                    'title': title,
                    'description': description[:200] if description else '',
                    'plugin': plugin_name,
                    'source_path': str(full_path),
                    'category': plugin.get('category', 'general'),
                    'keywords': plugin.get('keywords', []),
                    'content': content  # Full markdown content
                })

    return commands_list

def extract_skills(marketplace_file: Path) -> List[Dict[str, Any]]:
    """Extract all skills with their metadata."""
    with open(marketplace_file) as f:
        marketplace = json.load(f)

    skills_list = []

    for plugin in marketplace['plugins']:
        plugin_name = plugin['name']
        plugin_source = plugin['source']

        for skill_path in plugin.get('skills', []):
            # Construct full path to SKILL.md
            if not skill_path.endswith('SKILL.md'):
                skill_file = Path(plugin_source) / skill_path / 'SKILL.md'
            else:
                skill_file = Path(plugin_source) / skill_path

            # Remove leading "./"
            skill_file = Path(str(skill_file).replace('./', ''))

            if skill_file.exists():
                with open(skill_file) as f:
                    content = f.read()

                frontmatter = parse_frontmatter(content)

                skill_name = frontmatter.get('name', skill_path.split('/')[-1])

                # Also read any reference/asset files
                skill_dir = skill_file.parent
                reference_files = {}
                asset_files = {}

                # Check for references directory
                ref_dir = skill_dir / 'references'
                if ref_dir.exists():
                    for ref_file in ref_dir.glob('*.md'):
                        with open(ref_file) as f:
                            reference_files[ref_file.name] = f.read()

                # Check for assets directory
                assets_dir = skill_dir / 'assets'
                if assets_dir.exists():
                    for asset_file in assets_dir.glob('*.md'):
                        with open(asset_file) as f:
                            asset_files[asset_file.name] = f.read()

                skills_list.append({
                    'name': skill_name,
                    'description': frontmatter.get('description', ''),
                    'plugin': plugin_name,
                    'source_path': str(skill_file),
                    'category': plugin.get('category', 'general'),
                    'keywords': plugin.get('keywords', []),
                    'content': content,  # Full SKILL.md content
                    'references': reference_files,  # Reference files
                    'assets': asset_files  # Asset files
                })

    return skills_list

def extract_plugins(marketplace_file: Path) -> List[Dict[str, Any]]:
    """Extract plugin metadata."""
    with open(marketplace_file) as f:
        marketplace = json.load(f)

    plugins_list = []

    for plugin in marketplace['plugins']:
        plugins_list.append({
            'name': plugin['name'],
            'description': plugin['description'],
            'version': plugin['version'],
            'category': plugin.get('category', 'general'),
            'keywords': plugin.get('keywords', []),
            'agents_count': len(plugin.get('agents', [])),
            'commands_count': len(plugin.get('commands', [])),
            'skills_count': len(plugin.get('skills', []))
        })

    return plugins_list

def main():
    """Main extraction function."""
    marketplace_file = Path('.claude-plugin/marketplace.json')

    # Extract all artifacts
    agents = extract_agents(marketplace_file)
    commands = extract_commands(marketplace_file)
    skills = extract_skills(marketplace_file)
    plugins = extract_plugins(marketplace_file)

    # Create output directory
    output_dir = Path('betty-templates')
    output_dir.mkdir(exist_ok=True)

    # Save to JSON files
    with open(output_dir / 'agents.json', 'w') as f:
        json.dump({
            'total_count': len(agents),
            'agents': agents
        }, f, indent=2)

    with open(output_dir / 'commands.json', 'w') as f:
        json.dump({
            'total_count': len(commands),
            'commands': commands
        }, f, indent=2)

    with open(output_dir / 'skills.json', 'w') as f:
        json.dump({
            'total_count': len(skills),
            'skills': skills
        }, f, indent=2)

    with open(output_dir / 'plugins.json', 'w') as f:
        json.dump({
            'total_count': len(plugins),
            'plugins': plugins
        }, f, indent=2)

    # Create empty files for hooks and mcps
    with open(output_dir / 'hooks.json', 'w') as f:
        json.dump({
            'total_count': 0,
            'hooks': [],
            'note': 'No hooks found in this repository'
        }, f, indent=2)

    with open(output_dir / 'mcps.json', 'w') as f:
        json.dump({
            'total_count': 0,
            'mcps': [],
            'note': 'No MCP servers found in this repository'
        }, f, indent=2)

    # Create summary
    with open(output_dir / 'summary.json', 'w') as f:
        json.dump({
            'repository': 'wshobson/agents',
            'total_plugins': len(plugins),
            'total_agents': len(agents),
            'total_commands': len(commands),
            'total_skills': len(skills),
            'total_hooks': 0,
            'total_mcps': 0,
            'categories': list(set(p['category'] for p in plugins))
        }, f, indent=2)

    print(f"✓ Extracted {len(agents)} agents")
    print(f"✓ Extracted {len(commands)} commands")
    print(f"✓ Extracted {len(skills)} skills")
    print(f"✓ Extracted {len(plugins)} plugins")
    print(f"\nAll files saved to: {output_dir}/")

if __name__ == '__main__':
    main()
