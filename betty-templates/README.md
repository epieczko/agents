# Claude Code Templates for Betty

This directory contains extracted Claude Code artifacts from the `wshobson/agents` repository, organized in JSON format for easy import into your Betty repository.

## ⚠️ Files Too Large? Use QUICKSTART.md

**The original JSON files are too large to paste into Claude Code prompts.**

👉 **See [QUICKSTART.md](QUICKSTART.md) for the easy import methods!**

**Quick options:**
1. **Use the import script** (easiest): `python3 import_to_betty.py --priority high`
2. **Use split files** in `split/` directory (smaller, organized chunks)
3. **Browse metadata** in `metadata/` directory (no content, just names/descriptions)

## 📊 Overview

**Total Artifacts Extracted:**
- **65 Plugins** - Organized collections of related tools
- **146 Agents** - Specialized AI experts across domains
- **70 Commands** - Workflow and automation tools
- **58 Skills** - Modular knowledge packages with progressive disclosure
- **0 Hooks** - None found in this repository
- **0 MCPs** - None found in this repository

## 📁 Files in This Directory

### Quick Start

- **[QUICKSTART.md](QUICKSTART.md)** - ⭐ Start here! Easy import methods
- **[USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)** - Detailed Python/bash examples
- **import_to_betty.py** - Import script for bulk operations

### Core Artifact Files (⚠️ Too Large for Prompts)

| File | Description | Count | Size |
|------|-------------|-------|------|
| `agents.json` | All AI agents with **full .md content** | 146 | 1.2 MB |
| `commands.json` | All slash commands with **full .md content** | 70 | 1.3 MB |
| `skills.json` | All agent skills with **full content + references + assets** | 58 | 917 KB |
| `plugins.json` | Plugin metadata and organization | 65 | 29 KB |
| `hooks.json` | Git hooks (none in this repo) | 0 | - |
| `mcps.json` | MCP servers (none in this repo) | 0 | - |
| `summary.json` | Repository overview and statistics | - | <1 KB |

**✨ NEW: JSON files now contain the complete markdown content of each artifact, not just metadata!**

### Split Files (Recommended - Smaller & Easier)

Located in `split/` directory:

**By Priority:**
- `agents-priority-high.json` (281 KB) - 17 essential agents
- `commands-priority-high.json` (200 KB) - 11 key commands
- `skills-priority-high.json` (356 KB) - 17 core skills

**By Plugin (Smallest!):**
- `plugin-debugging-toolkit.json` (10 KB) ✓
- `plugin-git-pr-workflows.json` (55 KB) ✓
- `plugin-developer-essentials.json` (120 KB)
- `plugin-python-development.json` (133 KB)
- And more...

**By Category:**
- `agents-category-development.json` (121 KB)
- `agents-category-languages.json` (113 KB)
- `agents-category-ai-ml.json` (68 KB)
- And more...

### Metadata Files (Just Names/Descriptions)

Located in `metadata/` directory:

- `agents-metadata.json` (84 KB) - Browse without loading full content
- `commands-metadata.json` (33 KB) - Browse without loading full content
- `skills-metadata.json` (33 KB) - Browse without loading full content

### Curated Recommendations

| File | Description |
|------|-------------|
| `recommended-essentials.json` | Core agents/commands/skills for general development |
| `recommended-python.json` | Python development stack |
| `recommended-devops.json` | DevOps and infrastructure tools |
| `recommended-ai-ml.json` | AI/ML and LLM application development |

## 📋 Categories

The artifacts are organized into 23 categories:

**Development & Languages:**
- development, languages, api

**Infrastructure & Operations:**
- infrastructure, operations, performance

**Quality & Security:**
- quality, security, testing

**AI & Data:**
- ai-ml, data, database

**Business & Marketing:**
- business, marketing, finance, payments

**Specialized:**
- blockchain, gaming, accessibility, workflows, documentation, modernization, utilities

## 🚀 How to Use These Templates

**👉 See [QUICKSTART.md](QUICKSTART.md) for detailed instructions!**

### Quick Start (3 Steps)

**Option 1: Use the Import Script (Easiest)**
```bash
# Copy templates to Betty
cp -r betty-templates /path/to/betty/

# Run import script
cd /path/to/betty/betty-templates
python3 import_to_betty.py --priority high
```

**Option 2: Use Split JSON Files (Smaller)**
```bash
# These are small enough to work with:
# - betty-templates/split/plugin-*.json
# - betty-templates/split/*-category-*.json
# - betty-templates/metadata/*.json

# Example: View what's in python-development
jq '.agents[].name' split/plugin-python-development.json
```

**Option 3: Manual Extract with jq**
```bash
# Extract a single agent
jq -r '.agents[] | select(.name=="python-pro") | .content' \
  split/plugin-python-development.json > betty/.claude/agents/python-pro.md
```

### Don't Use (Too Large)

❌ **agents.json** (1.2 MB) - Use split files instead
❌ **commands.json** (1.3 MB) - Use split files instead
❌ **skills.json** (917 KB) - Use split files instead

These are kept for completeness but are too large for Claude Code prompts.

## 🎯 Recommended Artifacts for Betty

### Essential Development Tools (8 items)

**Agents:**
- `python-pro` - Python 3.12+ expert with modern tooling
- `debugger` - Interactive debugging and troubleshooting
- `code-reviewer` - AI-powered code quality analysis

**Commands:**
- `smart-debug` - Smart debugging workflow
- `pr-enhance` - Pull request enhancement
- `git-workflow` - Git workflow automation

