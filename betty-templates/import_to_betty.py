#!/usr/bin/env python3
"""
Import Claude Code artifacts into Betty repository.

Usage:
    python import_to_betty.py                              # Interactive mode
    python import_to_betty.py --priority high              # Import high priority items
    python import_to_betty.py --plugin python-development  # Import specific plugin
    python import_to_betty.py --category languages         # Import by category
    python import_to_betty.py --list                       # List available options
"""

import json
import sys
from pathlib import Path
from typing import Dict, List

# Adjust these paths as needed
TEMPLATES_DIR = Path(__file__).parent
BETTY_CLAUDE_DIR = Path('../betty/.claude')  # Adjust to your Betty location

def import_agent(agent: Dict, output_base: Path) -> Path:
    """Import a single agent."""
    output_path = output_base / 'agents' / f"{agent['name']}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(agent['content'])
    return output_path

def import_command(command: Dict, output_base: Path) -> Path:
    """Import a single command."""
    output_path = output_base / 'commands' / f"{command['name']}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(command['content'])
    return output_path

def import_skill(skill: Dict, output_base: Path) -> Path:
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

def import_from_file(json_file: Path, output_base: Path):
    """Import artifacts from a JSON file."""
    with open(json_file) as f:
        data = json.load(f)

    counts = {'agents': 0, 'commands': 0, 'skills': 0}

    # Import agents
    for agent in data.get('agents', []):
        path = import_agent(agent, output_base)
        print(f"  ✓ Agent: {agent['name']}")
        counts['agents'] += 1

    # Import commands
    for command in data.get('commands', []):
        path = import_command(command, output_base)
        print(f"  ✓ Command: {command['name']}")
        counts['commands'] += 1

    # Import skills
    for skill in data.get('skills', []):
        path = import_skill(skill, output_base)
        print(f"  ✓ Skill: {skill['name']}")
        counts['skills'] += 1

    return counts

def list_available():
    """List available import options."""
    print("\n📦 Available Imports:\n")

    print("HIGH PRIORITY (recommended start):")
    print("  python import_to_betty.py --priority high")
    print("  → Imports essential development tools\n")

    print("BY PLUGIN:")
    plugins = list((TEMPLATES_DIR / 'split').glob('plugin-*.json'))
    for p in sorted(plugins)[:8]:
        plugin_name = p.stem.replace('plugin-', '')
        print(f"  python import_to_betty.py --plugin {plugin_name}")
    print()

    print("BY CATEGORY:")
    categories = ['development', 'languages', 'infrastructure', 'ai-ml', 'security']
    for cat in categories:
        print(f"  python import_to_betty.py --category {cat}")
    print()

    print("CURATED COLLECTIONS:")
    print("  python import_to_betty.py --recommended essentials")
    print("  python import_to_betty.py --recommended python")
    print("  python import_to_betty.py --recommended devops")
    print("  python import_to_betty.py --recommended ai-ml")

def import_priority(priority: str):
    """Import by priority level."""
    print(f"\n📥 Importing {priority} priority artifacts...\n")

    files = list((TEMPLATES_DIR / 'split').glob(f'*-priority-{priority}.json'))
    total_counts = {'agents': 0, 'commands': 0, 'skills': 0}

    for file in files:
        print(f"Processing {file.name}...")
        counts = import_from_file(file, BETTY_CLAUDE_DIR)
        for key in total_counts:
            total_counts[key] += counts[key]

    print(f"\n✅ Imported: {total_counts['agents']} agents, {total_counts['commands']} commands, {total_counts['skills']} skills")

def import_plugin(plugin_name: str):
    """Import a specific plugin."""
    file = TEMPLATES_DIR / 'split' / f'plugin-{plugin_name}.json'

    if not file.exists():
        print(f"❌ Plugin '{plugin_name}' not found")
        print("Run with --list to see available plugins")
        return

    print(f"\n📥 Importing {plugin_name} plugin...\n")
    counts = import_from_file(file, BETTY_CLAUDE_DIR)
    print(f"\n✅ Imported: {counts['agents']} agents, {counts['commands']} commands, {counts['skills']} skills")

