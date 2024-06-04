# RealChat

RealChat is a real-time chat application built with Django and Django Channels. It supports user authentication, message storage, and real-time messaging.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)
5. [Project Structure](#project-structure)
6. [Testing](#testing)
7. [Contributing](#contributing)


## Features

- User Signup and Login, LogOut
- Real-time messaging using WebSockets
- Display online users
- Message history

## Requirements

- Python 3.10+
- Django 4.2+
- Django Channels 4.0+

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sumanbalayar08/RealChat.git
   cd RealChat

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

## Running the Project

1. **Apply the migrations:**

   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate

2. **Create A SuperUser:**

   ```bash
   python manage.py createsuperuser

3. **Run the development server:**

   ```bash
   python3 manage.py runserver
   
## Project Structure


The project structure is organized as follows:

- **Chatter/**: This directory contains the Django app for the chat functionality.
  - **migrations/**: Directory for Django database migrations.
  - **static/**: Directory for static files such as CSS, JavaScript, and images.
  - **templates/**: Directory for HTML templates.
  - **\_\_init\_\_.py**: Python package initialization file.
  - **admin.py**: Configuration for Django admin interface.
  - **apps.py**: Configuration for Django app.
  - **consumers.py**: WebSocket consumer for handling chat functionality.
  - **models.py**: Definition of Django models for message storage.
  - **routing.py**: Routing configuration for WebSocket connections.
  - **tests.py**: Unit tests for the app.
  - **urls.py**: URL configuration for the app.
  - **views.py**: Views for rendering HTML templates and handling HTTP requests.

- **RealChat/**: This directory contains the Django project settings and configuration.
  - **\_\_init\_\_.py**: Python package initialization file.
  - **asgi.py**: ASGI configuration for running the WebSocket server.
  - **settings.py**: Django project settings.
  - **urls.py**: URL configuration for the project.
  - **wsgi.py**: WSGI configuration for running the Django development server.

- **manage.py**: Django project management script for administrative tasks.

- **requirements.txt**: File listing all Python dependencies required to run the project.

- **README.md**: Project documentation file.
