# Usage Examples for Betty Templates

This guide shows how to use the JSON templates to extract and install Claude Code artifacts in your Betty repository.

## Quick Reference

All JSON files contain **complete markdown content** in the `content` field, making it easy to recreate the files directly.

## Example 1: Extract a Single Agent

```bash
# Extract python-pro agent and save to file
jq -r '.agents[] | select(.name=="python-pro") | .content' agents.json > betty/.claude/agents/python-pro.md
```

**Python script:**
```python
import json
from pathlib import Path

# Load agents
with open('agents.json') as f:
    data = json.load(f)

# Find and save python-pro
for agent in data['agents']:
    if agent['name'] == 'python-pro':
        output_path = Path('betty/.claude/agents/python-pro.md')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(agent['content'])
        print(f"Created {output_path}")
```

## Example 2: Extract All Agents from a Plugin

```bash
# Extract all python-development agents
jq -r '.agents[] | select(.plugin=="python-development") | "\(.name).md:\n\(.content)\n---END---\n"' agents.json
```

**Python script:**
```python
import json
from pathlib import Path

with open('agents.json') as f:
    data = json.load(f)

output_dir = Path('betty/.claude/agents')
output_dir.mkdir(parents=True, exist_ok=True)

# Extract all python-development agents
for agent in data['agents']:
    if agent['plugin'] == 'python-development':
        filename = f"{agent['name']}.md"
        output_path = output_dir / filename
        output_path.write_text(agent['content'])
        print(f"Created {output_path}")
```

## Example 3: Extract Commands by Category

```python
import json
from pathlib import Path

with open('commands.json') as f:
    data = json.load(f)

output_dir = Path('betty/.claude/commands')
output_dir.mkdir(parents=True, exist_ok=True)

# Extract all development category commands
for command in data['commands']:
    if command['category'] == 'development':
        filename = f"{command['name']}.md"
        output_path = output_dir / filename
        output_path.write_text(command['content'])
        print(f"Created {output_path}")
```

## Example 4: Extract a Skill with References and Assets

```python
import json
from pathlib import Path

with open('skills.json') as f:
    data = json.load(f)

# Find async-python-patterns skill
for skill in data['skills']:
    if skill['name'] == 'async-python-patterns':
        # Create skill directory
        skill_dir = Path(f"betty/.claude/skills/{skill['name']}")
        skill_dir.mkdir(parents=True, exist_ok=True)

        # Write main SKILL.md
        (skill_dir / 'SKILL.md').write_text(skill['content'])
        print(f"Created {skill_dir}/SKILL.md")

        # Write references
        if skill.get('references'):
            ref_dir = skill_dir / 'references'
            ref_dir.mkdir(exist_ok=True)
            for filename, content in skill['references'].items():
                (ref_dir / filename).write_text(content)
                print(f"Created {ref_dir}/{filename}")

        # Write assets
        if skill.get('assets'):
            assets_dir = skill_dir / 'assets'
            assets_dir.mkdir(exist_ok=True)
            for filename, content in skill['assets'].items():
                (assets_dir / filename).write_text(content)
                print(f"Created {assets_dir}/{filename}")
```

## Example 5: Batch Import from Recommended List

```python
import json
from pathlib import Path

# Load recommended essentials
with open('recommended-essentials.json') as f:
    recommended = json.load(f)

# Load full catalogs
with open('agents.json') as f:
    agents_data = json.load(f)
with open('commands.json') as f:
    commands_data = json.load(f)
with open('skills.json') as f:
    skills_data = json.load(f)

# Create output directories
Path('betty/.claude/agents').mkdir(parents=True, exist_ok=True)
Path('betty/.claude/commands').mkdir(parents=True, exist_ok=True)
Path('betty/.claude/skills').mkdir(parents=True, exist_ok=True)

# Import recommended agents
for rec_agent in recommended['agents']:
    agent_name = rec_agent['name']
    for agent in agents_data['agents']:
        if agent['name'] == agent_name:
            output_path = Path(f"betty/.claude/agents/{agent_name}.md")
            output_path.write_text(agent['content'])
            print(f"✓ Agent: {agent_name}")

# Import recommended commands
for rec_cmd in recommended['commands']:
    cmd_name = rec_cmd['name']
    for cmd in commands_data['commands']:
        if cmd['name'] == cmd_name:
            output_path = Path(f"betty/.claude/commands/{cmd_name}.md")
            output_path.write_text(cmd['content'])
            print(f"✓ Command: {cmd_name}")

# Import recommended skills
for rec_skill in recommended['skills']:
    skill_name = rec_skill['name']
    for skill in skills_data['skills']:
        if skill['name'] == skill_name:
            skill_dir = Path(f"betty/.claude/skills/{skill_name}")
            skill_dir.mkdir(parents=True, exist_ok=True)

            # Main skill file
            (skill_dir / 'SKILL.md').write_text(skill['content'])

            # References and assets
            if skill.get('references'):
                ref_dir = skill_dir / 'references'
                ref_dir.mkdir(exist_ok=True)
                for filename, content in skill['references'].items():
                    (ref_dir / filename).write_text(content)

            if skill.get('assets'):
                assets_dir = skill_dir / 'assets'
                assets_dir.mkdir(exist_ok=True)
                for filename, content in skill['assets'].items():
                    (assets_dir / filename).write_text(content)

            print(f"✓ Skill: {skill_name}")

print("\n✅ Import complete!")
```

