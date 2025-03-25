# Personal Expense Tracker
A simple Personal Expense Tracker web application built with Django.

User can:
1.Register and log in.
2.Add and view their daily expenses.
3.See a summary of their total expenses.

Implemented authentication, CRUD operations, and use basic form handling with Django.
Users can export expenses to a Excel file.


## Setup Instructions
**1. Clone the Repository**

    git clone https://github.com/Amal-Krishnanps/expense_tracker.gitgit add README.md
    
    cd expense_tracker

**2. Create a Virtual Environment**
   
     python -m venv venv
   
 **3. Activate the Virtual Environment**
 
      On Windows:
      venv\Scripts\activate
     
      On macOS/Linux:
      source venv/bin/activate
   
**4. Install Dependencies**

      pip install -r requirements.txt

**5. Apply Migrations**

     python manage.py migrate
     
**6. Run the Development Server:

     python manage.py runserver

Visit http://127.0.0.1:8000/ to access the app



