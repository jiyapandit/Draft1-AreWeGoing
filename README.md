# AreWeGoing?

Document file relationships and cleanup plan
Mar 3
·
AreWeGoing
·
main

Archive

Share

Create PR


1
Now create a small description on all the files we have created, which file should be connected to which one, what are we doing and why that is there and also remove unnecessary things and what would be our plan of actions
Copy
Summary
Expanded README.md from a single-line placeholder into a concise project guide describing the current file, its purpose, how files should connect, and why the documentation exists at this stage.

Added a cleanup section that identifies unnecessary early-stage artifacts to avoid (unused configs, empty folders, placeholder scripts).

Added a practical plan of action for next steps, including scope definition, minimal architecture, documentation discipline, vertical-slice delivery, and continuous cleanup.

Added a reusable rule for documenting every new file going forward (what it does, what uses it, and why it is needed now).

Committed the change (64ee793) and created a PR via the make_pr tool.

Testing

✅ git diff -- README.md

✅ nl -ba README.md

✅ git status --short


File (1)
now what should be our 1st step
Copy


Diff
Logs

README.md
README.md
+36
-0

# AreWeGoing?

This repository is currently in a very early setup phase.

## Project files we have right now

### `README.md`
- **Purpose:** Single source of truth for what exists in the repo today and what we plan to build next.
- **Connected to:** For now, no other files (this is the only file).
- **Why it exists:** To keep direction clear before adding code.

## What we are doing
We are defining the project structure first so that new files are intentional, connected, and documented from day one.

## What is unnecessary right now
Because the project has not started implementation yet, we should avoid adding:
- Unused config files (`docker-compose.yml`, CI workflows, linters) before code exists.
- Empty folders with no owner or purpose.
- Placeholder scripts that are never run.

## Plan of action
1. **Define scope**
   - Write a short feature goal: what "AreWeGoing" should answer and for whom.
2. **Create minimal architecture**
   - Add only the first required files (app entry point + one config file + one test file).
3. **Document file ownership**
   - For each new file, add a one-line purpose in this README.
4. **Implement in vertical slices**
   - Build one end-to-end flow first (input -> logic -> output).
5. **Keep cleanup continuous**
   - Remove dead files and stale docs in every pull request.

## Rule for every new file
When adding a new file, include:
- What it does.
- Which files import/use it.
- Why it is needed now (not later).
