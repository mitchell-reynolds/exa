---
title: "Product Requirements Doc"
description: "PRD of what we are building, tech stack, features"
---

# Project Requirements Document

## Project Overview

**Project Name**: Exa AI for Biotech researchers
**Type**: Claude Code Template/Skeleton
**Purpose**: Provides a structured foundation for AI-assisted development projects

### Problem Statement

Biotech researchers are overwhelmed by the volume of scientific literature, clinical trials, and industry news. Manually searching, reading, and synthesizing this information is:
- **Time-consuming**: Hours spent filtering through irrelevant search results.
- **Fragmented**: Information is spread across various formats (papers, news, social media).
- **Hard to Synthesize**: Difficult to extract key insights and patterns quickly.
- **Resource Intensive**: Requires significant cognitive load to create executive summaries for stakeholders.

### Solution

An AI-powered research applet that leverages the Exa AI SDK to find high-signal information and Claude's reasoning capabilities to synthesize it.
- **Intelligent Search**: Deep neural search via Exa AI to find the most relevant biotech content.
- **Executive Summarization**: Automatically generates comprehensive summaries with clear headings and bullet points.
- **Structured Insights**: Provides a UI-friendly table of ranked results with categories (e.g., papers, news) and generated summaries.
- **Streamlined Workflow**: A simple "query-in, insights-out" interface built with Streamlit.

## Target Audience

### Primary Users
- **Biotech Researchers**: Looking for the latest research and industry trends.
- **R&D Managers**: Needing quick executive summaries of specific biotech domains.
- **Market Intelligence Analysts**: Tracking news and social sentiment in the life sciences sector.

### Use Cases
1. **Literature Review** - Quickly synthesize the current state of research for a specific molecule or therapy.
2. **Competitive Intelligence** - Track news and announcements from competing biotech firms.
3. **Executive Reporting** - Generate structured summaries for stakeholders based on real-time data.
4. **Trend Analysis** - Identify emerging topics in the biotech community across various platforms.

## Functional Requirements

### Core Features

#### 1. Documentation System
- **Memory Bank Structure** - Organized docs/, tasks/, reference/ folders
- **Living Documentation** - Auto-updated with code changes
- **Convention Standards** - Consistent formatting and structure

#### 2. Task Management
- **Task Folders** - Individual workspace for each task
- **Research Documentation** - Context gathering and analysis
- **Implementation Planning** - Detailed plans with todos
- **Audit Process** - Post-implementation quality review

#### 3. Workflow Guidance
- **Mandatory Steps** - Required reading and preparation
- **Phase Structure** - Understanding → Planning → Implementation → Validation
- **Quality Gates** - Testing, linting, documentation requirements

#### 4. Handoff Protocol
- **Session Continuity** - Clear status and next steps
- **Context Preservation** - Sufficient detail for resumption
- **Integration Notes** - Dependencies and coordination

### Technical Features

#### 1. File Organization
```
memory-bank/
├── docs/               # Project documentation
│   ├── architecture/   # System design and ADRs
│   ├── prd.md         # This document
│   └── implementation_plan.md
├── tasks/              # Task workspace
│   ├── roadmap.md     # Task status tracking
│   └── [task-id]/     # Individual task folders
└── reference/          # Standards and guidelines
    ├── WORKFLOW.md    # How to work
    ├── CONVENTIONS.md # Coding standards
    └── CHECKLIST.md   # Quality validation
```

#### 2. Template Files
- **Example Task** - Complete demonstration of workflow
- **Documentation Templates** - Consistent structure across files
- **Quality Checklists** - Validation requirements

## Technical Requirements

### Technology Stack

#### Core Technologies
- **Language**: Python
- **Interface**: Streamlit
- **Search Engine**: Exa AI SDK
- **AI Synthesis**: Claude Code / Anthropic API
- **Environment**: `.env` for `EXA_API_KEY` management
- **Documentation**: Markdown with frontmatter
- **Version Control**: Git with structured commit messages
- **AI Assistant**: Claude Code (primary), extensible to others

#### Development Environment
- **Editor**: Any with markdown support
- **Local Server**: Streamlit dev server
- **Linting**: Ruff or Flake8 for Python, Markdown linting for consistency
- **Testing**: Pytest for unit and integration tests

### Integration Requirements

#### AI Assistant Integration
- **Structured Prompts** - Clear instructions in CLAUDE.md
- **Context Management** - Efficient file reading and understanding
- **Task Coordination** - Todo list management and progress tracking

#### Project Integration
- **Existing Codebases** - Template can be added to any project
- **Framework Agnostic** - Works with any tech stack
- **CI/CD Compatible** - Supports automated workflows

## Success Metrics

### Quality Metrics
- **Documentation Coverage** - All components have purpose statements
- **Task Completion Rate** - Percentage of tasks completed following workflow
- **Handoff Effectiveness** - Successful session continuations

### Efficiency Metrics
- **Setup Time** - Time to productive development start
- **Context Switch Time** - Time to resume interrupted work
- **AI Productivity** - Reduced clarification needs and improved output quality

### User Experience Metrics
- **Workflow Adherence** - AI agents follow prescribed steps
- **Documentation Quality** - Clear, actionable, and current
- **Error Reduction** - Fewer mistakes due to clear guidelines

## Non-Functional Requirements

### Performance
- **Fast Context Loading** - Efficient file organization for AI reading
- **Scalable Structure** - Supports projects of various sizes
- **Minimal Overhead** - Template doesn't slow development

### Reliability
- **Consistent Structure** - Predictable organization across projects
- **Version Control Friendly** - All files work well with Git
- **Backup Friendly** - Easy to archive and restore

### Usability
- **Clear Instructions** - Self-documenting structure
- **Example-Driven** - Learn by seeing complete examples
- **Error Prevention** - Checklists and validation steps

## Future Enhancements

### Phase 2 Potential Features
- **Multiple Language Templates** - Language-specific enhancements
- **IDE Integration** - Editor plugins for workflow support
- **Automated Validation** - Git hooks for quality checking
- **Metrics Dashboard** - Track project health and progress

### Integration Possibilities
- **Issue Tracking** - Integration with GitHub/Jira
- **CI/CD Pipelines** - Automated testing and deployment
- **Team Communication** - Slack/Teams notifications
- **Analytics** - Development velocity and quality metrics

## Implementation Notes

### Current Status
- ✅ **Core Template** - Basic structure implemented
- ✅ **Workflow Documentation** - Guidelines and checklists created
- ✅ **Example Task** - Complete demonstration available
- 🚧 **Testing** - Validation with real projects ongoing

### Getting Started
1. **Copy Template** - Clone or copy template structure
2. **Customize CLAUDE.md** - Add project-specific rules
3. **Update PRD** - Replace this template with actual requirements
4. **Create First Task** - Follow workflow for initial feature

---

**Note**: This PRD template should be customized for each specific project while maintaining the core structure and principles.