import os

root = r'C:\GitHub\AI_Website'

app_py = '''# app.py (Flask app)
from flask import Flask, render_template, request, redirect, url_for, session
import yagmail
import os

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
        contents = f"Name: {name}\\nComment: {comment}"
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
'''

login_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login | Prabhu's Portfolio</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  <style>
    .video-center { display: flex; align-items: center; justify-content: center; margin-bottom: 28px; }
  </style>
</head>
<body>
<div class="container gradient-bg">
    <div class="video-center">
      <video width="700" height="420" controls style="margin: auto;">
        <source src="{{ url_for('static', filename='Avatar-IV-Video_2.mp4') }}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <h2>Login (Optional)</h2>
    <form method="post" style="margin-bottom:20px;">
      <input type="text" name="username" placeholder="Your Username (optional)"><br>
      <input type="password" name="password" placeholder="Password (optional)"><br>
      <button type="submit">Login</button>
    </form>
    <form method="get" action="{{ url_for('home') }}">
      <button type="submit">Skip Login</button>
    </form>
</div>
</body>
</html>
'''

index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Prabhu's Portfolio</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  <script>
    function openInNewTab(url) {
      window.open(url, '_blank').focus();
    }
  </script>
  <style>
    .video-home-center {display:flex;justify-content:center;align-items:center;margin-bottom:28px;}
  </style>
</head>
<body>
<div class="container gradient-bg">
  <form method="get" action="{{ url_for('login') }}">
    <button type="submit" style="background:#8e24aa;">&larr; Back to Login</button>
  </form>
  <div class="video-home-center">
    <video width="720" height="420" controls style="margin:20px 0;">
      <source src="{{ url_for('static', filename='Avatar-IV-Video_1.mp4') }}" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <h1>Welcome to my AI-powered portfolio!</h1>
  <p style="font-size:20px;">
    I have explored and applied a wide range of advanced AI tools for end-to-end project development, technical documentation, analysis, prototyping—as well as building and deploying this very website!<br><br>
    <span style="color:#ff9800;">
      <b>AI tools used for documentation, research, product content:</b><br>
      Perplexity, Gemini, Claude.ai, Colab (Python), Copilot
    </span><br>
    <span style="color:#e91e63;">
      <b>Prototyping & Wireframes:</b><br>
      Figma, Copilot
    </span><br><br>
    <span style="color:#ab47bc;">
      <b>This website was collaboratively created and globally deployed using:</b><br>
      Google Colab, Python, Flask, Ngrok (for global publishing), Yagmail (for notifications), and code powered by ChatGPT.
    </span>
  </p>
  <h3 style="color:#8e24aa;">My Work & Links:</h3>
  <ul style="text-align:left; max-width:800px; margin:auto;">
    <li><a href="#" onclick="openInNewTab('https://docs.google.com/document/d/1yEYtZECB60CvFOz9_1aCFz3LTJ9WlOKT4D8cXxDj82k/edit?usp=sharing')">Project PDF</a></li>
    <li><a href="#" onclick="openInNewTab('https://g.co/gemini/share/cc9bd524f79c')">Gemini Web Page</a></li>
    <li><a href="#" onclick="openInNewTab('https://docs.google.com/spreadsheets/d/1L_yxeFsxY1SS4Cjkkw02TiFf-u6ImRA3I8dxa45GmUw/edit?gid=2056697474#gid=2056697474')">Detailed Acceptance Criteria</a></li>
    <li><a href="#" onclick="openInNewTab('https://drive.google.com/file/d/15TG86fTjd2wQ3dRKl9TPUT-F1srCTSbp/view?usp=sharing')">Referrer Flow Wireframes</a></li>
    <li><a href="#" onclick="openInNewTab('https://drive.google.com/file/d/1MbUwinSkSJZuZjD0Io6qyTAzIjpAwLab/view?usp=sharing')">Referee Flow Wireframes</a></li>
    <li><a href="#" onclick="openInNewTab('https://www.figma.com/proto/Oe0TAF1ljMXOSPuLRcllT2/BB-Assignment_Prototyping?node-id=41-4&t=0XJB5SDIUIFB3Wkx-0&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A2')">Referrer Flow Prototypes</a></li>
    <li><a href="#" onclick="openInNewTab('https://www.figma.com/proto/Oe0TAF1ljMXOSPuLRcllT2/BB-Assignment_Prototyping?node-id=20-5&p=f&t=GLCzDPuhCah9EXFw-0&scaling=min-zoom&content-scaling=fixed&page-id=20%3A2&starting-point-node-id=20%3A5')">Referee Flow Prototypes</a></li>
    <li><a href="#" onclick="openInNewTab('https://drive.google.com/file/d/19A_WqPjjZqTISLL9F0Q-ehDdtBrSJwyy/view?usp=sharing')">Competitive Analysis/Market/Problem/Solution Discovery</a></li>
    <li><a href="#" onclick="openInNewTab('https://claude.ai/public/artifacts/901107d9-b38d-475f-96a3-5edd0ffd49c3')">Refer-a-Friend Competitive Analysis Dashboard</a></li>
    <li><a href="#" onclick="openInNewTab('https://prabu-saas-global-profile.netlify.app/')">Digital Profile</a></li>
  </ul>
  <br>
  <p><a href="{{ url_for('contact') }}">Contact Me & Comments</a></p>
  <hr>
  <p><b>Website visits:</b> {{ click_count }}<br>
    <b>Comments received:</b> {{ comment_count }}</p>
</div>
</body>
</html>
'''

