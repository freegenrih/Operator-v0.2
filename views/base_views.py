from flask import (render_template,
                   request,
                   session,
                   escape,
                   url_for,
                   redirect
                   )

from views.executor import (EngineerGet,
                            EngineerUpdate,
                            OperatorCreate,
                            OperatorGet,
                            OperatorDel,
                            SettingsUsersRegUser,
                            SettingsUsersRegType,
                            SettingsUsersDel,
                            UsersGet
                            )


def type_user():
    return UsersGet().get_type_user()


def get_sesion_user():
    if escape(session['username']):
        user = escape(session['username'])
    else:
        user = None
    return user


def signin():
    return render_template('signin.html', type_user=type_user())


def logout():
    # delete sesion and exit
    session.pop('username', None)
    return redirect(url_for('signin'))


def semple_page():
    if request.method == 'POST' and request.form['user_type'] == 'Оператор':
        session['username'] = request.form['user_name']
        return redirect(url_for('operator'))

    elif request.method == 'POST' and request.form['user_type'] == 'Администратор':
        session['username'] = request.form['user_name']
        return redirect(url_for('admin'))

    elif request.method == 'POST' and request.form['user_type'] == 'Инженер':
        session['username'] = request.form['user_name']
        return redirect(url_for('engineer'))

    else:
        return redirect(url_for('signin'))


def engineer():
    if request.method == 'POST' and request.form['submit'] == 'completion':
        EngineerUpdate(request.form['optradio'], get_sesion_user()).update_note()
        return redirect(url_for('engineer'))

    else:
        return render_template('engineer.html',
                               application_engineer=EngineerGet().get_list_note(),
                               user=get_sesion_user())


def operator():
    if request.method == 'POST' and request.form['submit'] == 'create_note':
        OperatorCreate(get_sesion_user(),
                       request.form['select_pult'],
                       request.form['number_object'],
                       request.form['select_operation'],
                       request.form['add_comment']
                       ).create_note()
        return redirect(url_for('operator'))

    elif request.method == 'POST' and request.form['submit'] == 'delete':
        OperatorDel(request.form['optradio']).delete_note()
        return redirect(url_for('operator'))

    else:
        return render_template('operator.html',
                               application_operator=OperatorGet().get_list_note(),
                               user=get_sesion_user())


def admin():
    return render_template('admin.html', user=get_sesion_user())


def settings_users():

    if request.method == 'POST' and request.form['submit'] == 'Зарегестрировать Пользователя':
        SettingsUsersRegUser(request.form['user_name'],
                             request.form['user_password'],
                             request.form['user_type']).reg_user()
        return redirect(url_for('settings_users'))

    elif request.method == 'POST' and request.form['submit'] == 'delete_user':
        SettingsUsersDel(request.form['optradio']).delete_users()
        return redirect(url_for('settings_users'))

    elif request.method == 'POST' and request.form['submit'] == 'delete_user_type':
        SettingsUsersDel(request.form['optradio']).delete_user_type()
        return redirect(url_for('settings_users'))

    elif request.method == 'POST' and request.form['submit'] == 'Зарегестрировать Новый Тип Пользователя':
        SettingsUsersRegType(request.form['user_name_type']).reg_new_type()
        return redirect(url_for('settings_users'))

    else:
        return render_template('settings_users.html',
                               users=UsersGet().get_list_user(),
                               type_user=type_user(),
                               user=get_sesion_user()
                               )


def settings_phone():
    return render_template('settings_phone.html', user=get_sesion_user())
