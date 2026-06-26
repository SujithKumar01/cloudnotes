from flask import Flask, render_template, request, redirect, url_for
from database import create_table
from models import (
    add_note,
    get_all_notes,
    update_note,
    delete_note,
    search_notes
)

app = Flask(__name__)

# Ensure table exists on startup
create_table()

@app.route("/")
def index():
    notes = get_all_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    content = request.form["content"]
    add_note(title, content)
    return redirect(url_for("index"))

@app.route("/edit/<int:note_id>", methods=["POST"])
def edit(note_id):
    title = request.form["title"]
    content = request.form["content"]
    update_note(note_id, title, content)
    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>")
def delete(note_id):
    delete_note(note_id)
    return redirect(url_for("index"))

@app.route("/search")
def search():
    query = request.args.get("q", "")
    if query:
        notes = search_notes(query)
    else:
        notes = []
    return render_template("search.html", notes=notes, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
