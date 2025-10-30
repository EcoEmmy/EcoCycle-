# EcoCycle - Waste Management System

## Overview
EcoCycle is a comprehensive waste management and recycling incentive platform built with Flask and SQLite. The application enables users to log waste disposal activities, earn points for recycling, and redeem rewards. It includes both user-facing features and an administrative dashboard for managing the system.

## Project Status
- **Last Updated**: October 30, 2025
- **Status**: Fully operational and ready for use
- **Environment**: Replit

## Recent Changes
- October 30, 2025: Major database migration and feature enhancements
  - **Database Migration**: Converted from SQLite to PostgreSQL
    - All SQL queries updated to PostgreSQL syntax
    - Using psycopg2 for database connectivity
    - Requires DATABASE_URL environment variable (see DATABASE_SETUP.md)
  - **Photo Upload Enhancement**: Waste logging now accepts photos without barcode/QR requirement
  - **Map Update**: Map centered on University of Ibadan (7.3912°N, 3.9167°E)
  - Updated all dependencies in requirements.txt
  - Updated create_admin.py for PostgreSQL compatibility
- October 30, 2025: Initial setup in Replit environment
  - Installed Python 3.11 and all required dependencies
  - Configured workflow to run Flask app on port 5000
  - Created .gitignore for Python projects

## Technology Stack
- **Backend**: Flask 3.0.3
- **Database**: PostgreSQL (via psycopg 3.2.12 - Render-compatible)
- **Authentication**: Werkzeug password hashing
- **Template Engine**: Jinja2
- **Web Server**: Flask development server (dev) / Gunicorn (production)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **Maps**: Leaflet with OpenStreetMap tiles

## Project Architecture

### Database Schema
The application uses PostgreSQL with the following main tables:
- `students`: User accounts with authentication and points tracking
- `waste_logs`: Waste disposal records with approval workflow
- `rewards`: Available rewards for redemption
- `redeemed_rewards`: Record of redeemed rewards
- `admins`: Administrator accounts
- `developers`: Team member profiles
- `sponsors`: Partner/sponsor information
- `booths`: Waste collection booth locations
- `site_settings`: Customizable site configuration
- `contact_messages`: User contact form submissions

### Key Features
1. **User System**
   - Registration and login with secure password hashing
   - Personal dashboard with stats
   - Waste logging with photo upload
   - QR/Barcode scanning support
   - Points tracking (current and lifetime)
   - Reward redemption

2. **Admin System**
   - Secure admin authentication
   - Waste log approval workflow
   - Reward management
   - User management (activate/deactivate)
   - Developer profile management
   - Sponsor/collaborator management
   - Booth location management
   - Student data export

3. **Rewards System**
   - Points earned: 1kg waste = 10 points
   - Leaderboard based on lifetime points
   - Reward catalog with images
   - Redemption tracking

### File Structure
```
.
├── app.py                 # Main Flask application
├── create_admin.py        # Admin account creation utility
├── requirements.txt       # Python dependencies
├── ecocycle.db           # SQLite database
├── static/               # Static assets
│   ├── css/
│   ├── js/
│   └── images/
├── templates/            # HTML templates
└── uploads/              # User-uploaded files
    ├── developers/
    ├── rewards/
    ├── sponsors/
    └── waste/
```

### Configuration
- **Port**: 5000 (configured for Replit)
- **Host**: 0.0.0.0 (allows external access)
- **Session Secret**: Environment variable `SESSION_SECRET` or default
- **Upload Folder**: `uploads/`
- **Max Upload Size**: 16MB
- **Cache Control**: Disabled for all responses (no-cache headers)

## Running the Application

### Development
The application is configured to run automatically via Replit workflow:
```bash
python app.py
```

### Production (Deployment)
For production, the app uses Gunicorn as specified in `Procfile`:
```bash
gunicorn app:app
```

## Environment Variables
- `DATABASE_URL`: PostgreSQL connection string (REQUIRED - set by Replit when you create a PostgreSQL database)
- `SESSION_SECRET`: Flask session secret key (optional, has default)
- `PGHOST`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`, `PGPORT`: Individual PostgreSQL connection parameters (automatically set by Replit)

## Database Initialization
**IMPORTANT**: You must create a PostgreSQL database in Replit before running the application. See DATABASE_SETUP.md for detailed instructions.

The database tables are automatically created on first run via `init_db()` function. To manually create an admin account:
```bash
python create_admin.py
```

Default admin credentials:
- Username: admin
- Password: admin123 (change immediately after first login!)

## User Preferences
None specified yet.

## Notes
- The application includes cache-busting headers to ensure users see updates immediately
- Photo uploads are validated for image file types only
- **NEW**: Waste logging now accepts photos without requiring barcode/QR scans
- Waste logs require admin approval before points are awarded
- Points can only be redeemed once earned and approved
- Map is centered on University of Ibadan coordinates for accurate location tracking
- PostgreSQL provides better performance and scalability compared to SQLite
