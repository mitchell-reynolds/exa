---
title: "Project Execution Roadmap Template"
description: "Template for organizing task execution with parallelization strategy"
---

# Project Execution Roadmap

## Overview

This roadmap shows the optimal execution order for [X] implementation tasks. You can run them sequentially with a single agent (safest) or parallelize with multiple agents (faster but requires careful coordination).

## Task Completion Status

**Progress**: 0/[X] tasks complete

### Phase 1: [Phase Name] (0/[N])
- [ ] 1.1 - [Task Name]
- [ ] 1.2 - [Task Name]
- [ ] 1.3 - [Task Name]

### Phase 2: [Phase Name] (0/[N])
- [ ] 2.1 - [Task Name]
- [ ] 2.2 - [Task Name]

[Continue for all phases...]

## Execution Strategy

**Safety First**: Default to sequential execution. Parallelization is optional and only recommended when you have multiple agents and clear confidence in avoiding conflicts.

**Key Principle**: Tasks within the same module/file area should run sequentially to avoid conflicts. Tasks touching different parts of the system can potentially run in parallel.

## Week-by-Week Execution Plan

### Week 1: [Week Theme]

**CRITICAL PATH (Must Complete Sequential)**:
```
1.1 Task Name → 1.2 Task Name → 1.3 Task Name
```

**TIMING BREAKDOWN - When Tasks Can Start**:

```
Time 0: Agent 1 starts 1.1 [Task Name] (prerequisite)
        Agent 2, 3 wait (need X to complete first)

After 1.1 ✅: Agent 1 starts 1.2 [Task Name]
             Agent 2 can start 2.1 [Task Name] (needs 1.1, no conflicts)
             Agent 3 can start [research/planning] (read-only activities)

After 1.2 ✅: Agent 1 starts 1.3 [Task Name]
             Agent 2 continues 2.1
             Agent 3 continues current task

After 1.3 ✅: [Phase/system] complete, enables [next phase]
```

**Dependencies**:
- [Task] needs [other task] to complete first ([reason])
- [Task] and [task] must be sequential ([reason])

**Files Touched**: `/src/[module]/`, `/[other-path]/`

### Week 2: [Week Theme]

[Follow same pattern...]

## Safety Guidelines

### Single Agent Execution (Recommended)
If you prefer to avoid any parallelization conflicts, here's the complete sequential order:

```
Week 1: 1.1 → 1.2 → 1.3 → 2.1
Week 2: 2.2 → 2.3 → 3.1 → 3.2
[Continue with all tasks...]
```

**Total**: All [X] tasks accounted for in dependency-safe order.

### Multi-Agent File Conflict Rules
- **Never** have multiple agents edit the same module simultaneously
- **[System Component]** (X.X-X.X): Single agent only
- **[System Component]** (X.X-X.X): Tasks A and B must be sequential, C/D can parallel each other
- **APIs vs Services**: APIs can be built parallel to the services they wrap
- **UI**: Can work parallel to backend once APIs exist

## Quick Start Guide

### Start Here (Single Agent)
Begin with **1.1 - [First Task]** and follow the Week 1 critical path.

### Start Here (Multiple Agents)
1. **Agent 1**: Start 1.1 - [First Task]
2. **Agent 2**: Wait for 1.1, then start [next task]
3. **Agent 3**: Begin [research/planning] (read-only)

### High-Risk Integration Points
- **[System Component]** (X.X-X.X): Core dependency for [other features]
- **[System Component]** (X.X-X.X): Foundation for all [category] processing
- **[System Component]** (X.X-X.X): Blocks [other component] development

## Dependency Matrix

### Critical Dependencies (Must be Sequential)
```
1.1 First Task
  └── 1.2 Second Task
      └── 1.3 Third Task
          └── 2.1 Next Phase Task

2.1 Base Models
  └── 2.2 Dependent Models
      └── 3.1 Services Using Models
```

### Safe Parallel Zones
```
Week 1-2:
├── Track 1: [Tasks that don't conflict]
├── Track 2: [Independent tasks]
└── Track 3: [Research/planning tasks]

Week 3:
├── Track 1: [Core pipeline tasks]
├── Track 2: [Infrastructure tasks]
└── Track 3: [UI/Integration tasks]
```

## Synchronization Points

### Week 1 End: [Milestone Name]
**Deliverables Required**:
- [Component]: [Specific deliverables]
- [Component]: [Specific deliverables]
- [Component]: [Specific deliverables]

**Integration Test**: [Test description]

### Week 2 End: [Milestone Name]
[Continue pattern...]

## Risk Management

### High-Risk Conflicts
1. **[Conflict Area]**: [Description of conflict]
   - **Mitigation**: [How to avoid]

2. **[Conflict Area]**: [Description of conflict]
   - **Mitigation**: [How to avoid]

### Communication Protocols
1. **Daily Sync**: Brief status update on blocking issues
2. **Weekly Integration**: Full system integration testing
3. **Merge Strategy**: Feature branch per task, frequent merges to avoid conflicts

## Success Metrics

### Weekly Milestones
- **Week 1**: [Goal]
- **Week 2**: [Goal]
- **Week 3**: [Goal]

### Quality Gates
- Each track maintains >90% test coverage
- All integration tests pass at synchronization points
- No merge conflicts in critical path components
- Documentation complete for all public interfaces

---

**Next Action**: Begin with Task 1.1 - [First Task] while other tracks prepare research and planning phases.

## How to Use This Template

### For New Projects
1. **Copy this template** to your project's `memory-bank/tasks/roadmap.md`
2. **Replace placeholders** with your actual tasks from `implementation_plan.md`
3. **Identify dependencies** between your specific tasks
4. **Group tasks by week** based on complexity and dependencies
5. **Create timing breakdowns** for each week showing when agents can start tasks
6. **Test the plan** with a small team to identify conflicts

### Key Sections to Customize
- **Task Completion Status**: Copy task IDs and names from your implementation plan
- **Week-by-Week Plan**: Group your tasks by realistic weekly goals
- **Timing Breakdowns**: Map out exact dependencies and start conditions
- **Safety Guidelines**: Create sequential fallback path for all tasks
- **File Conflicts**: Identify modules where parallel work would conflict

### Best Practices
- **Start conservatively**: Use single-agent execution until you understand the dependencies
- **Test parallelization**: Try with 2 agents before scaling to 3+
- **Update frequently**: Adjust the roadmap as you discover new dependencies
- **Document conflicts**: Record any parallelization issues you encounter for future reference