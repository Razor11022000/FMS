# Django FMS (beta)
This is a Simple Fee Management System (FMS) Developed for Educational Purpose using Python (Django).
Feel free to make changes based on your requirements.

And if you like this project then ADD a STAR ⭐️  to this project 👆

## Features of this Project

### A. Admin Users Can
1. See Overall Summary Charts of Students details, Staffs details etc
2. Can issue TC to eligible students.
3. Manage Staffs (Add, Update and Delete)
4. Manage Payments (Add, Update and Delete)
5. Can edit Fee structure and manipulate payment details.

### B. Staff/Teachers Can
1. See the Overall Summary Charts related to their students
2. Add/Update Students personal details.
3. 3. Manage Payments (Add, Update and Delete)
4. They also have access to recent payments.

### C. Students Can
1. See the Overall Summary Charts related to their fee payment status. 
2. View their respective profiles
3. Edit limited personal info

## Support Developer
1. Add a Star 🌟  to this 👆 Repository


## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/Razor11022000/FMS.git
```

Then, Enter the project
```
$  cd FMS
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User 
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

## For Sponsor or Projects Enquiry
1. Email - mithungfeb2@gmail.com
2. LinkedIn - https://www.linkedin.com/in/mithun-g
