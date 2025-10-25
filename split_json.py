#!/usr/bin/env python3
"""
Split large JSON files into smaller, manageable chunks for Claude Code.
Creates priority-based and category-based splits.
"""

import json
from pathlib import Path
from typing import Dict, List, Any

def load_json(filename: str) -> Dict:
    """Load a JSON file."""
    with open(f'betty-templates/{filename}') as f:
        return json.load(f)

def save_json(data: Dict, filepath: Path):
    """Save data to JSON file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Created {filepath} ({filepath.stat().st_size / 1024:.1f} KB)")

def split_by_priority():
    """Split artifacts into high/medium/low priority based on recommendations."""

    # Load recommendation files to determine priority
    essentials = load_json('recommended-essentials.json')
    python = load_json('recommended-python.json')
    devops = load_json('recommended-devops.json')
    ai_ml = load_json('recommended-ai-ml.json')

    # Collect high priority items
    high_priority_agents = set()
    high_priority_commands = set()
    high_priority_skills = set()

    for rec in [essentials, python, devops, ai_ml]:
        for agent in rec.get('agents', []):
            if agent.get('priority') == 'high':
                high_priority_agents.add(agent['name'])
        for cmd in rec.get('commands', []):
            if cmd.get('priority') == 'high':
                high_priority_commands.add(cmd['name'])
        for skill in rec.get('skills', []):
            if skill.get('priority') == 'high':
                high_priority_skills.add(skill['name'])

    # Load full catalogs
    agents_data = load_json('agents.json')
    commands_data = load_json('commands.json')
    skills_data = load_json('skills.json')

    # Split agents
    high_agents = [a for a in agents_data['agents'] if a['name'] in high_priority_agents]
    save_json({
        'total_count': len(high_agents),
        'priority': 'high',
        'description': 'High priority agents recommended for immediate use',
        'agents': high_agents
    }, Path('betty-templates/split/agents-priority-high.json'))

    # Split commands
    high_commands = [c for c in commands_data['commands'] if c['name'] in high_priority_commands]
    save_json({
        'total_count': len(high_commands),
        'priority': 'high',
        'description': 'High priority commands recommended for immediate use',
        'commands': high_commands
    }, Path('betty-templates/split/commands-priority-high.json'))

    # Split skills
    high_skills = [s for s in skills_data['skills'] if s['name'] in high_priority_skills]
    save_json({
        'total_count': len(high_skills),
        'priority': 'high',
        'description': 'High priority skills recommended for immediate use',
        'skills': high_skills
    }, Path('betty-templates/split/skills-priority-high.json'))

def split_by_category():
    """Split artifacts by category."""

    agents_data = load_json('agents.json')
    commands_data = load_json('commands.json')
    skills_data = load_json('skills.json')

    # Get all categories
    categories = set()
    for agent in agents_data['agents']:
        categories.add(agent.get('category', 'general'))

    # Split by category
    for category in ['development', 'languages', 'infrastructure', 'ai-ml', 'security']:
        # Agents
        cat_agents = [a for a in agents_data['agents'] if a.get('category') == category]
        if cat_agents:
            save_json({
                'total_count': len(cat_agents),
                'category': category,
                'agents': cat_agents
            }, Path(f'betty-templates/split/agents-category-{category}.json'))

        # Commands
        cat_commands = [c for c in commands_data['commands'] if c.get('category') == category]
        if cat_commands:
            save_json({
                'total_count': len(cat_commands),
                'category': category,
                'commands': cat_commands
            }, Path(f'betty-templates/split/commands-category-{category}.json'))

        # Skills
        cat_skills = [s for s in skills_data['skills'] if s.get('category') == category]
        if cat_skills:
            save_json({
                'total_count': len(cat_skills),
                'category': category,
                'skills': cat_skills
            }, Path(f'betty-templates/split/skills-category-{category}.json'))

def split_by_plugin():
    """Split artifacts by plugin for focused imports."""

    agents_data = load_json('agents.json')
    commands_data = load_json('commands.json')
    skills_data = load_json('skills.json')

    # Top plugins to split
    top_plugins = [
        'python-development',
        'developer-essentials',
        'javascript-typescript',
        'kubernetes-operations',
        'cloud-infrastructure',
        'llm-application-dev',
        'git-pr-workflows',
        'debugging-toolkit'
    ]

    for plugin in top_plugins:
        plugin_agents = [a for a in agents_data['agents'] if a.get('plugin') == plugin]
        plugin_commands = [c for c in commands_data['commands'] if c.get('plugin') == plugin]
        plugin_skills = [s for s in skills_data['skills'] if s.get('plugin') == plugin]

        if plugin_agents or plugin_commands or plugin_skills:
            save_json({
                'plugin': plugin,
                'agents': plugin_agents,
                'commands': plugin_commands,
                'skills': plugin_skills,
                'counts': {
                    'agents': len(plugin_agents),
                    'commands': len(plugin_commands),
                    'skills': len(plugin_skills)
                }
            }, Path(f'betty-templates/split/plugin-{plugin}.json'))

def create_metadata_only():
    """Create lightweight metadata-only versions."""

    agents_data = load_json('agents.json')
    commands_data = load_json('commands.json')
    skills_data = load_json('skills.json')

    # Agents metadata
    agents_meta = [{
        'name': a['name'],
        'description': a['description'],
        'model': a.get('model'),
        'plugin': a['plugin'],
        'category': a['category'],
        'keywords': a['keywords']
    } for a in agents_data['agents']]

    save_json({
        'total_count': len(agents_meta),
        'note': 'Metadata only - use full files for content',
        'agents': agents_meta
    }, Path('betty-templates/metadata/agents-metadata.json'))

    # Commands metadata
    commands_meta = [{
        'name': c['name'],
        'title': c['title'],
        'description': c['description'],
        'plugin': c['plugin'],
        'category': c['category'],
        'keywords': c['keywords']
    } for c in commands_data['commands']]

    save_json({
        'total_count': len(commands_meta),
        'note': 'Metadata only - use full files for content',
        'commands': commands_meta
    }, Path('betty-templates/metadata/commands-metadata.json'))

    # Skills metadata
    skills_meta = [{
        'name': s['name'],
        'description': s['description'],
        'plugin': s['plugin'],
        'category': s['category'],
        'keywords': s['keywords'],
        'has_references': bool(s.get('references')),
        'has_assets': bool(s.get('assets'))
    } for s in skills_data['skills']]

    save_json({
        'total_count': len(skills_meta),
        'note': 'Metadata only - use full files for content',
        'skills': skills_meta
    }, Path('betty-templates/metadata/skills-metadata.json'))

def main():
    """Run all split operations."""
    print("Splitting large JSON files into manageable chunks...\n")

    print("1. Splitting by priority...")
    split_by_priority()

    print("\n2. Splitting by category...")
    split_by_category()

    print("\n3. Splitting by plugin...")
    split_by_plugin()

    print("\n4. Creating metadata-only versions...")
    create_metadata_only()

    print("\n✅ All splits created successfully!")
    print("\nCreated directories:")
    print("  betty-templates/split/     - Priority, category, and plugin-based splits")
    print("  betty-templates/metadata/  - Lightweight metadata-only files")

if __name__ == '__main__':
    main()
