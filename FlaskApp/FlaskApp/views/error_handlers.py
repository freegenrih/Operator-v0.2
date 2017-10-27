from flask import render_template


def bad_request(e):
    return render_template('errors/400.html'), 400


def page_not_found(e):
    return render_template('errors/404.html'), 404


def page_error(e):
    return render_template('errors/500.html'), 500
