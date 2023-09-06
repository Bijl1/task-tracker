# Task Tracker

![Task Tracker Logo](link_to_your_logo_image)

## Video Demo

Watch a demo of the Task Tracker [here](https://youtu.be/U5HyyJ0QGlc).

## Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## About

The Task Tracker is a web-based task management application that allows users to efficiently organize and keep track of their tasks. It is built using Python, the Flask web framework, and SQLite for data storage. The application features user authentication to ensure data privacy and security.

## Features

- **User Authentication:** Create an account or log in to access the application's features securely.
- **Task Creation:** Add new tasks with details like name, date, time, and description.
- **Task Listing:** View tasks in an organized list format for easy management.
- **Task Editing:** Modify existing tasks, including name, date, time, and description.
- **Task Deletion:** Remove tasks when they are completed or no longer needed.
- **User-Friendly Interface:** Intuitive and user-friendly design for accessibility.

## Project Structure

- `app.py`: Core Flask application with routes and user authentication.
- `database.db`: SQLite database file for storing user accounts and task data.
- HTML Templates (e.g., `index.html`, `signup.html`, `login.html`, `tasks.html`, `create_task.html`, `edit_task.html`): Define the layout and structure of web pages.
- `style.css`: CSS file for enhancing the visual appeal and user experience.

## Getting Started

To run the Task Tracker on your local machine, follow these steps:

1. Clone this repository: `git clone https://github.com/yourusername/task-tracker.git`
2. Install the required Python packages: `pip install -r requirements.txt`
3. Set up your Flask secret key (replace `'your_secret_key'` in `app.py`) for security.
4. Initialize the database: `python app.py initdb`
5. Run the application: `python app.py`

## Usage

1. Open your web browser and access the Task Tracker at `http://localhost:5000`.
2. Sign up for an account or log in if you already have one.
3. Start managing your tasks by adding, editing, and deleting them.

## Contributing

Contributions to the Task Tracker project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add feature-name'`
4. Push to your branch: `git push origin feature-name`
5. Create a pull request.

