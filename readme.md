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
   