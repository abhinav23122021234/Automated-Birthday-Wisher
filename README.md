
# 🎉 Automated Birthday Wisher  

This Python script automatically checks for birthdays every day and sends personalized email wishes to the respective individuals. It is designed to run daily on the cloud using **PythonAnywhere** or any other cloud-based scheduler.  

## 🚀 Features  
✅ Reads a list of birthdays from `birthdays.csv`  
✅ Picks a random birthday wish from predefined templates  
✅ Sends an email automatically on the person's birthday  
✅ Can be scheduled to run daily using a cloud service  

## 📂 Project Structure  
```
/Automated-Birthday-Wisher
│── main.py                 # Main script to check birthdays and send emails
│── birthdays.csv           # CSV file storing names, emails, and birthdates
│── letter_templates/       # Folder containing birthday message templates
│   ├── letter_1.txt  
│   ├── letter_2.txt  
│   ├── letter_3.txt  
```

## 🛠️ Setup Instructions  

### 1️⃣ Prerequisites  
- Python 3.x installed  
- A Gmail account with **App Passwords** enabled (for secure email sending)  
- A cloud service like **PythonAnywhere** to schedule the script  

### 2️⃣ Install Dependencies  
Run the following command to install required libraries:  
```bash
pip install pandas smtplib
```

### 3️⃣ Configure Email Credentials  
In `main.py`, replace the following placeholders with your actual Gmail credentials:  
```python
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"
```
⚠️ **Do not use your regular Gmail password!** Create an **App Password** from [Google App Passwords](https://myaccount.google.com/apppasswords).  

### 4️⃣ Add Birthdays to `birthdays.csv`  
Ensure `birthdays.csv` contains at least the following columns:  
```csv
name,email,year,month,day
John Doe,johndoe@example.com,1995,3,15
Jane Smith,janesmith@example.com,2000,7,22
```
New birthdays can also be added via the script using the `add_person` function.  

### 5️⃣ Set Up a Daily Scheduler (PythonAnywhere)  
1. Upload your project files to **PythonAnywhere**.  
2. Go to the **Tasks** section and schedule `main.py` to run daily.  
3. Ensure your Gmail credentials are correctly set.  

## 🎯 How It Works  
1. The script checks the current date and matches it with birthdays in `birthdays.csv`.  
2. If a match is found, a random letter from `letter_templates/` is chosen.  
3. The `[NAME]` placeholder in the letter is replaced with the person's actual name.  
4. The email is sent using **SMTP (Simple Mail Transfer Protocol)**.  

## ⚡ Example Email Sent  
**Subject:** Happy Birthday! 🎉  
```
Dear John,  

Wishing you a fantastic birthday filled with love and happiness!  
Enjoy your special day.  

Best regards,  
Your Friend  
```

## 🛠️ Troubleshooting  
🔹 **UnicodeEncodeError** → Add `encoding="utf-8"` while opening files.  
🔹 **FileNotFoundError** → Ensure `birthdays.csv` exists or is initialized as an empty file.  
🔹 **SMTP Authentication Error** → Enable **App Passwords** in Gmail settings.  
