# greytHR Leave Management System

A comprehensive leave management system built for Greytip Software (greytHR) with React frontend and Flask backend.

## Features

### Core Functionality
- **Employee Management**: Full CRUD operations for employee records
- **Leave Request Management**: Submit, approve, reject leave requests
- **Leave Balance Tracking**: Monitor remaining leave balances by type
- **Dashboard**: Overview of system statistics and recent activities
- **Role-based Access**: Different views for employees, managers, and HR

### Technical Features
- **Frontend**: React with TypeScript, Tailwind CSS
- **Backend**: Flask REST API with CORS support
- **Database**: SQLite with proper relationships
- **Testing**: Unit tests and integration tests
- **API Communication**: Frontend communicates exclusively via API calls

## Setup Instructions

### Backend Setup
1. Install Python dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`

### Frontend Setup
1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173`

## Testing

### Unit Tests
Run backend unit tests:
```bash
npm run test
```

### Integration Tests
1. Make sure the Flask server is running:
   ```bash
   python backend/app.py
   ```

2. Run integration tests:
   ```bash
   cd backend
   python tests/test_integration.py
   ```

## API Endpoints

### Employees
- `GET /api/employees` - Get all employees
- `POST /api/employees` - Create new employee
- `PUT /api/employees/<id>` - Update employee
- `DELETE /api/employees/<id>` - Delete employee

### Leave Requests
- `GET /api/leave-requests` - Get all leave requests
- `POST /api/leave-requests` - Create new leave request
- `PUT /api/leave-requests/<id>/approve` - Approve request
- `PUT /api/leave-requests/<id>/reject` - Reject request
- `DELETE /api/leave-requests/<id>` - Delete request

### Leave Balances
- `GET /api/leave-balances/<employee_id>` - Get employee leave balances

### Dashboard
- `GET /api/dashboard/stats` - Get dashboard statistics

## Database Schema

### Tables
1. **employees**: Employee information and roles
2. **leave_requests**: Leave request details and status
3. **leave_balances**: Available leave balances by type and year

### Sample Data
The system includes sample employees and leave balances for testing:
- Rajesh Kumar (Engineering - Senior Developer)
- Priya Sharma (HR - HR Manager)
- Arjun Patel (Sales - Sales Executive)
- Kavya Reddy (Marketing - Marketing Lead)
- Suresh Nair (Engineering - Team Lead)

## Usage

1. **Dashboard**: View system overview and recent activities
2. **Employee Management**: Add, view, and delete employee records
3. **Leave Requests**: Submit new requests and manage approvals
4. **Leave Balances**: Check remaining leave balances by employee

## Project Structure

```
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── tests/
│       ├── test_app.py     # Unit tests
│       └── test_integration.py # Integration tests
├── src/
│   ├── App.tsx            # Main React application
│   ├── main.tsx           # React entry point
│   └── index.css          # Tailwind styles
└── package.json           # Node.js dependencies
```

This system demonstrates full-stack development with proper separation of concerns, comprehensive testing, and production-ready features for an internal HR leave management system.