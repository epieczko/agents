# Claude Code Templates for Betty

This directory contains extracted Claude Code artifacts from the `wshobson/agents` repository, organized in JSON format for easy import into your Betty repository.

## 📊 Overview

**Total Artifacts Extracted:**
- **65 Plugins** - Organized collections of related tools
- **146 Agents** - Specialized AI experts across domains
- **70 Commands** - Workflow and automation tools
- **58 Skills** - Modular knowledge packages with progressive disclosure
- **0 Hooks** - None found in this repository
- **0 MCPs** - None found in this repository

## 📁 Files in This Directory

### Core Artifact Files

| File | Description | Count |
|------|-------------|-------|
| `agents.json` | All AI agents with descriptions and metadata | 146 |
| `commands.json` | All slash commands and workflows | 70 |
| `skills.json` | All agent skills with progressive disclosure | 58 |
| `plugins.json` | Plugin metadata and organization | 65 |
| `hooks.json` | Git hooks (none in this repo) | 0 |
| `mcps.json` | MCP servers (none in this repo) | 0 |
| `summary.json` | Repository overview and statistics | - |

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

### Option 1: Using meta.agent Task

If you have a `meta.agent` task configured in your Betty repository:

```bash
# Import specific agents
meta.agent import --from agents.json --select "python-pro,typescript-pro,backend-architect"

# Import by category
meta.agent import --from agents.json --category "development"

# Import recommended essentials
meta.agent import --from recommended-essentials.json
```

### Option 2: Manual Import

1. **Choose artifacts** from the JSON files
2. **Copy source files** from the `plugins/` directory
3. **Place in Betty's .claude directory:**
   ```
   betty/.claude/
   ├── agents/
   ├── commands/
   └── skills/
   ```

### Option 3: Selective Plugin Installation

Install specific plugins from the marketplace:

```bash
# Add the marketplace (if not already added)
/plugin marketplace add wshobson/agents

# Install specific plugins
/plugin install python-development
/plugin install developer-essentials
/plugin install git-pr-workflows
```

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
      "keywords": ["python", "django", "fastapi", "async", "backend"]
    }
  ]
}
```

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
      "keywords": ["python", "scaffolding", "project-setup"]
    }
  ]
}
```

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
      "keywords": ["python", "async", "concurrency"]
    }
  ]
}
```

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
