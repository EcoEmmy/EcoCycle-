# Deploying EcoCycle to Render

This guide will help you deploy the EcoCycle application to Render's hosting platform.

## Prerequisites

- GitHub account
- Render account (free tier available at https://render.com)
- The EcoCycle project files

## Step 1: Prepare Your Repository

1. Push your EcoCycle code to a GitHub repository
2. Ensure all files from the zip are included
3. Make sure `.gitignore` is properly configured to exclude:
   - `__pycache__/`
   - `.pythonlibs/`
   - `*.pyc`
   - `.env` (if you have local environment variables)

## Step 2: Create PostgreSQL Database on Render

1. Go to https://dashboard.render.com
2. Click **New +** → **PostgreSQL**
3. Fill in the details:
   - **Name**: `ecocycle-db`
   - **Database**: `ecocycle`
   - **User**: (auto-generated)
   - **Region**: Choose closest to your users
   - **Plan**: Free tier is sufficient to start
4. Click **Create Database**
5. Wait for the database to be created
6. Copy the **Internal Database URL** (you'll need this later)

## Step 3: Create Web Service on Render

1. Go to https://dashboard.render.com
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `ecocycle`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free tier or paid plan

## Step 4: Configure Environment Variables

In the **Environment** section, add these variables:

| Key | Value | Notes |
|-----|-------|-------|
| `DATABASE_URL` | (Paste the Internal Database URL from Step 2) | Required |
| `SESSION_SECRET` | (Generate a random string) | Optional but recommended |
| `PYTHON_VERSION` | `3.11.0` | Ensures correct Python version |

To generate a secure SESSION_SECRET, you can use:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## Step 5: Deploy

1. Click **Create Web Service**
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Start your application with Gunicorn
3. Wait for the deployment to complete (usually 2-5 minutes)

## Step 6: Initialize Database

After the first deployment:

1. Go to your service page on Render
2. Click on **Shell** tab
3. Run the database initialization:
   ```bash
   python create_admin.py
   ```
4. Note the admin credentials:
   - Username: `admin`
   - Password: `admin123` (change immediately!)

## Step 7: Access Your Application

1. Click on the URL at the top of your service page (e.g., `https://ecocycle.onrender.com`)
2. Your application should now be live!
3. Log in with the admin credentials and change the password immediately

## Important Notes

### Database Connections
- The application uses `psycopg` (version 3) which is optimized for production use
- Connection pooling is handled automatically
- DATABASE_URL format: `postgresql://user:password@host:port/database`

### Free Tier Limitations
- Web service spins down after 15 minutes of inactivity
- Database has storage limits (check Render's free tier details)
- First request after spin-down may take 30+ seconds

### Upgrading to Paid Plan
For production use, consider:
- **Starter Plan**: Always-on service, no spin-down
- **Standard Plan**: Better performance and resources
- **PostgreSQL Paid**: Larger storage, automated backups

## Troubleshooting

### Build Fails
- Check that `requirements.txt` is in the root directory
- Verify Python version compatibility
- Check build logs for specific error messages

### Application Won't Start
- Verify `DATABASE_URL` is set correctly
- Check that port binding is correct (Render uses `$PORT` env variable)
- Review application logs for errors

### Database Connection Errors
- Ensure DATABASE_URL uses the Internal URL, not External
- Verify database is running
- Check firewall/network settings

### Photo Uploads Not Working
- Ensure upload directories exist (Render's ephemeral filesystem)
- Consider using cloud storage (AWS S3, Cloudinary) for production

## Post-Deployment Tasks

1. **Change Admin Password**: Log in and update the default password
2. **Add Collection Booths**: Configure booth locations for University of Ibadan
3. **Add Rewards**: Set up the rewards catalog
4. **Test Features**: Verify waste logging, photo uploads, and point system
5. **Configure Backups**: Set up database backup schedule on Render

## Monitoring

- Use Render's built-in monitoring dashboard
- Check application logs regularly
- Monitor database usage and performance
- Set up alerts for downtime

## Support

- Render Documentation: https://render.com/docs
- EcoCycle Issues: Create an issue in your GitHub repository
- Community: Render Community Forum

## Security Checklist

- ✅ Change default admin password
- ✅ Use strong SESSION_SECRET
- ✅ Enable HTTPS (automatic on Render)
- ✅ Keep dependencies updated
- ✅ Monitor access logs
- ✅ Regular database backups

Your EcoCycle application is now deployed and ready to help manage waste at University of Ibadan!
