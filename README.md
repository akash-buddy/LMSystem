
# 📚 Library Management System using Django

## A web-based system for librarians to manage books, members, issuing and returning of books.


## 📖 Project Description

The **Library Management System using Django** is a full-featured web application designed to help librarians efficiently manage books and members in a library. Built using the Django web framework, it allows administrators to perform core library tasks such as adding and updating books, registering members, issuing and returning books, and tracking rent fees and member debts.

This system streamlines library operations by integrating a rent calculation mechanism, ensuring that members who borrow books are charged based on the number of days the book is issued. It also enforces a debt limit, automatically preventing members from borrowing further if their outstanding dues exceed ₹500. Additionally, the application can fetch and import book data directly from an external API (Frappe Library API), making it easier to populate the system with valid book entries without manual input.

The app provides a clean and intuitive interface for managing day-to-day tasks and includes a search function for quickly locating books by title or author. It also includes an admin panel for backend data management. This project is ideal for small to mid-sized libraries and serves as a practical demonstration of Django’s power for building real-world web applications.

---

## 🔍 Key Features

- **Book Management (CRUD)**: Add, edit, update, and delete books with fields like title, author, ISBN, publisher, and stock count.
![Alt text](https://github.com/akash-buddy/LMSystem/blob/4ae4f70cbb1c512ee967322acd5028e34bcf1ddc/readme_image/book_view.png)
- **Member Management (CRUD)**: Add and manage library members with details like name, email, phone, and debt.
![Alt text](https://github.com/akash-buddy/LMSystem/blob/34258b15e09cfc89a838c0d3cc53b72109bfebee/readme_image/member.png)
- **Issue and Return Books**:
  - Issues books to members.
  - Calculates rent fee based on number of days borrowed (₹10/day).
  - Updates book stock accordingly.
![Alt text](https://github.com/akash-buddy/LMSystem/blob/b13e8ddd9d065781ce6d2c388145166e45ced765/readme_image/issue_book.png)
- **Debt Handling**:
  - Automatically adds rent to the member’s debt upon return.
  - Blocks issuing if debt exceeds ₹500.
- **Search Functionality**: Quickly find books using keywords from the title or author's name.
- **Book Import via API**:
  - Fetches book data from Frappe Library API
  - Imports multiple books with pre-filled information like book-id, title, author, ISBN, etc.
![Alt text](https://github.com/akash-buddy/LMSystem/blob/d794131421218e55327b4c1fbc0969f721218837/readme_image/import_book.png)
- **Admin Interface**: Manage all models (books, members, transactions) via Django's built-in admin panel.
- **User-Friendly Interface**: Clean and organized templates for easy use by library staff.

---
## 🧱 Tech Stack

- Backend: Django (Python)
- Frontend: Django Templates (HTML)
- Database: SQLite
- API Integration: Frappe Library API


## 📌 Ideal Use Cases

-  School or college libraries
-  Small to mid-size public libraries
-  Academic Django project for learning CRUD, views, forms, and API integration
-  Portfolio project for demonstrating Django skills

---

## ⚙️ Installation Instructions

Follow the steps below to set up and run the **Library Management System using Django** on your local machine:


####  1. Clone the Repository
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

#### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Install Dependencies
`pip install -r requirements.txt`



#### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```



#### 5. Run the Development Server
`python manage.py runserver`


---

##  Deploying to Render

You can easily deploy this Django Library Management System to [Render](https://render.com) — a free platform for hosting web apps.


#### 1. Push Your Code to GitHub

Make sure your project is in a GitHub repository:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/library-management-system.git
git push -u origin main

```
#### 2. Prepare for Deployment
Make sure you have the following files in your project root:
requirements.txt
```bash
pip freeze > requirements.txt
```
#### 3. Configure settings.py for Production
- Set ALLOWED_HOSTS:
```bash
ALLOWED_HOSTS = ['your-app-name.onrender.com']
```
- Add static file configuration at the bottom:
```bash
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

### Create a Render Account and New Web Service

1. Go to [https://dashboard.render.com](https://dashboard.render.com)

2. Click on New > Web Service+-

3. Connect your GitHub repository that contains the Django project.

4. Fill out the deployment form:

   - **Build Command**  
     ```
     pip install -r requirements.txt
     ```

   - **Start Command**  
     ```
     gunicorn LMSystem.wsgi
     ```

5. Set the following Environment Variables:

   | Key                    | Value                    |
   |------------------------|--------------------------|
   | DJANGO_SETTINGS_MODULE | LMSystem.settings        |
   | SECRET_KEY             | your_django_secret_key   |
   | DEBUG                  | False                    |

6. Go to your service --> **Shell** --> **Run**

7. Your Library Management System is now live on Render 👉 https://lm-system.onrender.com/



---


## Bug Reporting

If any librarian encounters a bug in the Library Management System, please report it by sending an email with details to:

📧 **Email:** [akashsp707@gmail.com](mailto:akashsp707@gmail.com)

Please include the following information in your report:

- A clear description of the issue    
- Screenshot  
- Your browser information  

We appreciate your feedback to help improve the system!

