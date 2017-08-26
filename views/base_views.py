from datetime import datetime
from flask import (render_template,
                   request,
                   session,
                   escape,
                   url_for,
                   redirect
                   )

from sqlrw import wraper_write, wraper_read

from views.executor import (EngineerList,
                            EngineerUpdate,
                            OperatorCreate)


def type_user():
    sql_type_user = "SELECT * FROM `user_type`"
    return wraper_read(sql_type_user)


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
                               application_engineer=EngineerList().get_list_note(),
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
        print(request.form['optradio'])
        sql = "DELETE FROM `dbo_operator_application` " \
              "WHERE `dbo_operator_application`.`id` = {};".format(int(request.form['optradio']))
        wraper_write(sql)
        return redirect(url_for('operator'))

    else:
        sql = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"
        return render_template('operator.html',
                               application_operator=wraper_read(sql),
                               user=get_sesion_user())


def admin():
    return render_template('admin.html', user=get_sesion_user())


def settings_users():
    sql_list_users = "SELECT * FROM `dbo_users`"

    if request.method == 'POST' and request.form['submit'] == 'Зарегестрировать Пользователя':

        sql_reg_user = "INSERT INTO `dbo_users` (`id`, `date_register_user`, `user_name`, `user_password`, `user_type`) " \
                       "VALUES (NULL, '{}', '{}', '{}', '{}');".format(str(datetime.now())[0:-7],
                                                                       str(request.form['user_name']),
                                                                       str(request.form['user_password']),
                                                                       str(request.form['user_type'])
                                                                       )
        wraper_write(sql_reg_user)
        return redirect(url_for('settings_users'))

    elif request.method == 'POST' and request.form['submit'] == 'delete_user':
        sql_delete_user = "DELETE FROM `dbo_users` WHERE `dbo_users`.`id` ={} ".format(int(request.form['optradio']))
        wraper_write(sql_delete_user)

        return redirect(url_for('settings_users'))

    elif request.method == 'POST' and request.form['submit'] == 'delete_user_type':
        sql_detete_user_type = "DELETE FROM `user_type` " \
                               "WHERE `user_type`.`id` = {} ".format(int(request.form['optradio']))
        wraper_write(sql_detete_user_type)
        return redirect(url_for('settings_users'))

    elif request.method == 'POST' and request.form['submit'] == 'Зарегестрировать Новый Тип Пользователя':
        sql_reg_type_user = "INSERT INTO `user_type` (`id`, `user_type`) " \
                            "VALUES (NULL, '{}')".format(str(request.form['user_name_type']))
        wraper_write(sql_reg_type_user)
        return redirect(url_for('settings_users'))

    else:
        return render_template('settings_users.html',
                               users=wraper_read(sql_list_users),
                               type_user=type_user(),
                               user=get_sesion_user()
                               )


def settings_phone():
    return render_template('settings_phone.html', user=get_sesion_user())
