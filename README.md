# Django Session and Django Message

This project demonstrates how to use Django Session and Django Messages in a Django application.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Introduction
This project is a user login system built with Python and Django. 
It uses SQLite to store user data, Django Sessions to track state between the site and browser (storing information like login status and user preferences), and Django Messages to show helpful notifications.

## Features
- User registration with username, email and password
- Secure login and logout functionality
- Session management by Django Sessions
- Customizable message types (info, success, warning, error).
- Error handling for authentication issues


## Requirements
- Python 3.x or higher
- Django 5.x or higher
- Python Decouple 3.x or higher

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/PratesB/django_session_message.git
    ```
2. Navigate to the project directory:
    ```sh
    cd django_session_message
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` file with the necessary information:
    ```sh
    touch .env
    ```
    Add your environment-specific variables in the `.env` file:
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DB_ENGINE=django.db.backends.sqlite3
    DB_NAME=db.sqlite3
    ```

## Usage

1. Create a SuperUser (optional)  
    If you need access to the admin panel, create a superuser:  
    ```bash
    python manage.py createsuperuser
    ```

    Follow the instructions and set a username and password.

2. Run the application, use the following command:
    ```bash
    python manage.py runserver
    ```
3. Access the application:
- Home Page: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin (You should use your superuser credentials to log in)


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

