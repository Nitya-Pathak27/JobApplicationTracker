# 🚀 Job Application Tracker

A Flask and MySQL based web application that helps users efficiently manage and track their job applications in one place.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![Git](https://img.shields.io/badge/Git-Version_Control-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)


## 📌 Project Overview

Job Application Tracker is a web application developed using **Python Flask** and **MySQL** that allows user to organize and manage their job applications efficiently.

The appliation enables users to:

- Register and log in securely
- Add new job applications 
- Edit existing applications
- Delete applications
- Search applications
- Filter applications by status 
- Sort applciations by company or application date
- View upcoming applictions deadline

## ✨ Features

- 🔐 User Authentication
- ➕ Add Job Applications
- ✏️ Edit Applications
- 🗑 Delete Applications
- 🔍 Search by Company or Position
- 📂 Filter by Application Status
- 📅 Sort Applications
- ⏰ Upcoming Deadline Reminders
- 💻 Responsive User Interface

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2

### Backend 
- Python
- Flask

### Database
- MySQL

## 📂 Folder Structure

```text
JobApplicationTracker/
│
├── market/
│   ├── app.py
│   ├── db.py
│   ├── routes/
│   ├── database/
│   ├── static/
│   ├── templates/
│   └── utils.py
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env (not included in repository)
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/Nitya-Pathak27/JobApplicationTracker.git
```

2. Navigate to the project

```bash
cd JobApplicationTracker
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create a `.env` file and configure your MySQL credentials.

7. Run the application.

## 🚀 Future Improvements

- Email notifications for upcoming deadlines
- Resume upload support
- Application analytics dashboard
- Calendar integration
- Dark mode
- Export applications to PDF or Excel

## 👨‍💻 Author

**Nitya Pathak**

GitHub: https://github.com/Nitya-Pathak27