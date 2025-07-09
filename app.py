from flask import Flask, render_template, request, redirect
app = Flask(__name__)
tasks = []
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", tasks=tasks)
@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    if task_text:
        tasks.append({"text": task_text, "done": False})
    return redirect("/")
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect("/")
@app.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    if 0 <= id < len(tasks):
        tasks[id]["done"] = not tasks[id]["done"]
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)

