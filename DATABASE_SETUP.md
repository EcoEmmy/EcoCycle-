# PostgreSQL Database Setup Guide

## Important: Database Requirement

This application now uses **PostgreSQL** instead of SQLite. You must create a PostgreSQL database in Replit before running the application.

## Setup Steps

### 1. Create PostgreSQL Database in Replit

1. Open your Replit project
2. Go to the **Tools** panel on the left sidebar  
3. Click on **Database**
4. Click **Create database** button
5. Select **PostgreSQL**
6. Replit will automatically create the database and set up the `DATABASE_URL` environment variable

### 2. Verify Database Connection

After creating the database, the following environment variables will be automatically available:
- `DATABASE_URL` - Full PostgreSQL connection string
- `PGHOST` - Database host
- `PGUSER` - Database username  
- `PGPASSWORD` - Database password
- `PGDATABASE` - Database name
- `PGPORT` - Database port

### 3. Initialize Database Tables

The application will automatically create all required tables when it first starts. The `init_db()` function will create:

- `students` - User accounts
- `admins` - Administrator accounts
- `waste_logs` - Waste submission records
- `rewards` - Available rewards
- `redeemed_rewards` - Redemption history
- `developers` - Team member profiles
- `sponsors` - Partner organizations
- `booths` - Collection booth locations
- `site_settings` - Site customization
- `contact_messages` - Contact form submissions

### 4. Create First Admin Account

Run the admin creation script:

```bash
python create_admin.py
```

Default credentials:
- **Username**: admin
- **Password**: admin123

⚠️ **Important**: Change these credentials immediately after first login!

## Key Changes from SQLite

1. **Database Library**: Uses `psycopg` (version 3) - the modern PostgreSQL adapter recommended for production
2. **Connection String**: Uses `DATABASE_URL` environment variable instead of local file
3. **Auto-increment**: Uses `SERIAL` instead of `AUTOINCREMENT`
4. **Placeholders**: Uses `%s` instead of `?` in queries
5. **Better Performance**: PostgreSQL offers better concurrent access and scalability
6. **Hosting Ready**: Compatible with Render, Heroku, Railway, and other cloud platforms

## Troubleshooting

### Error: "DATABASE_URL environment variable is not set"

**Solution**: Create a PostgreSQL database in Replit as described in Step 1 above.

### Error: Connection refused or timeout

**Solution**: Check that your Replit database is running. Go to Tools → Database to verify status.

### Tables not created

**Solution**: The app automatically creates tables on startup. Check the logs for any errors during initialization.

## Migration from SQLite (if needed)

If you have existing data in SQLite (`ecocycle.db`), you'll need to manually export and import:

1. Export data from SQLite tables
2. Import into PostgreSQL using INSERT statements
3. Note: Sequence values may need adjustment for SERIAL columns

## University of Ibadan Location

The map is now centered on University of Ibadan coordinates:
- **Latitude**: 7.3912° N
- **Longitude**: 3.9167° E

## Photo Upload Enhancement

Waste logging now accepts photo uploads without requiring barcode/QR code scans. Users can simply upload a photo of their waste for admin approval.
