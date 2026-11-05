# TaskFlow – Full-Stack Task Manager

TaskFlow is a small full-stack web application for creating, tracking, completing and deleting personal tasks.

## Features

- Create tasks with a title and optional description
- Mark tasks as complete or reopen them
- Delete tasks
- Persist task data in SQLite
- Validate task titles on the server
- Display task counts and user feedback

## Technology

- **Front end:** HTML, CSS
- **Back end:** Python, Flask
- **Database:** SQLite
- **Version control:** Git

## Run locally

1. Install Python 3.10 or later.
2. Clone this repository or download the source code.
3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000 in your browser.

The SQLite database (`tasks.db`) is created automatically when the application starts.

## Project structure

```text
task_manager_portfolio/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Engineering notes

The application uses parameterized SQL queries to avoid constructing SQL from raw user input. Input validation is performed on the server, and task operations use HTTP POST requests.

For production deployment, replace the development secret key, disable Flask debug mode, add authentication and CSRF protection, and configure a production WSGI server.

## Portfolio note

This is a learning and portfolio project. Extend it with user authentication, task categories, due dates, search, automated tests and deployment to demonstrate additional engineering skills.
