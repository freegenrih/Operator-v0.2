from flask import (render_template,
                   request,
                   session,
                   escape,
                   url_for,
                   redirect
                   )


def signin():
    return render_template('signin.html')


def operator():
    return render_template('operator.html')


def engineer():
    return render_template('engineer.html')


def admin():
    return render_template('admin.html')
