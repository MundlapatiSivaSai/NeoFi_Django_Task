# NeoFi Django Task

This repository contains the Django backend for the NeoFi note-taking application. It's designed to provide a RESTful API for managing notes, including functionalities such as user authentication, note creation, sharing, and accessing version history.

## Demo

Check out the live demo of the application: [NeoFi Django Task Demo](https://neofibysiva.onrender.com/)

## Features

- User authentication (signup and login)
- Note management (create, update, delete)
- Note sharing among users
- Accessing note version history

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

1. **Clone the repository**

   ```
   git clone https://github.com/MundlapatiSivaSai/NeoFi_Django_Task.git
   cd NeoFi_Django_Task
   ```

2. **Set up a virtual environment** (optional but recommended)

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Migrate the database**

   ```
   python manage.py migrate
   ```

5. **Create a superuser** (optional for admin access)

   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`.

### Usage

- **User Registration**: `POST /api/signup`
- **User Login**: `POST /api/login`
- **Create Note**: `POST /api/notes/create`
- **Share Note**: `POST /api/notes/share`
- **Note Version History**: `GET /api/notes/version-history/{id}`

## Running the Tests

Explain how to run the automated tests for this system.

```
python manage.py test
```


## Authors

- **Mundlapati Siva Sai** -
