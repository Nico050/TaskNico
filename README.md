# TaskNico - Task and Project Manager

TaskNico is a task and project management system designed to help users efficiently organize their activities. The system allows the creation of one-time and recurring tasks, project management with multiple tasks and collaborators, and an email notification system to keep users informed about their activities.

## 🚀 Main Features

- **Task Creation and Management**:
  - Tasks can be **one-time** or **recurring**.
  - Priority assignment (`Low`, `Medium`, `High`).
  - Status tracking (`On_going`, `Completed`, etc.).
  - Ability to add collaborators to tasks.

- **Project Management**:
  - Each project can contain multiple tasks.
  - Assign a manager and multiple collaborators.
  - Tasks are automatically associated with participants.

- **Email Notifications**:
  - Automatic emails are sent to collaborators and managers when tasks or projects are created or deleted.
  - Login, logout, registration, and account deletion confirmations.

- **User Authentication and Account Management**:
  - User registration with email verification.
  - Modify and delete accounts, including removing associated data.

- **Local Database Storage**:
  - Stores user, task, and project information in CSV files.
  - Each user has a personal task database (`UsernameT.csv`) and project database (`UsernameP.csv`).

---

## 🏗 Code Structure

### 1️⃣ Classes and Their Functionality

#### 📌 `Conta` Class (account.py)
Responsible for user account management, including:
✅ User registration and login.
✅ Account modification and deletion.
✅ Stores user data in `users.csv`.
✅ Password encapsulation and hashing with `hash_password()`.

#### 📌 `Task` Class and Subclasses (tasks.py)
Handles task creation and deletion.
- `O_Tasks`: Creates one-time tasks.
- `R_Tasks`: Creates recurring tasks.
- Tasks are stored in `UsernameT.csv` and notify collaborators via email.

#### 📌 `Project` Class (projects.py)
Manages project creation and deletion.
- Each project can contain multiple tasks and collaborators.
- Data is stored in the `UsernameP.csv` file.

---

### 2️⃣ Main Files and Modules

#### 📧 notify.py - Notification System
Handles automatic email notifications.
- Notifies users about task and project creation/deletion.
- Sends confirmations for login, logout, registration, and account deletion.

#### 🖥 first_screen.py - Login/Register Screen
Manages user access:
- Displays login and registration options.
- Verifies credentials before granting access.

#### 📊 seccond_screen.py - Main Menu
Provides options after login:
- Create/delete tasks.
- Create/delete projects.
- Manage user account.
- Logout or exit the program.

---

## 📂 Local Database Storage Method

TaskNico uses **CSV files as a local database** to store system information. Each user has their own set of files:
- **`users.csv`**: Contains data of all registered users.
- **`UsernameT.csv`**: Stores the user's tasks.
- **`UsernameP.csv`**: Stores the user's projects.

### 📌 How Does Storage Work?
✅ When a user creates a task or project, the data is added to their respective CSV file.
✅ When an account is deleted, the user's `UsernameT.csv` and `UsernameP.csv` files are removed.
✅ Operations use `pandas` to efficiently handle data manipulation.

---

## 🔧 How to Run TaskNico

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/TaskNico.git
   cd TaskNico
   ```
2. **Install dependencies**
   ```bash
   pip install pandas smtplib
   ```
3. **Run the program**
   ```bash
   python main.py
   ```

---

## 📬 Conclusion

TaskNico is a robust system for managing tasks and projects, ensuring organization and efficient communication among team members. With local CSV-based storage, the program provides a lightweight and practical solution for task tracking.

## Funcionalyties

Task Creation and Assignment: Implemented
Deadline and Priority Setting: implemented
Progress Tracking and Updates: Not implemented, 
because I couldn't create a function that when the deadline arrives can tell if it was completed
Collaboration and Communication Tools: Not implemented, becouse needs a cloud data bank, to remote acess
File Sharing and Management: Not implemented, i don't know how to upload a file on code
Calendar Integration: Not implemented, i don't have the knolege of a library that do that
Customizable Workflow: implemented
Notifications and Alerts: implemented
Reporting and Analytics: Not implemented
Access Control and Permissions: Not implemented
