# attendance-management-api
Production-ready attendance management REST API built with Flask and MySQL, designed with real-world business rules, role-based access, and extensibility in mind.


## Key Features

- User authentication and role-based access (Admin / Employee)
- Secure check-in and check-out system with automatic timestamping
- Validation to prevent invalid attendance states
- Attendance session tracking with historical records
- Admin-level attendance analytics and summaries
- Designed for easy future integration with AI and analytics modules

## Tech Stack

- Backend Framework: Flask
- Database: MySQL
- ORM: SQLAlchemy
- Authentication: JWT
- API Style: REST

## Core Business Rules

- A user can only have one active attendance session at a time
- Check-in timestamps are generated server-side to ensure data integrity
- Users cannot manually modify attendance times
- Check-out is only allowed for an active session
- Admin users have read-only access to attendance data
