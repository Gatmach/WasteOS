# ♻️ WasteOS

<div align="center">

**A Modern IoT Smart Waste Management Platform**

Built with **Django**, **Django REST Framework**, **PostgreSQL**, and **Docker**

*Monitor smart bins, optimize waste collection, and gain AI-powered operational insights.*

---

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-success?logo=django)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-API-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# Overview

WasteOS is an IoT-powered Smart Waste Management Platform designed to help organizations monitor waste bins in real time, optimize collection operations, and make data-driven decisions.

The platform integrates smart bins, IoT sensors, collection vehicles, operational management, analytics, and AI-powered recommendations into a single backend platform.

WasteOS follows a modular Django architecture with clean separation of responsibilities using Services, Selectors, Serializers, ViewSets, and REST APIs.

---

# Features

## Authentication & User Management

* Custom User Model
* JWT Authentication
* Login
* Logout
* Refresh Token
* Change Password
* User Profile (/me)
* Role-Based Access Control
* Organization-based Users
* Facility-based Users

---

## Organization Management

* Organizations
* Facilities
* Zones

---

## Smart Bin Management

* Smart Bins
* Fill Level Monitoring
* Battery Monitoring
* Bin Alerts
* Bin Status Tracking

---

## Sensor Management

* IoT Sensors
* Sensor Readings
* Historical Data

---

## Waste Collection Operations

* Drivers
* Collection Vehicles
* Collection Routes
* Collection Scheduling
* Collection Records

---

## Analytics

* KPI Snapshots
* Operational Statistics
* Collection Performance
* Waste Trends

---

## Artificial Intelligence

* Waste Forecasting
* Collection Recommendations
* Predictive Analytics

---

## Notifications

* Notification Management
* Alert Delivery
* Notification Logs

---

## Reports

* Operational Reports
* Collection Reports
* Analytics Reports

---

## Website

* Contact Messages
* FAQ
* Announcements
* Newsletter

---

# Technology Stack

## Backend

* Python 3.14
* Django 6
* Django REST Framework

## Database

* PostgreSQL

## Authentication

* JWT
* SimpleJWT

## API Documentation

* DRF Spectacular (OpenAPI)

## Filtering

* django-filter

## Containerization

* Docker

---

# Project Architecture

The project follows a layered architecture.

```
Client
    │
    ▼
ViewSet / API
    │
    ▼
Serializer
    │
    ▼
Services
    │
    ▼
Selectors
    │
    ▼
Models
    │
    ▼
Database
```

### Services

Business logic.

Examples:

* create_user()
* update_user()
* activate_user()

### Selectors

Read-only database queries.

Examples:

* list_users()
* get_user()
* search_users()

Keeping reads and writes separated improves maintainability and testing.

---

# Project Structure

```text
wasteOS/
│
├── apps/
│   ├── accounts/
│   ├── ai/
│   ├── analytics/
│   ├── bins/
│   ├── common/
│   ├── dashboard/
│   ├── notifications/
│   ├── operations/
│   ├── organizations/
│   ├── reports/
│   ├── sensors/
│   └── website/
│
├── config/
│
├── docker/
│
├── media/
├── static/
├── templates/
├── tests/
│
├── requirements/
│
├── manage.py
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/wasteOS.git
cd wasteOS
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your-secret-key
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

DATABASE_NAME=wasteos_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

```

---

# Database

Run migrations.

```bash
python manage.py migrate
```

Create a superuser.

```bash
python manage.py createsuperuser
```

---

# Run Development Server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

---

# Docker

Build containers.

```bash
docker compose build
```

Run the application.

```bash
docker compose up
```

---

# API Documentation

Swagger/OpenAPI documentation is available after the server starts.

Swagger UI

```
/api/schema/swagger-ui/
```

OpenAPI Schema

```
/api/schema/
```

---

# Authentication

WasteOS uses JWT Authentication.

### Login

```
POST /api/accounts/login/
```

### Refresh Token

```
POST /api/accounts/token/refresh/
```

### Logout

```
POST /api/accounts/users/logout/
```

### Current User

```
GET /api/accounts/users/me/
```

### Change Password

```
POST /api/accounts/users/change_password/
```

---

# Development Workflow

The project follows:

* Clean Architecture
* Service Layer Pattern
* Selector Pattern
* Thin ViewSets
* Business Logic inside Services
* Read Queries inside Selectors
* Modular Django Apps

---

# Current Modules

| Module       
| -------------
| Accounts    
| Organizations 
| Bins     
| Sensors   
| Operations  
| Dashboard  
| Analytics  
| AI        
| Notifications 
| Reports       
| Website       

---

# Roadmap

* Complete Organizations APIs
* Complete Bin Management APIs
* Complete Sensor APIs
* Complete Operations APIs
* Dashboard APIs
* Analytics Engine
* AI Predictions
* Notifications
* Reporting System
* Docker Deployment
* CI/CD
* Automated Testing

---

# Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# License

This project is licensed under the MIT License.

---

<div align="center">

**Built with ❤️ using Django & Django REST Framework**

</div>
