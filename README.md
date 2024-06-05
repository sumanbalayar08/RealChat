# RealChat

RealChat is a real-time chat application built with Django and Django Channels. It supports user authentication, message storage, and real-time messaging.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Running the Project](#running-the-project)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
  - [How to Initiate Messages](#how-to-initiate-messages)
  - [Example Workflow](#example-workflow)
7. [Testing](#testing)
8. [Contributing](#contributing)


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

- **static/**: Directory for static files and images.

- **templates/**: Directory for HTML templates.

- **manage.py**: Django project management script for administrative tasks.

- **requirements.txt**: File listing all Python dependencies required to run the project.

- **README.md**: Project documentation file.

## Usage

### How to Initiate Messages

#### Sign Up

1. Open your browser and navigate to the homepage.
2. Click on the Sign Up link or navigate to the sign-up page.
3. Fill in the required details such as username, email, password, and confirm your password.
4. Click the Sign Up button to create your account.

#### Log In

1. Navigate to the login page.
2. Enter your username and password.
3. Click the Log In button to access your account.

#### Access Chat Home

1. Once logged in, you will be redirected to the chat home page.
2. The chat home page displays a list of connected users who are online.
3. If no users are connected, you will see a message indicating that no users are available.

#### Open Another Browser and Repeat

1. To test the messaging feature, open a different browser or an incognito window and repeat the sign-up and login process with a different username.

#### Reload and Interact

1. Reload the browser to ensure the list of online users is updated.

#### Start a Chat

1. On the chat home page, click on the username of the user you want to chat with.
2. This will open a chat window where you can send and receive messages.

#### Send and Receive Messages

1. Type your message in the chat input field and press Enter or click the Send button to send the message.
2. The message will be displayed in the chat window.
3. To see messages from other users, reload the browser.

#### Repeat for Multiple Users

1. You can repeat the process of signing up, logging in, and chatting from different browsers or devices to simulate a real-time chat environment with multiple users.

### Example Workflow

#### Browser 1:

1. Sign up with username1.
2. Log in with username1.
3. Access chat home.

#### Browser 2:

1. Sign up with username2.
2. Log in with username2.
3. Access chat home.

#### Interaction:

1. In Browser 1, click on username2 and send a message.
2. Reload Browser 2 to see the message from username1.
3. In Browser 2, reply to the message from username1.
4. Reload Browser 1 to see the reply from username2.

## Testing

1. **Run unit tests:**

   ```bash
   python3 manage.py test Chatter
