from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, Todo
from forms import TodoForm
from sqlalchemy import select

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    todos = db.session.execute(select(Todo).order_by(Todo.created_at.desc())).scalars().all()
    return render_template("index.html", todos=todos)

@main_bp.route("/add", methods=["GET", "POST"])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(title=form.title.data, description=form.description.data)
        db.session.add(todo)
        db.session.commit()
        flash("Task added successfully!", "success")
        return redirect(url_for("main.index"))
    return render_template("add.html", form=form)

@main_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    todo = db.get_or_404(Todo, id)
    form = TodoForm(obj=todo)
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        db.session.commit()
        flash("Task updated!", "success")
        return redirect(url_for("main.index"))
    return render_template("edit.html", form=form, todo=todo)

@main_bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo = db.get_or_404(Todo, id)
    db.session.delete(todo)
    db.session.commit()
    flash("Task deleted!", "danger")
    return redirect(url_for("main.index"))

@main_bp.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    todo = db.get_or_404(Todo, id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("main.index"))