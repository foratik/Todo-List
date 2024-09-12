from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = Task(name=request.form['task'])
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete', methods=['POST'])
def delete_task():
    task_to_delete = Task.query.get(request.form['task_id'])
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit', methods=['POST'])
def edit_task():
    task = Task.query.get(request.form['task_id'])
    task.name = request.form['new_task']
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/done', methods=['POST'])
def do_task():
    task = Task.query.filter_by(id=request.form['task_id']).first()
    task.toggle_status()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, port=5000)
