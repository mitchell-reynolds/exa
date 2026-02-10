---
Title: Root Claude.md File
Description: Instructions that Claude must read every time. 
---

# Project Guidelines for Claude

This is a skeleton/template for creating new projects in Claude Code.

## MANDATORY FIRST STEPS - READ BEFORE ANY TASK

🛑 **STOP**: Before starting ANY task, you MUST:

1. ✅ **Read and understand** `memory-bank/reference/WORKFLOW.md`
2. ✅ **Read and understand** `memory-bank/reference/CONVENTIONS.md`
3. ✅ **Review relevant sections** of `memory-bank/reference/CHECKLIST.md` for your current phase
4. ✅ **Confirm** which workflow phase you're starting with (Understanding/Planning/Implementation/Validation)
5. ✅ **Create or update** your todo list using TodoWrite tool
6. ✅ **State explicitly** that you've read the required files

**If you skip these steps, STOP immediately and read them now.**

## Project Context

We are building an applet for Biotech researchers leveraging the Exa AI SDK. The core idea is to use Exa AI to search for relevant information and then use Claude Code to process, synthesize, and present it in a user-friendly format. We will want the user to simply input a query, and the applet will return an Executive Summary based on the search results from Exa AI. The summary should be comprehensive and well-structured, with clear headings and bullet points. 

Then below you want a UI friendly table of relevant information, ranked by relevance with generated summaries from Exa. The table should have columns for Title, URL, Category (eg research paper, news, tweet, etc.), and a Summary column.

See `memory-bank/prd.md` for our PRD. This template provides a structured foundation for AI-assisted development projects with clear documentation, task tracking, and quality standards.

## Documentation Standards

See `memory-bank/reference/CONVENTIONS.md` for documentation standards and conventions. You MUST read this file.

## Project-Specific Rules

- **Tech Stack**: Python, Streamlit, [Exa AI SDK](https://exa.ai/docs/sdks/python-sdk)
- **Exa AI and API Key**: Refer to the docs as much as needed which can be found here - [Exa AI](https://exa.ai/docs/sdks/python-sdk). Use `EXA_API_KEY` for environment variable within a `.env` file.
- **Small, incremental changes**: Make the smallest reasonable changes to achieve the desired outcome
- **Documentation first**: All code must have clear purpose statements and be documented before implementation
- **Test-driven development**: Write tests first, then implement features
- **No shortcuts**: Follow the complete workflow even for small tasks
- **Quality gates**: Code must pass linting, type checking, and tests before marking tasks complete

## Development Workflow

### CRITICAL: Always Follow the Workflow

**BEFORE STARTING ANY TASK**: You MUST follow the workflow defined in `memory-bank/reference/WORKFLOW.md`:
1. Create task subfolder in `memory-bank/tasks/[task-id]/` (e.g., `2-1-baml-foundation`)
2. Document research in the task subfolder's `research.md`
3. Create implementation plan with todos in `plan.md`
4. Get user approval before implementing
5. Track progress and update todos during implementation
6. Create `audit.md` for post-implementation review when requested, this will be another agent's audit of your work, you may have to fix something
7. Create `handoff.md` in the task subfolder following `memory-bank/reference/HANDOFF_GUIDELINES.md`

**NEVER skip this workflow** - it's critical for project organization and tracking.

### Task Implementation
1. Read the full task description in `docs/implementation_plan.md`
2. Check dependencies in `tasks/roadmap.md`
3. Update task status in roadmap when starting/completing
4. Follow the directory structure defined in `docs/architecture/OVERVIEW.md`

### Testing Requirements

- **Unit tests required**: All functions/methods must have unit tests with >90% coverage
- **Integration tests**: Test component interactions and data flow
- **Test first**: Write failing tests before implementing functionality
- **Run tests frequently**: Execute tests after each logical change
- **Test commands**: Use `npm test` or project-specific test commands (document in this file if different)

### Code Quality

- **Linting**: Code must pass linting with zero warnings (`npm run lint` or equivalent)
- **Type checking**: All TypeScript/typed code must pass type checking
- **No debug code**: Remove console.logs, debugger statements, and commented code before committing
- **Follow existing patterns**: Match the style and conventions of surrounding code
- **Code reviews**: All significant changes require review (use audit.md process)

## Memory Bank Organization

```text
memory-bank/
├── docs/               # Core project documentation
  |-- architecture/     # Architecture overview and ADRs
├── tasks/              # Task tracking and implementation workspace
└── reference/          # Standards, schemas, decisions, workflow
```

**Key Files:**
- `memory-bank/reference/WORKFLOW.md` - How to implement tasks
- `memory-bank/reference/data_schemas.md` - All data structure definitions
- `memory-bank/docs/architecture/OVERVIEW.md` - system design, ADR logs in `decision-records` subfolder
- `memory-bank/reference/TESTING.md` - Testing standards and patterns

## Parallel Development Guidelines

### When Multiple Agents Work Together

- **Clear handoffs**: Use handoff.md files to communicate context between agents
- **Shared task tracking**: Update roadmap.md when tasks are started/completed
- **Avoid conflicts**: Coordinate on files being modified simultaneously
- **Document decisions**: Record architectural decisions in decision-records/

### Critical Dependencies

- **Task dependencies**: Check tasks/roadmap.md before starting work
- **File dependencies**: Verify architecture/OVERVIEW.md for component relationships
- **External dependencies**: Document in prd.md and keep updated
- **Testing dependencies**: Ensure test environment is properly configured

## Error Handling Priorities

- **User-facing errors**: Provide clear, actionable error messages
- **System errors**: Log with sufficient context for debugging
- **Graceful degradation**: System should remain functional when non-critical components fail
- **Recovery strategies**: Document how to recover from common failure scenarios

## Success Metrics to Remember

- **Code quality**: Zero linting errors, passing tests, type safety
- **Documentation coverage**: All modules have purpose statements and key files are documented
- **Task completion**: All todo items marked complete, audit passed
- **User experience**: Features work as specified in PRD and meet acceptance criteria

## When in Doubt

1. Check the PRD first (`docs/prd.md`)
2. Review architecture overview and decisions (`docs/architecture/` files)
3. Follow the parallel execution strategy (`tasks/roadmap.md`)
4. Keep documentation synchronized with code changes