**Skills:**
- `git-advanced-workflows` - Git best practices
- `debugging-strategies` - Debugging methodologies

### Python Development Stack (12 items)

**From `python-development` plugin:**
- Agents: `python-pro`, `django-pro`, `fastapi-pro`
- Commands: `python-scaffold`
- Skills: `async-python-patterns`, `python-testing-patterns`, `python-packaging`, `python-performance-optimization`, `uv-package-manager`

### DevOps & Infrastructure (15 items)

**From multiple plugins:**
- `kubernetes-architect` - K8s deployment expert
- `cloud-architect` - Multi-cloud infrastructure
- `terraform-specialist` - IaC automation
- Skills: `k8s-manifest-generator`, `helm-chart-scaffolding`, `gitops-workflow`, `terraform-module-library`

### AI/ML Development (10 items)

**From `llm-application-dev` plugin:**
- Agents: `ai-engineer`, `prompt-engineer`
- Commands: `langchain-agent`, `ai-assistant`, `prompt-optimize`
- Skills: `langchain-architecture`, `prompt-engineering-patterns`, `rag-implementation`, `llm-evaluation`

## 📖 Understanding the JSON Structure

### Agents Structure

```json
{
  "total_count": 146,
  "agents": [
    {
      "name": "python-pro",
      "description": "Master Python 3.12+ with modern features...",
      "model": "sonnet",
      "plugin": "python-development",
      "source_path": "plugins/python-development/agents/python-pro.md",
      "category": "languages",
      "keywords": ["python", "django", "fastapi", "async", "backend"],
      "content": "---\nname: python-pro\ndescription: Master Python...\n---\n\n[FULL MARKDOWN CONTENT]"
    }
  ]
}
```

**Key Field:**
- **`content`**: Full markdown file content including YAML frontmatter (ready to write directly to file)

### Commands Structure

```json
{
  "total_count": 70,
  "commands": [
    {
      "name": "python-scaffold",
      "title": "Python Project Scaffolding",
      "description": "Generate production-ready Python projects...",
      "plugin": "python-development",
      "source_path": "plugins/python-development/commands/python-scaffold.md",
      "category": "languages",
      "keywords": ["python", "scaffolding", "project-setup"],
      "content": "# Python Project Scaffolding\n\n[FULL MARKDOWN CONTENT]"
    }
  ]
}
```

**Key Field:**
- **`content`**: Full markdown command file (ready to write directly to file)

### Skills Structure

```json
{
  "total_count": 58,
  "skills": [
    {
      "name": "async-python-patterns",
      "description": "Master Python asyncio, concurrent programming...",
      "plugin": "python-development",
      "source_path": "plugins/python-development/skills/async-python-patterns/SKILL.md",
      "category": "languages",
      "keywords": ["python", "async", "concurrency"],
      "content": "---\nname: async-python-patterns\n...\n[FULL SKILL.md CONTENT]",
      "references": {
        "api-best-practices.md": "[CONTENT]",
        "examples.md": "[CONTENT]"
      },
      "assets": {
        "templates.md": "[CONTENT]"
      }
    }
  ]
}
```

**Key Fields:**
- **`content`**: Full SKILL.md markdown content
- **`references`**: Object with reference filenames as keys and full content as values
- **`assets`**: Object with asset filenames as keys and full content as values

## 🔍 Finding What You Need

### By Category

```bash
# List all agents in a category
jq '.agents[] | select(.category=="languages")' agents.json

# List all development-related plugins
jq '.plugins[] | select(.category=="development")' plugins.json
```

### By Keywords

```bash
# Find Python-related items
jq '.agents[] | select(.keywords[] | contains("python"))' agents.json

# Find testing-related commands
jq '.commands[] | select(.keywords[] | contains("testing"))' commands.json
```

### By Plugin

```bash
# Get all agents from python-development plugin
jq '.agents[] | select(.plugin=="python-development")' agents.json
```

## 🌟 Top Plugins by Artifact Count

1. **cloud-infrastructure** - 6 agents, 0 commands, 4 skills
2. **observability-monitoring** - 4 agents, 2 commands, 4 skills
3. **multi-platform-apps** - 6 agents, 1 command, 0 skills
4. **python-development** - 3 agents, 1 command, 5 skills
5. **developer-essentials** - 0 agents, 0 commands, 8 skills

## 💡 Tips

1. **Start Small** - Begin with `recommended-essentials.json` for core functionality
2. **By Domain** - Install domain-specific plugins as needed
3. **Test First** - Try plugins in a test project before adding to production
4. **Review Content** - Check source files in `plugins/` before importing
5. **Stay Organized** - Use consistent naming and structure in Betty

## 📚 Next Steps

1. Review `recommended-essentials.json` for must-have artifacts
2. Check domain-specific recommendations (Python, DevOps, AI/ML)
3. Browse the full catalogs in `agents.json`, `commands.json`, `skills.json`
4. Copy desired artifacts to your Betty repository
5. Test and iterate based on your workflow

## 🔗 Resources

- **Source Repository**: https://github.com/wshobson/agents
- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code/overview
- **Plugin System**: https://docs.claude.com/en/docs/claude-code/plugins
- **Agent Skills**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

## 📝 Notes

- All paths in JSON files are relative to the repository root
- Source files are markdown with YAML frontmatter
- Skills use progressive disclosure (metadata → instructions → resources)
- No hooks or MCPs were found in this repository
