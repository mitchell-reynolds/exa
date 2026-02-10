---
title: "System Architecture Overview"
description: "High-level system design, components, and their interactions; includes target directory structure - needs to be kept updated"
---

# System Architecture Overview

## Project Structure

This template uses a standardized directory structure to support AI-assisted development:

```text
project-root/
├── CLAUDE.md                    # AI agent instructions (mandatory reading)
├── README.md                    # Project overview and setup
├── memory-bank/                 # Structured documentation and workflow
│   ├── docs/                   # Core project documentation
│   │   ├── architecture/       # System design documents
│   │   │   ├── OVERVIEW.md    # This file - high-level architecture
│   │   │   └── decision-records/ # ADR (Architecture Decision Records)
│   │   ├── prd.md             # Product Requirements Document
│   │   ├── implementation_plan.md # Overall roadmap
│   │   └── changelog.md       # Change tracking
│   ├── tasks/                  # Task management workspace
│   │   ├── roadmap.md         # Task status dashboard
│   │   ├── backlog.md         # Issue tracking
│   │   └── [task-id]/         # Individual task workspaces
│   │       ├── research.md    # Context and investigation
│   │       ├── plan.md        # Implementation plan with todos
│   │       ├── audit.md       # Quality review
│   │       └── handoff.md     # Session handoff documentation
│   └── reference/              # Standards and guidelines
│       ├── WORKFLOW.md        # How agents should work
│       ├── CONVENTIONS.md     # Coding standards
│       ├── CHECKLIST.md       # Quality validation
│       ├── HANDOFF_GUIDELINES.md # Session transition standards
│       └── data_schemas.md    # Data structure definitions
├── src/                        # Source code (project-specific)
├── tests/                      # Test files (project-specific)
├── docs/                       # External/user documentation
└── [project-specific files]   # Package.json, config files, etc.
```

## Core Components

### 1. Memory Bank System

**Purpose**: Centralized knowledge management for AI-assisted development

**Components**:
- **docs/**: Project-wide documentation that evolves with the codebase
- **tasks/**: Individual task workspaces with complete context
- **reference/**: Stable guidelines and standards

**Key Principles**:
- Living documentation that stays synchronized with code
- Task isolation to prevent context mixing
- Clear handoff protocols for session continuity

### 2. Task Management Framework

**Purpose**: Structure complex work into manageable, trackable units

**Workflow Phases**:
1. **Understanding** - Research and context gathering
2. **Planning** - Detailed implementation planning with todos
3. **Implementation** - Execution with progress tracking
4. **Validation** - Testing, quality checks, and review

**Coordination**:
- `roadmap.md` - High-level task status and dependencies
- `backlog.md` - Discovered issues and future enhancements
- Individual task folders with complete context

### 3. Quality Assurance System

**Purpose**: Ensure consistent quality and standards across implementations

**Components**:
- **Mandatory Reading** - Required files before starting any task
- **Quality Checklists** - Validation steps for completeness
- **Audit Process** - Post-implementation review
- **Documentation Standards** - Consistent formatting and structure

### 4. AI Agent Integration

**Purpose**: Enable effective AI-assisted development with clear guidelines

**Integration Points**:
- **CLAUDE.md** - Primary instructions and project context
- **WORKFLOW.md** - Step-by-step process guidelines
- **TodoWrite integration** - Progress tracking throughout tasks
- **Handoff protocols** - Session continuity between agents

## Data Flow

### Task Lifecycle

```text
User Request → Research Phase → Planning Phase → Implementation Phase → Validation Phase
      ↓              ↓              ↓                 ↓                    ↓
 Task Created → research.md → plan.md (todos) → Code Changes → audit.md → handoff.md
      ↓              ↓              ↓                 ↓                    ↓
 Roadmap Updated → Context Gathered → User Approval → Tests Written → Quality Gates
```

### Documentation Synchronization

```text
Code Changes → Related Doc Updates → Living Documentation → Architecture Updates
      ↓               ↓                       ↓                    ↓
Implementation → Plan Updates → Convention Compliance → Decision Records
```

## Design Decisions

### 1. File-Based Knowledge Management

**Decision**: Use markdown files in structured directories instead of database
**Rationale**:
- Version control friendly
- Human readable
- AI assistant friendly
- No external dependencies

### 2. Task Isolation

**Decision**: Each task gets its own subfolder with complete context
**Rationale**:
- Prevents context mixing
- Enables parallel work
- Clear handoff boundaries
- Easy to archive completed work

### 3. Mandatory Reading Protocol

**Decision**: Force AI agents to read key files before starting any task
**Rationale**:
- Ensures consistency across sessions
- Reduces clarification needs
- Maintains quality standards
- Prevents workflow shortcuts

### 4. Living Documentation

**Decision**: Documentation updates required in same commit as code changes
**Rationale**:
- Prevents documentation drift
- Maintains accuracy
- Reduces maintenance overhead
- Improves long-term project health

## Integration Patterns

### AI Assistant Integration

```text
User Request → Mandatory Reading → Context Analysis → Task Creation → Implementation
      ↓              ↓                    ↓              ↓              ↓
CLAUDE.md Read → Workflow Followed → Research Done → Plan Approved → Quality Gates
```

### Team Collaboration

```text
AI Implementation → Human Review → Quality Validation → Documentation Update
        ↓               ↓               ↓                    ↓
    handoff.md → User Testing → audit.md Review → Architecture Update
```

### Project Integration

```text
Template Copy → Customization → First Task → Iterative Development
      ↓              ↓             ↓              ↓
Project Setup → CLAUDE.md → Workflow Test → Production Use
```

## Quality Attributes

### Maintainability
- **Clear Structure**: Predictable organization
- **Documentation Standards**: Consistent formatting
- **Living Docs**: Always current with code

### Reliability
- **Quality Gates**: Testing and validation requirements
- **Handoff Protocols**: Reliable session transitions
- **Version Control**: Full change tracking

### Usability
- **Self-Documenting**: Structure explains itself
- **Example-Driven**: Learn by seeing complete examples
- **Error Prevention**: Checklists and validation

### Scalability
- **Parallel-Safe**: Multiple agents can work simultaneously
- **Task Isolation**: No cross-contamination
- **Modular Structure**: Easy to extend and customize

## Future Architecture Considerations

### Phase 2 Enhancements
- **Automated Validation**: Git hooks for quality checking
- **IDE Integration**: Editor plugins for workflow support
- **Metrics Collection**: Development velocity tracking
- **Template Variants**: Language-specific optimizations

### Integration Opportunities
- **CI/CD Pipelines**: Automated testing and deployment
- **Issue Tracking**: GitHub/Jira integration
- **Team Communication**: Slack/Teams notifications
- **Analytics Dashboard**: Project health monitoring

---

## Maintenance Notes

This architecture overview should be updated when:
- New components are added to the system
- Workflow changes are made
- Integration patterns change
- Quality requirements evolve

All changes should be documented in `decision-records/` with ADR format.