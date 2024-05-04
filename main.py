from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)


@app.route('/delete', methods=['POST'])
def delete_task():
    task_to_delete = request.form['task']
    tasks.remove(task_to_delete)
    return redirect(url_for('index'))

@app.route('/edit', methods=['POST'])
def edit_task():
    old_task = request.form['old_task']
    new_task = request.form['new_task']
    index = tasks.index(old_task)
    tasks[index] = new_task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
