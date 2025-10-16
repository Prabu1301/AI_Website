from flask import Flask, render_template, request, redirect, url_for, session
import yagmail

app = Flask(__name__)
app.secret_key = "supersecret"

CLICK_COUNT = 0
COMMENT_LIST = []

EMAIL_RECEIVER = "gideonprabu@gmail.com"
GMAIL_USER = "prabu.notifications@gmail.com"
GMAIL_APP_PASSWORD = "YOUR-GMAIL-APP-PASSWORD"  # <-- Replace with your Google App Password

PASSWORDS = {"kcwo mvdn cpcj ynkb"}

def send_comment_alert(name, comment):
    try:
        yag = yagmail.SMTP(GMAIL_USER, GMAIL_APP_PASSWORD)
        subject = f"New Portfolio Comment from {name}"
        contents = f"Name: {name}\nComment: {comment}"
        yag.send(to=EMAIL_RECEIVER, subject=subject, contents=contents)
        print(f"Email sent to {EMAIL_RECEIVER}.")
    except Exception as e:
        print("Failed to send email:", str(e))

def update_analytics():
    global CLICK_COUNT
    CLICK_COUNT += 1

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if password and password not in PASSWORDS:
            return render_template("login.html")
        session["user"] = username or "Guest"
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home")
def home():
    update_analytics()
    return render_template("index.html", click_count=CLICK_COUNT, comment_count=len(COMMENT_LIST))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    msg = ""
    if request.method == "POST":
        name = request.form.get("name") or "Anonymous"
        comment = request.form.get("comment") or ""
        if comment.strip():
            COMMENT_LIST.append((name, comment.strip()))
            send_comment_alert(name, comment.strip())
            msg = "Thanks, comment submitted & alert sent!"
    return render_template("contact.html", comments=COMMENT_LIST, comment_count=len(COMMENT_LIST), click_count=CLICK_COUNT, msg=msg)

if __name__ == "__main__":
    app.run()
