# Blog API Project

A RESTful API for a blog platform built with Python, SQLAlchemy, and Pydantic.

## Overview

This project provides a backend API for a blog application where users can:
- Register and login with secure authentication
- Create, read, update, and delete blog posts
- View other users and their blog posts

## Technologies Used

- Python 3.13.3
- SQLAlchemy (ORM for database operations)
- Pydantic (for data validation and serialization)
- JWT Authentication (for secure user sessions)

## Features

- **User Management**: Registration, authentication, and profile viewing
- **Blog Management**: Create, read, update, and delete blog posts
- **Security**: Password hashing and JWT token-based authentication

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/milad-sol/blog-api.git
   cd blog-api
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables (create a `.env` file with necessary configurations)

5. Run the application:
   ```bash
   python main.py
   ```

## API Endpoints

- **Authentication**
  - POST `/login` - User login and token generation
  
- **Users**
  - POST `/users` - Create a new user
  - GET `/users/{id}` - Get user details including their blogs
  
- **Blogs**
  - GET `/blogs` - List all blogs
  - POST `/blogs` - Create a new blog post
  - GET `/blogs/{id}` - Get a specific blog post
  - PUT `/blogs/{id}` - Update a blog post
  - DELETE `/blogs/{id}` - Delete a blog post

## Data Models

- **User** - Represents application users with authentication details
- **Blog** - Represents blog posts created by users

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
