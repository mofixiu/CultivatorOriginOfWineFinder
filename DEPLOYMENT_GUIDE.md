# 🚀 Deployment Guide - Wine Cultivar Prediction System

## ⚠️ Important Platform Notes

### Render.com (RECOMMENDED for Streamlit)
✅ **Best choice** - Native support for Python web services  
✅ Easy deployment with automatic builds  
✅ Free tier available  

### Vercel
⚠️ **Not recommended** - Vercel is optimized for frontend/serverless functions  
⚠️ Streamlit requires a persistent server which Vercel doesn't support natively  
💡 **Alternative**: Use Streamlit Cloud or Render instead

---

## 📋 OPTION 1: Deploy to Render.com (RECOMMENDED)

### Step-by-Step Instructions:

1. **Prepare Your Repository**
   - Push all project files to GitHub
   - Ensure `wine_cultivar_model.pkl` is in the `model/` folder
   - Verify all files are committed

2. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub (recommended for easy integration)

3. **Create New Web Service**
   - Click **"New +"** button
   - Select **"Web Service"**
   - Connect your GitHub repository

4. **Configure Web Service**
   ```
   Name: wine-cultivar-predictor
   Region: Choose closest to you
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
   ```

5. **Advanced Settings (Optional)**
   ```
   Instance Type: Free (or upgrade as needed)
   Auto-Deploy: Yes (recommended)
   Health Check Path: /
   ```

6. **Deploy**
   - Click **"Create Web Service"**
   - Wait 2-5 minutes for deployment
   - Render will show build logs
   - Once complete, you'll get a URL like: `https://wine-cultivar-predictor.onrender.com`

7. **Test Your Application**
   - Click the generated URL
   - Test with sample data
   - Verify predictions work correctly

---

## 📋 OPTION 2: Deploy to Streamlit Cloud (Alternative)

### Step-by-Step Instructions:

1. **Prepare Repository**
   - Push to GitHub
   - Public or private repository (both work)

2. **Deploy to Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click **"New app"**

3. **Configure App**
   ```
   Repository: your-username/WineCultivar_Project
   Branch: main
   Main file path: app.py
   ```

4. **Deploy**
   - Click **"Deploy!"**
   - Wait for deployment
   - Get URL: `https://your-app.streamlit.app`

---

## 📋 OPTION 3: Deploy to PythonAnywhere

### Step-by-Step Instructions:

1. **Create Account**
   - Go to https://www.pythonanywhere.com
   - Sign up for free account

2. **Upload Files**
   - Go to **"Files"** tab
   - Create folder: `WineCultivar_Project`
   - Upload all project files

3. **Create Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 wine-env
   workon wine-env
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to **"Web"** tab
   - Click **"Add a new web app"**
   - Choose Manual configuration
   - Python 3.10

5. **Setup WSGI**
   - Edit WSGI configuration file
   - Add Streamlit configuration

6. **Reload and Test**
   - Click **"Reload"**
   - Visit your URL: `username.pythonanywhere.com`

---

## 🔧 Required Files Checklist

Ensure these files are in your repository:

- ✅ `app.py` - Main application file
- ✅ `requirements.txt` - Python dependencies
- ✅ `model/wine_cultivar_model.pkl` - Trained model
- ✅ `Procfile` - Process configuration (for Render)
- ✅ `runtime.txt` - Python version (optional)
- ✅ `setup.sh` - Streamlit setup script (optional)
- ✅ `.streamlit/config.toml` - Streamlit configuration

---

## 🐛 Common Issues & Solutions

### Issue 1: Model File Not Found
**Error**: `FileNotFoundError: model/wine_cultivar_model.pkl`

**Solution**:
- Ensure model file is in the `model/` folder
- Check file name matches exactly: `wine_cultivar_model.pkl`
- Verify file is committed to Git (check .gitignore)

### Issue 2: Port Binding Error (Render)
**Error**: `Port binding failed`

**Solution**:
- Use: `--server.port=$PORT` in start command
- Render automatically assigns the PORT variable

### Issue 3: Dependencies Not Installing
**Error**: `ModuleNotFoundError`

**Solution**:
- Check `requirements.txt` has all dependencies
- Use specific version numbers (already done)
- Try: `pip install --upgrade pip` before requirements

### Issue 4: Application Crashes on Startup
**Error**: Various startup errors

**Solution**:
- Check build logs in Render dashboard
- Verify Python version compatibility
- Test locally first: `streamlit run app.py`

### Issue 5: Large Model File
**Error**: `File too large for GitHub`

**Solution**:
- Use Git LFS for files > 100MB
- Or host model file separately and download on startup
- Model should be ~100KB (not an issue for this project)

---

## 📊 Post-Deployment Testing

After deployment, test with these samples:

### Test Case 1 - Expected: Cultivar 0
```
Alcohol: 13.2
Malic Acid: 2.5
Total Phenols: 2.8
Flavanoids: 2.9
Color Intensity: 5.6
Proline: 1065
```

### Test Case 2 - Expected: Cultivar 1
```
Alcohol: 12.5
Malic Acid: 3.4
Total Phenols: 2.0
Flavanoids: 1.5
Color Intensity: 4.8
Proline: 625
```

### Test Case 3 - Expected: Cultivar 2
```
Alcohol: 13.8
Malic Acid: 1.8
Total Phenols: 2.6
Flavanoids: 2.2
Color Intensity: 7.5
Proline: 985
```

---

## 📝 Submission Information

After deployment, update `WineCultivar_hosted_webGUI_link.txt` with:

```
Name: [Your Full Name]
Matric Number: [Your Matric Number]
Machine Learning Algorithm Used: Random Forest Classifier
Model Persistence Method Used: Joblib
Live URL: [Your Render/Streamlit URL]
GitHub Repository: [Your GitHub repo URL]
```

---

## 💡 Pro Tips

1. **Free Tier Limitations**
   - Render free tier: App sleeps after inactivity, cold starts ~30s
   - Streamlit Cloud: 1GB RAM limit
   - PythonAnywhere: Limited CPU seconds

2. **Keep App Alive**
   - Use UptimeRobot or similar service
   - Ping your URL every 15 minutes

3. **Custom Domain** (Optional)
   - Render: Supports custom domains on paid plans
   - Streamlit: Custom domains available

4. **Environment Variables**
   - Store sensitive data in environment variables
   - Configure in platform dashboard

5. **Monitoring**
   - Check logs regularly for errors
   - Set up email notifications for downtime

---

## 📞 Support Resources

- **Render Documentation**: https://render.com/docs
- **Streamlit Cloud Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **GitHub Issues**: Create issue in your repository

---

**Last Updated**: January 21, 2026  
**Project**: Wine Cultivar Origin Prediction System  
**Course**: CSC415
