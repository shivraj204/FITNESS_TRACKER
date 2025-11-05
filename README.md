A full-stack web application built with Django to help users track their fitness activities, including workouts, daily logs (steps, calories, hydration), goal setting, and progress visualization. Features secure user authentication, personalized dashboards, interactive charts, and email reminders.

Features
User Authentication: Secure login and registration system with personalized dashboards.
Workout Logging: Log activities, duration, and calories burned.
Daily Health Logs: Track steps, calories consumed, and water intake.
Goal Tracking: Set and monitor daily goals for calories, steps, and hydration.
Progress Charts: Visualize fitness data with interactive charts using Chart.js.
Email Reminders: Automated SMTP-based notifications for missed activities or goals.
Responsive Design: Built with HTML, CSS (Bootstrap), and JavaScript for a mobile-friendly interface.
Tech Stack
Backend: Django (Python)
Database: MySQL (or SQLite for local development)
Frontend: HTML, CSS (Bootstrap), JavaScript
Charts: Chart.js
Email: SMTP integration via Django
Other: Python libraries for data handling
Installation and Setup
Follow these steps to set up the project locally.

Prerequisites
Python 3.8 or higher
MySQL (or use SQLite as a fallback)
Git
A code editor (e.g., VS Code)
Step 1: Clone the Repository
bash

Copy code
git clone https://github.com/your-username/fitness-tracker.git
cd fitness-tracker
Step 2: Create a Virtual Environment
bash

Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
bash

Copy code
pip install -r requirements.txt
If requirements.txt doesn't exist, install manually:

bash

Copy code
pip install django mysqlclient
Step 4: Configure the Database
For MySQL: Create a database named fitness_tracker_db and update fitness_tracker/settings.py with your credentials.
For SQLite: Change the database engine in settings.py to 'django.db.backends.sqlite3' and set 'NAME': BASE_DIR / 'db.sqlite3'.
Step 5: Run Migrations
bash

Copy code
python manage.py makemigrations
python manage.py migrate
Step 6: Create a Superuser
bash

Copy code
python manage.py createsuperuser
Follow the prompts to set up an admin account.

Step 7: Configure Email (SMTP)
Update fitness_tracker/settings.py with your SMTP details (e.g., Gmail):

python
7 lines
Copy code
Download code
Click to expand
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
...
Step 8: Run the Development Server
bash

Copy code
python manage.py runserver