## Example 6: Search and Extract by Keyword

```python
import json
from pathlib import Path

with open('agents.json') as f:
    data = json.load(f)

keyword = "python"
output_dir = Path('betty/.claude/agents')
output_dir.mkdir(parents=True, exist_ok=True)

# Find all agents with "python" keyword
for agent in data['agents']:
    if keyword in agent.get('keywords', []):
        filename = f"{agent['name']}.md"
        output_path = output_dir / filename
        output_path.write_text(agent['content'])
        print(f"✓ {agent['name']} ({agent['plugin']})")
```

## Example 7: Complete Importer Script

Here's a complete script that lets you choose what to import:

```python
#!/usr/bin/env python3
"""
Import Claude Code artifacts into Betty repository.
Usage: python import_to_betty.py [recommended-file.json]
"""

import json
import sys
from pathlib import Path

def load_catalog(catalog_name):
    """Load a catalog JSON file."""
    with open(f'betty-templates/{catalog_name}.json') as f:
        return json.load(f)

def import_agent(agent, output_base):
    """Import a single agent."""
    output_path = output_base / 'agents' / f"{agent['name']}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(agent['content'])
    return output_path

def import_command(command, output_base):
    """Import a single command."""
    output_path = output_base / 'commands' / f"{command['name']}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(command['content'])
    return output_path

def import_skill(skill, output_base):
    """Import a skill with references and assets."""
    skill_dir = output_base / 'skills' / skill['name']
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Main SKILL.md
    (skill_dir / 'SKILL.md').write_text(skill['content'])

    # References
    if skill.get('references'):
        ref_dir = skill_dir / 'references'
        ref_dir.mkdir(exist_ok=True)
        for filename, content in skill['references'].items():
            (ref_dir / filename).write_text(content)

    # Assets
    if skill.get('assets'):
        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        for filename, content in skill['assets'].items():
            (assets_dir / filename).write_text(content)

    return skill_dir

def main():
    # Betty .claude directory
    betty_claude = Path('betty/.claude')

    if len(sys.argv) > 1:
        # Import from recommended file
        rec_file = sys.argv[1]
        with open(rec_file) as f:
            recommended = json.load(f)

        # Load full catalogs
        agents_data = load_catalog('agents')
        commands_data = load_catalog('commands')
        skills_data = load_catalog('skills')

        # Import agents
        for rec_agent in recommended.get('agents', []):
            for agent in agents_data['agents']:
                if agent['name'] == rec_agent['name']:
                    path = import_agent(agent, betty_claude)
                    print(f"✓ Agent: {path}")

        # Import commands
        for rec_cmd in recommended.get('commands', []):
            for cmd in commands_data['commands']:
                if cmd['name'] == rec_cmd['name']:
                    path = import_command(cmd, betty_claude)
                    print(f"✓ Command: {path}")

        # Import skills
        for rec_skill in recommended.get('skills', []):
            for skill in skills_data['skills']:
                if skill['name'] == rec_skill['name']:
                    path = import_skill(skill, betty_claude)
                    print(f"✓ Skill: {path}")

        print(f"\n✅ Imported artifacts from {rec_file}")
    else:
        print("Usage: python import_to_betty.py [recommended-file.json]")
        print("\nAvailable recommended files:")
        print("  - recommended-essentials.json")
        print("  - recommended-python.json")
        print("  - recommended-devops.json")
        print("  - recommended-ai-ml.json")

if __name__ == '__main__':
    main()
```

**Usage:**
```bash
# Import essential development tools
python import_to_betty.py betty-templates/recommended-essentials.json

# Import Python development stack
python import_to_betty.py betty-templates/recommended-python.json

# Import DevOps tools
python import_to_betty.py betty-templates/recommended-devops.json
```

## Using jq for Quick Queries

```bash
# List all agent names
jq -r '.agents[].name' agents.json

# List agents by category
jq -r '.agents[] | select(.category=="languages") | .name' agents.json

# Count artifacts by plugin
jq -r '.agents | group_by(.plugin) | map({plugin: .[0].plugin, count: length})' agents.json

# Find all async-related skills
jq -r '.skills[] | select(.keywords[] | contains("async")) | .name' skills.json

# Get full content of a specific agent
jq -r '.agents[] | select(.name=="python-pro") | .content' agents.json

# Extract all commands with "test" in the name
jq -r '.commands[] | select(.name | contains("test")) | {name, title, plugin}' commands.json
```

## Notes

- All `content` fields contain complete markdown ready to write to files
- Skills may have additional `references` and `assets` objects with supporting files
- The `source_path` field shows the original location in this repository
- Use `jq` for quick JSON queries and filtering
- The Python examples create necessary directories automatically
