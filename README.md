# ERP Management System Backend

A scalable **ERP (Enterprise Resource Planning) Backend API** built using **FastAPI**, **SQLAlchemy**, **MySQL**, **JWT Authentication**, **Redis**, **Docker**, and **Alembic**.

The project demonstrates a production-style backend architecture with authentication, role-based authorization, employee management, HRMS, CRM, inventory, payroll, sales, project management, ticketing, reporting, and notification modules.

---

# Features

## Authentication & Authorization

* User Registration
* User Login
* JWT Authentication
* Refresh Token Authentication
* Password Hashing (bcrypt)
* Role-Based Access Control (RBAC)
* Permission Middleware

---

## HR Management

* Employee Management
* Department Management
* Designation Management
* Attendance Management
* Leave Requests
* Payroll Management
* Salary Structures
* Payslip Generation

---

## Inventory Management

* Product Management
* Category Management
* Supplier Management
* Inventory Tracking

---

## Sales Management

* Customer Management
* Sales Orders
* Sales Order Items
* Invoice Management

---

## CRM

* Client Management
* Lead Management
* Opportunity Tracking

---

## Project Management

* Project Management
* Project Task Management
* Timesheet Management

---

## Help Desk

* Ticket Management
* Notification Management

---

## Dashboard

Dashboard API with live statistics including:

* Employees
* Departments
* Attendance
* Leave Requests
* Products
* Tickets

---

## Backend Features

* FastAPI
* SQLAlchemy ORM
* Alembic Database Migrations
* MySQL Database
* Redis Integration
* Docker Support
* Pagination
* Searching
* Filtering
* Soft Delete
* Email Service
* Global Exception Handling
* Logging
* Unit Testing (Pytest)
* RESTful API Design

---

# Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Alembic
* MySQL
* Redis
* Docker
* JWT
* Pydantic
* Pytest
* Uvicorn

---

# Project Structure

```text
ERP-Management-System
│
├── alembic/
├── models/
├── routers/
├── schemas/
├── services/
├── utils/
├── tests/
├── screenshots/
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Amanshaik2004/erp-management-system.git
```

Move into the project

```bash
cd erp-management-system
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Server

```bash
uvicorn main:app --reload
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Docker

Build Docker Image

```bash
docker build -t erp-management-system .
```

Run Container

```bash
docker run -p 8000:8000 erp-management-system
```

---

# API Testing

The repository includes:

* Postman Collection
* Swagger UI
* API Response Screenshots

---

# Testing

Run Unit Tests

```bash
pytest
```

---

# Future Improvements

* Forgot Password API
* Reset Password API
* Email Verification
* OTP Authentication
* File Uploads
* WebSocket Notifications
* CI/CD Pipeline
* Kubernetes Deployment

---

# Screenshots

API execution screenshots are available inside the **screenshots/** directory.

---

# Author

**Shaik Mohammed Aman**

Backend Developer | Python | FastAPI | SQL | Docker | Redis

---

# License

This project is intended for learning and portfolio purposes.
