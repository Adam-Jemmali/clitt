# Task Tracker CLI

A simple command-line tool to track tasks — what you need to do, what you're
working on, and what's done. Tasks are stored in a local `tasks.json` file
using only Python's built-in standard library (no external packages).

Based on the [Task Tracker project](https://roadmap.sh/projects/task-tracker)
from roadmap.sh.

## Requirements

- Python 3.7 or later (no external libraries needed — everything used is
  built into Python)

## Setup

1. Clone or download this project folder.
2. Make sure `task_cli.py` is in your project directory.
3. No installation step is required — you run it directly with Python.

## Running the app

All commands follow this pattern:

```bash
python task_cli.py <command> [arguments]
```

The first time you run any command, a `tasks.json` file will be created
automatically in the same folder. You don't need to create it yourself.

## Commands

### Add a task

```bash
python task_cli.py add "Buy groceries"
```
Output:
```
Task added successfully (ID: 1)
```

### Update a task's description

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as in progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

### List all tasks

```bash
python task_cli.py list
```

### List tasks by status

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

## Task data

Each task is stored as a JSON object with the following fields:

| Field         | Description                                      |
|---------------|---------------------------------------------------|
| `id`          | Unique numeric identifier, assigned automatically  |
| `description` | Short text describing the task                    |
| `status`      | One of `todo`, `in-progress`, `done`               |
| `createdAt`   | Timestamp of when the task was created             |
| `updatedAt`   | Timestamp of the last change to the task           |

Example `tasks.json` after adding one task:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-09-07 14:32:10",
    "updatedAt": "2026-09-07 14:32:10"
  }
]
```

## Error handling

- Running a command with missing arguments (e.g. `add` with no description)
  prints a usage message instead of crashing.
- Referencing a task ID that doesn't exist prints a clear error.
- Typing a non-numeric ID (e.g. `delete abc`) is caught and reported instead
  of crashing the program.
- If `tasks.json` doesn't exist yet, it's created automatically on first use.

## Notes

- Tasks are stored in `tasks.json` in the **current directory** — run the
  tool from the same folder each time so it reads/writes the same file.
- Task IDs are not reused after deletion (deleting task 2 won't cause a
  future task to also be numbered 2).