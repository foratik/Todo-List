import json
from flask import Flask, render_template, request, redirect, url_for

def update_history(tasks):
    history = open('history.txt', 'w')
    history.write(json.dumps(tasks))
    history.close()

app = Flask(__name__)
history = open('history.txt', 'r')
content = history.read()
if content != '':
    tasks = json.loads(content)
else:
    tasks = []
history.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append([task, 'ongoing'])
        update_history(tasks)
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)


@app.route('/delete', methods=['POST'])
def delete_task():
    task_to_delete = request.form['task']
    for task in tasks:
        if task[0] == task_to_delete:
            tasks.remove(task)
    update_history(tasks)
    return redirect(url_for('index'))


@app.route('/edit', methods=['POST'])
def edit_task():
    old_task = request.form['old_task']
    new_task = request.form['new_task']
    for k in range(len(tasks)):
        if tasks[k][0] == old_task:
            tasks[k] = [new_task, 'ongoing']
            break
    update_history(tasks)
    return redirect(url_for('index'))


@app.route('/done', methods=['POST'])
def do_task():
    task_to_be_done = request.form['my_task']
    for task in tasks:
        if task[0] == task_to_be_done:
            if task[1] == 'ongoing':
                task[1] = 'done'
            else:
                task[1] = 'ongoing'
    update_history(tasks)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
