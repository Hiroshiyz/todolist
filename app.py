from flask import Flask, render_template, request, redirect
from database.database import init_db, get_all_tasks, add_task, delete_task, mark_task_done

# flask
app = Flask(__name__)

# 顯示get


@app.route('/', methods=['GET'])
def home():
    tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)

# 新增task


@app.route('/', methods=['POST'])
def sumbit_task():
    title = request.values['title']
    if title:
        add_task(title)
    return redirect('/')

# 刪除


@app.route('/delete/<int:task_id>', methods=['POST'])
def deletes(task_id):
    delete_task(task_id)
    return redirect('/')

# 標記


@app.route('/mark/<int:task_id>', methods=['POST'])
def mark(task_id):
    mark_task_done(task_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
