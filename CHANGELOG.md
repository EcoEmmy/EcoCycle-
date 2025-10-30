# EcoCycle - Changelog

## Latest Update - October 30, 2025

### Major Features & Enhancements

#### 1. Hall of Residence Dropdown ✅
- **Changed**: Residence field from text input to dropdown menu
- **Added**: 12 University of Ibadan halls including:
  - Abdulsalami Hall
  - Queen Elizabeth II Hall
  - Obafemi Awolowo Hall
  - Tedder Hall
  - Sultan Bello Hall
  - Independence Hall
  - Kuti Hall
  - Queen Idia Hall
  - Mellanby Hall
  - Nnamdi Azikiwe Hall
  - Off-Campus
  - Other
- **Benefit**: Standardized data entry and better analytics

#### 2. Miscellaneous Waste Category ✅
- **Added**: New "Miscellaneous" waste type with 🗑️ icon
- **Purpose**: Allows users to log waste that doesn't fit standard categories
- **Location**: Available in Waste Logs page alongside other waste types

#### 3. Photo Upload Enhancement ✅
- **Changed**: Waste logging no longer requires barcode/QR code
- **Feature**: Users can now upload photos of waste directly
- **Benefit**: More accessible waste logging process
- **Note**: Submissions still require admin approval

#### 4. University of Ibadan Map Integration ✅
- **Updated**: Map coordinates to University of Ibadan
  - Latitude: 7.3912°N
  - Longitude: 3.9167°E
- **Map Provider**: Leaflet with OpenStreetMap tiles
- **Zoom Level**: Optimized for campus view (zoom level 15)

#### 5. PostgreSQL Migration ✅
- **Migrated**: From SQLite to PostgreSQL
- **Library**: Using psycopg 3.2.12 (modern, production-ready)
- **Compatibility**: Render, Heroku, Railway, and other cloud platforms
- **Benefits**:
  - Better concurrent access
  - Improved performance
  - Automatic backups (with hosting provider)
  - Scalability for growth

### Database Schema Updates
- Changed `INTEGER PRIMARY KEY AUTOINCREMENT` to `SERIAL PRIMARY KEY`
- Updated all query placeholders from `?` to `%s`
- Added proper foreign key constraints
- Optimized table structures for PostgreSQL

### Infrastructure Changes
- **Dependencies Updated**:
  - psycopg[binary]==3.2.12 (PostgreSQL adapter)
  - python-dotenv==1.2.1 (environment variables)
  - All Flask dependencies updated to latest stable versions
  
- **New Files**:
  - `DATABASE_SETUP.md` - PostgreSQL setup guide
  - `RENDER_DEPLOYMENT.md` - Render deployment instructions
  - `CHANGELOG.md` - This file

### Configuration
- `DATABASE_URL` environment variable required
- Compatible with Replit's PostgreSQL integration
- Production-ready with Gunicorn

### Bug Fixes
- Fixed cache control headers for immediate updates
- Improved error handling for database connections
- Enhanced validation for file uploads

### Developer Notes
- Old SQLite database (`ecocycle.db`) removed
- All queries converted to cursor-based pattern
- Added dict_row factory for better data handling
- Code organized for maintainability

## Previous Updates

### Initial Replit Setup - October 30, 2025
- Configured for Replit environment
- Set up Flask workflow on port 5000
- Added .gitignore for Python projects
- Initial database structure created

---

## Deployment Notes

### For Replit:
1. Create PostgreSQL database in Tools → Database
2. Database tables auto-initialize on first run
3. Run `python create_admin.py` to create admin account

### For Render:
See `RENDER_DEPLOYMENT.md` for complete deployment instructions

---

## Support & Documentation

- Setup Guide: `DATABASE_SETUP.md`
- Deployment Guide: `RENDER_DEPLOYMENT.md`
- Project Info: `replit.md`

---

**Version**: 2.0.0  
**Last Updated**: October 30, 2025  
**Status**: Production Ready 🚀
