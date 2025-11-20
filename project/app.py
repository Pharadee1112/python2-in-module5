from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# --------- Decorator ----------
def log_route(func):
    def wrapper(*args, **kwargs):
        print(f"Route called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# --------- OOP Email Service ----------
class EmailService:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password

    def send(self, to, message):
        msg = MIMEText(message)
        msg["Subject"] = "Library Notification"
        msg["From"] = self.sender
        msg["To"] = to

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender, self.password)
                server.sendmail(self.sender, to, msg.as_string())
        except Exception as e:
            print("Email error:", e)

# ใช้ email object
email_service = EmailService("YOUR_EMAIL@gmail.com", "YOUR_PASSWORD")

# --------- Flask Routes ----------
@app.route("/")
def index():
    return render_template("form.html")

@app.route("/send-email", methods=["POST"])
@log_route
def send_email():
    name = request.form["name"]
    borrow_date = request.form["borrow_date"]
    user_email = request.form["email"]

    # บันทึกลงไฟล์
    with open("borrow_log.txt", "a") as f:
        f.write(f"{name} borrowed on {borrow_date}\n")

    # ส่งอีเมล
    message = f"Hello {name},\nYour borrow date: {borrow_date}"
    email_service.send(user_email, message)

    return f"Email sent to {user_email}!"
