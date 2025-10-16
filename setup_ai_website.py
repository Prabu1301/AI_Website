import os

# === Your GitHub repo folder path ===
project_root = r"C:\GitHub\AI_Website"

folders = [
    project_root,
    os.path.join(project_root, "templates"),
    os.path.join(project_root, "static"),
]

files = {
    os.path.join(project_root, "app.py"): "# Paste your Flask app code here\n",
    os.path.join(project_root, "requirements.txt"): "flask\nyagmail\n",
    os.path.join(project_root, "Procfile"): "web: python app.py\n",
    os.path.join(project_root, "README.md"): (
        "# AI Portfolio Website\n\n"
        "This is a Flask-powered AI portfolio site with video widgets, feedback forms, and email notifications.\n"
        "Deployable free on Railway.app and shareable globally.\n"
        "See README for setup and links.\n"
    ),
    os.path.join(project_root, "templates", "login.html"): "<!-- Paste your login.html template here -->\n",
    os.path.join(project_root, "templates", "index.html"): "<!-- Paste your index.html template here -->\n",
    os.path.join(project_root, "templates", "contact.html"): "<!-- Paste your contact.html template here -->\n",
    os.path.join(project_root, "static", "style.css"): "/* Paste your CSS code here */\n",
    # Do NOT auto-create MP4 files; drag and drop your videos into /static after running this!
}

for folder in folders:
    if not os.path.isdir(folder):
        os.makedirs(folder)
        print(f"Created folder: {folder}")

for path, default_content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(default_content)
    print(f"Created file: {path}")

print("\n✅ All folders and starter files are now created under", project_root)
print("✅ Drag your videos into /static manually!")
print("✅ Paste your actual Flask, HTML, and CSS code as needed before committing.")
