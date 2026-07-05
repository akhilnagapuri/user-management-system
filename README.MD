# User Management System

A full-stack User Management System built with FastAPI, Django, and MongoDB.

## Tech Stack
- FastAPI (Backend - Port 8000)
- Django (Frontend - Port 8001)
- MongoDB (Database)

## Features
- JWT authentication & role-based authorization
- Create, edit, search, and manage users
- Soft delete with Trash & Restore workflow
- Clean layered architecture: Router → Service → Repository

## How to Run
1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Run FastAPI: uvicorn main:app --reload --port 8000
4. Run Django: python manage.py runserver 8001