---
title: "Implementation Checklist"
description: "Comprehensive checklist for task implementation and validation"
---

# Implementation Checklist

This checklist ensures consistent quality and completeness across all task implementations. Use this before marking any task as complete.

## 🔍 PHASE 1: Pre-Implementation Checklist

### 📋 Preparation (Before Starting Any Task)
- [ ] **Read required files**:
  - [ ] `memory-bank/reference/WORKFLOW.md`
  - [ ] `memory-bank/reference/CONVENTIONS.md`
  - [ ] `memory-bank/docs/prd.md` (if exists)
  - [ ] `memory-bank/docs/architecture/OVERVIEW.md` (if exists)
- [ ] **Create task folder** in `memory-bank/tasks/[task-id]/`
- [ ] **Document research** in `research.md`
- [ ] **Create implementation plan** in `plan.md` with todos
- [ ] **Get user approval** for the plan before implementing
- [ ] **Update todo list** using TodoWrite tool

### 🔍 Context Understanding
- [ ] **Understand current codebase** structure and patterns
- [ ] **Identify dependencies** and potential conflicts
- [ ] **Check existing implementations** for similar features
- [ ] **Verify technology stack** and available libraries
- [ ] **Document unknowns** and questions for user

## 💻 PHASE 3: During Implementation Checklist

### 💻 Code Development
- [ ] **Follow existing patterns** in codebase
- [ ] **Use TypeScript** with strict typing (if applicable)
- [ ] **Add ABOUTME comments** to all new files
- [ ] **Follow naming conventions** from surrounding code
- [ ] **Implement error handling** consistently
- [ ] **Add logging** where appropriate
- [ ] **Update todos** as work progresses

### 🧪 Testing Requirements
- [ ] **Write tests first** (TDD approach)
- [ ] **Unit tests** for individual functions/methods
- [ ] **Integration tests** for component interactions
- [ ] **End-to-end tests** for complete user flows
- [ ] **Edge case testing** for error conditions
- [ ] **Achieve >90% coverage** (verify with coverage tools)

### 📝 Documentation
- [ ] **Update relevant docs** in same commit as code changes
- [ ] **Add JSDoc comments** to public functions
- [ ] **Update API documentation** for new endpoints
- [ ] **Update architecture docs** if structure changes
- [ ] **Document configuration** requirements

## ✅ PHASE 4: Post-Implementation Checklist

### ✅ Code Quality Validation
- [ ] **Run linting** and fix all warnings (`npm run lint`)
- [ ] **Run type checking** and fix all errors (`tsc --noEmit`)
- [ ] **Run all tests** and ensure they pass
- [ ] **Check test coverage** meets requirements
- [ ] **Remove debug code** (console.logs, commented code)
- [ ] **Verify no security issues** (secrets, vulnerabilities)

### 🔄 Integration Verification
- [ ] **Test with existing features** to ensure no breaking changes
- [ ] **Verify database migrations** work correctly (if applicable)
- [ ] **Test error scenarios** and edge cases
- [ ] **Confirm API contracts** haven't changed unexpectedly
- [ ] **Check performance** hasn't degraded

### 📊 Documentation Sync
- [ ] **Update `docs/changelog.md`** with significant changes
- [ ] **Sync architecture docs** with implementation reality
- [ ] **Update `tasks/roadmap.md`** task status
- [ ] **Document any discovered issues** in `tasks/backlog.md`

## Task Completion Checklist

### 🎯 Success Criteria Verification
- [ ] **All todos marked complete** in task plan.md
- [ ] **All acceptance criteria met** from original requirements
- [ ] **User can test functionality** as described in handoff.md
- [ ] **No known critical issues** remaining
- [ ] **Ready for production** deployment

### 📋 Final Documentation
- [ ] **Create audit.md** (using implementation-auditor agent if requested)
- [ ] **Address audit findings** if any critical issues found
- [ ] **Write handoff.md** following HANDOFF_GUIDELINES.md
- [ ] **Update any parent docs** affected by this implementation

### 🔒 Security and Quality Gates
- [ ] **No hardcoded secrets** or credentials
- [ ] **Input validation** implemented where needed
- [ ] **Error messages** don't leak sensitive information
- [ ] **Dependencies** are up-to-date and secure
- [ ] **Code follows security best practices**

## Emergency Stops 🛑

**STOP and ask for help if:**
- You can't find critical files referenced in documentation
- Tests are failing and you can't determine why
- You're about to make changes that feel too large or risky
- You discover the requirements are unclear or contradictory
- You encounter errors you don't understand
- You need to deviate significantly from the approved plan

## Quality Gates by Project Type

### Web Applications
- [ ] **CORS configured** properly for frontend integration
- [ ] **Environment variables** documented and configurable
- [ ] **Database migrations** are reversible
- [ ] **API responses** follow consistent format

### CLI Tools
- [ ] **Help text** is clear and comprehensive
- [ ] **Error messages** are actionable
- [ ] **Exit codes** follow conventions
- [ ] **Configuration files** have clear schemas

### Libraries/Packages
- [ ] **Public API** is well-documented
- [ ] **Breaking changes** are clearly marked
- [ ] **Examples** are provided in documentation
- [ ] **Backward compatibility** is maintained (unless breaking version)

## Team Handoff Checklist

### When Multiple Agents Work on Project
- [ ] **Read previous handoff.md** files to understand context
- [ ] **Update shared roadmap** with current progress
- [ ] **Document any blocking issues** for next agent
- [ ] **Commit all work** before ending session
- [ ] **Write clear handoff.md** for next agent

### Session Continuity
- [ ] **All decisions documented** in task folder
- [ ] **Rationale captured** for design choices
- [ ] **Known issues logged** in appropriate files
- [ ] **Next steps clearly outlined** for continuation

---

## How to Use This Checklist

1. **Print or bookmark** this checklist for easy reference
2. **Check items as you go** - don't save everything for the end
3. **Stop immediately** if you can't check a critical item
4. **Ask for help** rather than skipping important validation steps
5. **Adapt as needed** but document any deviations

**Remember**: This checklist exists to help ensure quality and consistency. It's better to be thorough than fast!