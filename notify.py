import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def protocol(smtp_server, port, sender_email, sender_password, email, msg):
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Habilita a criptografia TLS
        server.login(sender_email, sender_password)  # Faz login no servidor
        server.sendmail(sender_email, email, msg.as_string())  # Envia o email
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

def send_email(email, subject, message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "tasknicomanager@gmail.com"
    sender_password = "mqiw kvae qief oyex"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "html"))

    with open("logo1.png", "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header("Content-ID", "<logo>")
        msg.attach(img)

    protocol(smtp_server, port, sender_email, sender_password, email, msg)

def registration_email(email, Name, Surname):
    subject = "TaskNico Registration"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Hello {Name} {Surname}! Welcome to TaskNico!</p>
            <p>Your registration was successful!</p>
            <p>Now you can start using the app.</p>
            <p>Enjoy!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def login_email(email, Name, Surname):
    subject = "Your account was accessed"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Welcome back {Name} {Surname}!</p>
            <p>Your account has just been logged into our system!</p>
            <p>Now you can manage and see your tasks and project.</p>
            <p>Enjoy!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def logout_email(email, Name, Surname):
    subject = "Your account was logged out"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Goodbye {Name} {Surname}! :( </p>
            <p>Your account has just been logged out!</p>
            <p>Now you can't manage your tasks and projects until you log in again.</p>
            <p>We hope to see you soon!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def delete_email(email, Name, Surname):
    subject = "Your account was deleted"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Goodbye {Name} {Surname}! :( </p>
            <p>Your account has just been deleted...</p>
            <p>We hope to see you soon!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def task_created_email(email, Name, Surname, task_name):
    subject = "TaskNico - New Task Created"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Hello {Name} {Surname}!</p>
            <p>A new task has been created: <strong>{task_name}</strong>.</p>
            <p>You are assigned to this task.</p>
            <p>Thank you for using TaskNico!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def task_deleted_email(email, Name, Surname, task_name):
    subject = "TaskNico - Task Deleted"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Hello {Name} {Surname}!</p>
            <p>The task <strong>{task_name}</strong> has been deleted.</p>
            <p>You are no longer assigned to this task.</p>
            <p>Thank you for using TaskNico!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def project_created_email(email, Name, Surname, project_name):
    subject = "TaskNico - New Project Created"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Hello {Name} {Surname}!</p>
            <p>A new project has been created: <strong>{project_name}</strong>.</p>
            <p>You are part of this project.</p>
            <p>Thank you for using TaskNico!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

def project_deleted_email(email, Name, Surname, project_name):
    subject = "TaskNico - Project Deleted"
    message = f"""
    <html>
        <body>
            <h1>TaskNico</h1>
            <p>Hello {Name} {Surname}!</p>
            <p>The project <strong>{project_name}</strong> has been deleted.</p>
            <p>You are no longer part of this project.</p>
            <p>Thank you for using TaskNico!</p>
            <img src="cid:logo" alt="TaskNico Logo" style="width: 200px; height: auto;">
        </body>
    </html>
    """
    send_email(email, subject, message)

    