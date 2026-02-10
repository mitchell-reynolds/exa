---
title: Coding and Documentation Conventions
description: Coding and documentation standards
---

## Documentation Standards

### File Purpose Headers
**MANDATORY**: Every file must start with a clear purpose statement.

**For Markdown files** - Use frontmatter:
```yaml
---
title: "Descriptive File Title"
description: "What this file contains and its purpose"
---
```

**For Python files** - Use ABOUTME comments:
```python
# ABOUTME: Brief description of what this module does
# ABOUTME: Second line if needed for complex modules
```

**For other files** - Use appropriate comment syntax with ABOUTME prefix.


### CLAUDE.md files 

When generating `CLAUDE.md` files for a subdirectory (module), include a structured manifest, for instance:
```markdown
# Backend Module Overview
Quick description of this module's purpose...

## Key Files
- `server.js` - Express server setup, middleware configuration
- `routes/api.js` - RESTful API endpoints for economic data
- `services/dataFetcher.js` - External API integration logic

## Current State
- ✅ Basic server setup complete
- 🚧 Auth middleware in progress (see TASK_001)
- ❌ Rate limiting not implemented

## Dependencies
- External: fred-api, yahoo-finance
- Internal: shared/validators, shared/types
```

### Living Documentation Rule

When making changes to code or architecture:
1. **ALWAYS** update related documentation in the same commit
2. **Key files to keep synchronized in `memory-bank`**:
   - `docs/architecture/OVERVIEW.md` - when changing system components or data flow
   - `docs/prd.md` - when changing requirements or success criteria
   - `reference/data_schemas.md` - when modifying data structures
   - `tasks/roadmap.md` - when completing or modifying tasks
   - `docs/implementation_plan.md` - overall implementation plan

