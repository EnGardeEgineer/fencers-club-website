# Fencers Club Website

A beautiful, modern website for the Fencers Club - Est. 1883. Built with Django and featuring information about programs, coaches, membership, and more.

## 🚀 Quick Start Guide

Follow these simple steps to get the website running on your computer:

### Step 1: Download the Code
1. Click the green "Code" button above
2. Select "Download ZIP"
3. Extract the ZIP file to your Desktop
4. Open the extracted folder

### Step 2: Install Python (if you don't have it)
1. Go to https://python.org/downloads/
2. Download Python 3.8 or newer
3. Run the installer and **check "Add Python to PATH"**
4. Restart your computer after installation

### Step 3: Open Command Line
**Windows:**
- Press `Windows Key + R`
- Type `cmd` and press Enter

**Mac:**
- Press `Cmd + Space`
- Type `Terminal` and press Enter

### Step 4: Navigate to the Project
```bash
cd Desktop/fencers-club-website-main
```
(Replace with the actual folder name if different)

### Step 5: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 6: Run the Website
```bash
python manage.py runserver
```

### Step 7: Open in Browser
1. Open your web browser
2. Go to: http://127.0.0.1:8000/
3. Enjoy exploring the Fencers Club website! 🎉

## 🌐 Share on Your WiFi Network

To let others on your WiFi access the site:

1. **Find your IP address:**
   - Windows: Run `ipconfig` and look for "IPv4 Address"
   - Mac: Run `ifconfig` and look for "inet"

2. **Start server with your IP:**
   ```bash
   python manage.py runserver YOUR_IP_ADDRESS:8000
   ```
   Example: `python manage.py runserver 192.168.1.105:8000`

3. **Share the link:**
   - Give others: `http://YOUR_IP_ADDRESS:8000/`
   - Example: `http://192.168.1.105:8000/`

## 📱 Website Pages

- **Home:** Main landing page with hero section
- **About:** Club history and mission since 1883
- **Programs:** Youth and adult fencing programs
- **Coaches:** Meet our expert coaching staff
- **Membership:** Join the club - pricing and benefits
- **Contact:** Get in touch and visit our facility
- **News:** Latest updates and announcements

## 🛠️ Technical Details

- **Framework:** Django 5.0.2
- **Styling:** Tailwind CSS
- **Database:** SQLite (included)
- **Python Version:** 3.8+

## 🎨 Features

- ✨ Modern, responsive design
- 📱 Mobile-friendly layout
- 🏛️ Rich history and tradition
- 👥 Coach profiles and programs
- 💰 Clear membership pricing
- 📞 Easy contact information
- 🏆 Championship achievements

## 🚨 Troubleshooting

**"Command not found" errors:**
- Make sure Python is installed and added to PATH
- Restart your command line/terminal

**"Module not found" errors:**
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct folder

**Website won't load:**
- Check that the server is running (you should see "Starting development server...")
- Make sure you're using the correct URL: http://127.0.0.1:8000/

**Need help?**
- Contact Sarah at sarah.ellis@my.liu.edu

---

**Built with ❤️ for the Fencers Club community** 