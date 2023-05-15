# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)
# tasks = []

# @app.route("/")  <button class="inline-flex text-white bg-red-500 border-0 py-2 px-6 focus:outline-none hover:bg-red-600 rounded text-lg">Get Started </button>  <button class="inline-flex text-white bg-red-500 border-0 py-2 px-6 focus:outline-none hover:bg-red-600 rounded text-lg">Get Started </button>
# def home():
#     return render_template('home.html')

# @app.route("/login")
# def index():
#     return render_template("todo.html", tasks=tasks)

# @app.route("/myform",methods=["GET","POST"])
# def myform():
#     print(request.form)
#     if request.method == "POST":
#         user=request.form["user"]
#         password=request.form["password"]
#         if user == "Aish" and password == "1234":
#                 return redirect(url_for("todo", user = user))
#         elif user == "Navya" and password == "1234":
#             return redirect(url_for("todo", user = user))
#         else:
#             return redirect('/')

# @app.route('/todo', methods=['GET', 'POST'])
# def todo():
#     if request.method == 'POST':
#         # Add a new task to the list
#         task = request.form['task']
#         tasks.append(task)
#         user = request.form.get('user')
#         return redirect(url_for("todo"))
#     else:
#         # Render the todo template with the list of tasks
#         # user = request.args['user']
#         return render_template('todo.html', tasks=tasks)

# @app.route("/delete_task/<int:todo>")
# def delete_task(todo):
#     tasks.pop(todo)
#     return redirect(url_for("todo"))

# if __name__ == "__main__":
#     app.run(debug=True,port=12345)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route("/")
def home():
    return render_template('login.html')

# @app.route("/login")
# def index():
#     return render_template("todo.html", tasks=tasks)

@app.route("/myform",methods=["GET","POST"])
def myform():
    print(request.form)
    if request.method == "POST":
        user=request.form["user"]
        password=request.form["password"]
        if user == "Aish" and password == "1234":
                return redirect(url_for("todo", user = user))
        elif user == "Navya" and password == "1234":
            return redirect(url_for("todo", user = user))
        else:
            return redirect('/')

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        # Add a new task to the list
        task = request.form['task']
        tasks.append(task)
        user = request.form.get('user')
        return redirect(url_for("todo"))
    else:
        # Render the todo template with the list of tasks
        # user = request.args['user']
        return render_template('todo.html', tasks=tasks)
    
@app.route("/delete_task/<int:todo>")
def delete_task(todo):
    tasks.pop(todo)
    return redirect(url_for("todo"))

@app.route("/update_task/<int:todo>", methods=["GET","POST"])
def update_task(todo):
    if request.method == 'POST':
        new_value = request.form['new_value']
        tasks[todo] = new_value
        return redirect(url_for("todo"))
    else:
        old_value = tasks[todo]
        return render_template('test.html', old_value = old_value, todo = todo)


if __name__ == "__main__":
    app.run(debug=True,port=12345)