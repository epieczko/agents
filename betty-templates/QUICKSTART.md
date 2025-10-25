# Quick Start Guide - Importing to Betty

The original JSON files are too large for Claude Code prompts. Use these smaller files and import methods instead!

## 🚀 Recommended Approach: Use the Import Script

**Step 1:** Copy the templates to your Betty repo:
```bash
# Copy the entire betty-templates directory to your Betty repo
cp -r betty-templates /path/to/betty/
```

**Step 2:** Run the import script:
```bash
cd /path/to/betty/betty-templates
python3 import_to_betty.py
```

**Step 3:** Follow the interactive wizard or use command-line options:

### Quick Start - Import High Priority Items

```bash
# Import the essentials (best starting point)
python3 import_to_betty.py --priority high
```

This imports:
- **17 agents** - Core development experts (debugger, code-reviewer, python-pro, etc.)
- **11 commands** - Essential workflows (smart-debug, pr-enhance, git-workflow, etc.)
- **17 skills** - Fundamental knowledge (async-python, git-workflows, debugging, etc.)

### Import by Plugin

```bash
# Python development
python3 import_to_betty.py --plugin python-development

# Developer essentials (8 essential skills)
python3 import_to_betty.py --plugin developer-essentials

# Git workflows
python3 import_to_betty.py --plugin git-pr-workflows

# Kubernetes operations
python3 import_to_betty.py --plugin kubernetes-operations

# LLM development
python3 import_to_betty.py --plugin llm-application-dev
```

### Import by Category

```bash
# All language-focused tools
python3 import_to_betty.py --category languages

# All development tools
python3 import_to_betty.py --category development

# Infrastructure & DevOps
python3 import_to_betty.py --category infrastructure

# AI/ML tools
python3 import_to_betty.py --category ai-ml
```

### Import Curated Collections

```bash
# Essential development tools
python3 import_to_betty.py --recommended essentials

# Complete Python stack
python3 import_to_betty.py --recommended python

# DevOps & infrastructure
python3 import_to_betty.py --recommended devops

# AI/ML development
python3 import_to_betty.py --recommended ai-ml
```

## 📁 Alternative: Use Split JSON Files

If you prefer to paste JSON into Claude Code, use the smaller split files:

### High Priority Items (Small Enough for Prompts)

Located in `betty-templates/split/`:

- **agents-priority-high.json** (281 KB) - 17 essential agents
- **commands-priority-high.json** (200 KB) - 11 key commands
- **skills-priority-high.json** (356 KB) - 17 core skills

These are still large but manageable. For even smaller files, use category or plugin splits:

### By Plugin (Smallest Files)

- **plugin-debugging-toolkit.json** (10 KB) ✓ Small!
- **plugin-git-pr-workflows.json** (55 KB) ✓ Small!
- **plugin-python-development.json** (133 KB)
- **plugin-developer-essentials.json** (120 KB)
- **plugin-javascript-typescript.json** (107 KB)
- **plugin-kubernetes-operations.json** (106 KB)
- **plugin-llm-application-dev.json** (184 KB)

### By Category

- **agents-category-development.json** (121 KB)
- **agents-category-languages.json** (113 KB)
- **agents-category-ai-ml.json** (68 KB) ✓ Smaller!
- **skills-category-development.json** (191 KB)
- **skills-category-languages.json** (234 KB)

## 🔍 Browse Metadata First

To see what's available without loading full content:

Located in `betty-templates/metadata/`:

- **agents-metadata.json** (84 KB) - Just names, descriptions, no content
- **commands-metadata.json** (33 KB) - Just names, descriptions, no content
- **skills-metadata.json** (33 KB) - Just names, descriptions, no content

Use these to browse and decide what to import!

## 📝 Manual Import from JSON

If you want to manually extract specific items:

```bash
# Extract a single agent
cd betty-templates
jq -r '.agents[] | select(.name=="python-pro") | .content' split/plugin-python-development.json > ../betty/.claude/agents/python-pro.md

# Extract all agents from a plugin file
jq -r '.agents[] | .name' split/plugin-python-development.json | while read name; do
  jq -r ".agents[] | select(.name==\"$name\") | .content" split/plugin-python-development.json > ../betty/.claude/agents/$name.md
done
```

## 🎯 Recommended Starting Point

**For most users:**
```bash
# Start with high priority essentials
python3 import_to_betty.py --priority high

# Then add your language of choice
python3 import_to_betty.py --plugin python-development
# OR
python3 import_to_betty.py --plugin javascript-typescript
```

**For Python developers:**
```bash
python3 import_to_betty.py --recommended python
```

**For DevOps/SREs:**
```bash
python3 import_to_betty.py --recommended devops
```

**For AI/ML engineers:**
```bash
python3 import_to_betty.py --recommended ai-ml
```

## 📊 File Size Reference

| Type | File | Size | Can Paste? |
|------|------|------|------------|
| Original | agents.json | 1.2 MB | ❌ Too large |
| Original | commands.json | 1.3 MB | ❌ Too large |
| Original | skills.json | 917 KB | ❌ Too large |
| Priority High | agents-priority-high.json | 281 KB | ⚠️ Maybe |
| Priority High | skills-priority-high.json | 356 KB | ⚠️ Maybe |
| Plugin | debugging-toolkit | 10 KB | ✅ Yes! |
| Plugin | git-pr-workflows | 55 KB | ✅ Yes! |
| Plugin | python-development | 133 KB | ⚠️ Maybe |
| Metadata | agents-metadata.json | 84 KB | ✅ Yes! |

## 💡 Pro Tips

1. **Start small** - Import high priority items first, test in Betty
2. **Use metadata** - Browse metadata files to see what's available
3. **Use the script** - Easiest way to bulk import
4. **Cherry-pick** - Use plugin-specific files for targeted imports
5. **Check Betty** - Verify imports in Betty before adding more

## 🆘 Troubleshooting

**Q: Import script can't find files?**
A: Adjust `BETTY_CLAUDE_DIR` path in import_to_betty.py line 20

**Q: Still too large for Claude Code?**
A: Use the individual plugin files - they're much smaller

**Q: Want to see what's in a file before importing?**
A: Use the metadata files first, or `jq '.agents[].name' file.json`

**Q: How do I import just one specific agent?**
A: Use jq to extract: `jq -r '.agents[] | select(.name=="NAME") | .content' file.json > agent.md`
