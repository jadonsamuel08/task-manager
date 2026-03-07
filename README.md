# Task Manager (CLI)

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-See%20LICENSE-lightgrey)

A lightweight command-line task manager built with Python.

This project lets you add tasks, view all tasks, and mark tasks as completed. Task data is persisted locally in `tasks.json`.

## Features

- Add tasks with title, due date, and priority
- Validate due date format (`YYYY-MM-DD`)
- Validate priority values (`low`, `medium`, `high`)
- View tasks with completion status
- Mark tasks as completed
- Persist tasks to local JSON storage

## Tech Stack

- Python 3
- JSON file storage (no external database)

## Project Structure

- `main.py` — CLI entry point and user interaction loop
- `planner.py` — task management logic
- `task.py` — `Task` model and serialization helpers
- `storage.py` — load/save task data from/to `tasks.json`
- `tasks.json` — persisted task data

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/jadonsamuel08/task-manager
cd task_manager
```

### 2) (Optional) Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Run the application

```bash
python main.py
```

## Usage

When you run the app, you’ll see this menu:

1. Add Tasks
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Typical flow:

- Choose `1` to add a task
- Choose `2` to list all tasks
- Choose `3` and enter a task ID to mark it complete
- Choose `4` to delete task
- Choose `5` to exit

## Data Storage

- All tasks are saved in `tasks.json`.
- If the file is missing, empty, or invalid JSON, the app starts with an empty task list.

## Future Improvements

- Edit and delete tasks
- Filter tasks by priority or completion status
- Sort tasks by due date
- Add unit tests
- Implement Flask app UI