contact_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Contact | Prabhu's Portfolio</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
<div class="container gradient-bg">
    <h2>Contact Me</h2>
    <p>Email: <b>gideonprabu@gmail.com</b><br>
       LinkedIn: <a style="color:#ff5722;" href="https://www.linkedin.com/in/prabu1301" target="_blank">LinkedIn Profile</a></p>
    <hr>
    <h3>Leave Your Feedback/Comment:</h3>
    <form method="post">
      <input type="text" name="name" placeholder="Your Name"><br>
      <textarea name="comment" placeholder="Your Comment" rows="3" required></textarea><br>
      <button type="submit">Submit Comment</button>
    </form>
    {% if msg %}
      <p style="color:#43a047;">{{ msg }}</p>
    {% endif %}
    <hr>
    <h4>All Comments ({{ comment_count }})</h4>
    <ul style="max-width:600px; margin:auto; text-align:left;">
      {% for c in comments %}
        <li><b>{{ c[0] }}</b>: {{ c[1] }}</li>
      {% endfor %}
    </ul>
    <hr>
    <p>
      <b>Website visits:</b> {{ click_count }}<br>
      <b>Comments received:</b> {{ comment_count }}
    </p>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</div>
</body>
</html>
'''

style_css = '''body {
  font-family: 'Segoe UI', 'Arial', sans-serif;
  background: linear-gradient(120deg, #ff9800 0%, #f44336 50%, #8e24aa 100%);
  color: #222;
  min-height: 100vh;
  margin:0;
}
.gradient-bg {
  background: linear-gradient(120deg, #faeeff 0%, #ffe7db 80%);
}
.container {
  width: 85vw;
  margin: 45px auto 24px auto;
  border-radius: 24px;
  padding: 38px 16px 28px 16px;
  box-shadow: 0px 2px 36px 0px rgba(255,140,91,0.12), 0px 2px 12px 0px rgba(189,99,255,0.08);
}
input, textarea {
  width: 80%;
  margin: 14px;
  padding: 12px;
  border-radius: 12px;
  border: 1px solid #ffe0b2;
  font-size: 17px;
  background: #fffaf3;
}
button {
  background: linear-gradient(120deg, #ff9800 0%, #e91e63 100%);
  color: white;
  border: none;
  padding: 12px 26px;
  border-radius: 14px;
  font-size: 20px;
  margin-top:4px;
  cursor: pointer;
  box-shadow: 0px 2px 12px 0px #ffcdd2;
}
button:hover {
  background: linear-gradient(120deg, #e91e63 0%, #ff9800 100%);
}
hr { margin: 32px 0; border: 0; border-top: 2px solid #e1bee7;}
footer {
  margin-top: 22px;
  font-size: 15px;
  color: #666;
}
ul {padding-left: 32px;}
a { color: #8e24aa; text-decoration: underline; }
a:hover { color: #ff5722; }
'''