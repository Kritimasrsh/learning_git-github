from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

to_do_list = []

@app.route('/')
def index():
    return render_template('index.html', tasks=to_do_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        to_do_list.append(task)
    return redirect(url_for('index'))

@app.route('/remove/<int:task_id>')
def remove(task_id):
    if 0 <= task_id < len(to_do_list):
        to_do_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)