def import_category(category: str):
    """Import by category."""
    print(f"\n📥 Importing {category} category...\n")

    files = list((TEMPLATES_DIR / 'split').glob(f'*-category-{category}.json'))
    total_counts = {'agents': 0, 'commands': 0, 'skills': 0}

    for file in files:
        print(f"Processing {file.name}...")
        counts = import_from_file(file, BETTY_CLAUDE_DIR)
        for key in total_counts:
            total_counts[key] += counts[key]

    print(f"\n✅ Imported: {total_counts['agents']} agents, {total_counts['commands']} commands, {total_counts['skills']} skills")

def import_recommended(collection: str):
    """Import from curated recommendations."""
    file = TEMPLATES_DIR / f'recommended-{collection}.json'

    if not file.exists():
        print(f"❌ Collection '{collection}' not found")
        print("Available: essentials, python, devops, ai-ml")
        return

    print(f"\n📥 Importing recommended {collection} artifacts...\n")

    with open(file) as f:
        recommended = json.load(f)

    # Load full catalogs
    agents_file = TEMPLATES_DIR / 'agents.json'
    commands_file = TEMPLATES_DIR / 'commands.json'
    skills_file = TEMPLATES_DIR / 'skills.json'

    with open(agents_file) as f:
        agents_data = json.load(f)
    with open(commands_file) as f:
        commands_data = json.load(f)
    with open(skills_file) as f:
        skills_data = json.load(f)

    counts = {'agents': 0, 'commands': 0, 'skills': 0}

    # Import agents
    for rec_agent in recommended.get('agents', []):
        for agent in agents_data['agents']:
            if agent['name'] == rec_agent['name']:
                import_agent(agent, BETTY_CLAUDE_DIR)
                print(f"  ✓ Agent: {agent['name']} ({rec_agent.get('priority', 'N/A')} priority)")
                counts['agents'] += 1
                break

    # Import commands
    for rec_cmd in recommended.get('commands', []):
        for cmd in commands_data['commands']:
            if cmd['name'] == rec_cmd['name']:
                import_command(cmd, BETTY_CLAUDE_DIR)
                print(f"  ✓ Command: {cmd['name']} ({rec_cmd.get('priority', 'N/A')} priority)")
                counts['commands'] += 1
                break

    # Import skills
    for rec_skill in recommended.get('skills', []):
        for skill in skills_data['skills']:
            if skill['name'] == rec_skill['name']:
                import_skill(skill, BETTY_CLAUDE_DIR)
                print(f"  ✓ Skill: {skill['name']} ({rec_skill.get('priority', 'N/A')} priority)")
                counts['skills'] += 1
                break

    print(f"\n✅ Imported: {counts['agents']} agents, {counts['commands']} commands, {counts['skills']} skills")

def interactive_mode():
    """Interactive import wizard."""
    print("\n🎯 Claude Code Import Wizard for Betty\n")
    print("What would you like to import?\n")
    print("1. High priority essentials (recommended start)")
    print("2. Specific plugin")
    print("3. By category")
    print("4. Curated collection")
    print("5. List all options")
    print("0. Exit\n")

    choice = input("Enter choice (0-5): ").strip()

    if choice == '1':
        import_priority('high')
    elif choice == '2':
        plugin = input("Plugin name (e.g., python-development): ").strip()
        import_plugin(plugin)
    elif choice == '3':
        category = input("Category (e.g., languages): ").strip()
        import_category(category)
    elif choice == '4':
        collection = input("Collection (essentials/python/devops/ai-ml): ").strip()
        import_recommended(collection)
    elif choice == '5':
        list_available()
    elif choice == '0':
        print("Goodbye!")
        return
    else:
        print("Invalid choice")

def main():
    """Main entry point."""
    if len(sys.argv) == 1:
        interactive_mode()
        return

    arg = sys.argv[1]

    if arg == '--list':
        list_available()
    elif arg == '--priority' and len(sys.argv) > 2:
        import_priority(sys.argv[2])
    elif arg == '--plugin' and len(sys.argv) > 2:
        import_plugin(sys.argv[2])
    elif arg == '--category' and len(sys.argv) > 2:
        import_category(sys.argv[2])
    elif arg == '--recommended' and len(sys.argv) > 2:
        import_recommended(sys.argv[2])
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
