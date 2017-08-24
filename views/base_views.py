from datetime import datetime
from flask import (render_template,
                   request,
                   session,
                   escape,
                   url_for,
                   redirect
                   )

from sqlrw import wraper_write, wraper_read


def signin():
    return render_template('signin.html')


def semple_page():
    if request.method == 'POST' and request.form['user_type'] == 'Оператор':
        return redirect(url_for('operator'))

    elif request.method == 'POST' and request.form['user_type'] == 'Администратор':
        return redirect(url_for('admin'))

    elif request.method == 'POST' and request.form['user_type'] == 'Инженер':
        return redirect(url_for('engineer'))

    else:
        return redirect(url_for('signin'))


def engineer():
    if request.method == 'POST' and request.form['submit'] == 'completion':
        newsql = "UPDATE `dbo_operator_application` " \
                 "SET `checked_engineer` = '1', `date_of_completion` = '{}', `name_engineer_completion` = '21' " \
                 "WHERE `dbo_operator_application`.`id` = {}".format(str(datetime.now())[0:-7],
                                                                     int(request.form['optradio']))
        wraper_write(newsql)
        return redirect(url_for('engineer'))

    else:
        sql = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"
        return render_template('engineer.html', application_engineer=wraper_read(sql))


def operator():
    if request.method == 'POST' and request.form['submit'] == 'create_note':
        sql = "INSERT INTO `dbo_operator_application` " \
              "(`id`, `date_of_creation`, `name_operator`, `name_pult`, `number_object`, `message`," \
              "`checked_engineer`, `date_of_completion`, `name_engineer_completion`) " \
              "VALUES (NULL, '{}', '{}', '{}', '{}', '{}',0, '', ' ');".format(str(datetime.now())[0:-7], str('21'),
                                                                               str(request.form['select_pult']),
                                                                               str(request.form['number_object']),
                                                                               str(request.form['select_operation'])
                                                                               + ' ' + str(request.form['add_comment']))

        wraper_write(sql)

        return redirect(url_for('operator'))

    elif request.method == 'POST' and request.form['submit'] == 'delete':
        print(request.form['optradio'])
        sql = "DELETE FROM `dbo_operator_application` " \
              "WHERE `dbo_operator_application`.`id` = {};".format(int(request.form['optradio']))
        wraper_write(sql)
        return redirect(url_for('operator'))

    else:
        sql = "SELECT * FROM `dbo_operator_application` WHERE `checked_engineer`=0"
        # sql = "SELECT * FROM `dbo_operator_application`  ORDER BY `dbo_operator_application`.`id` DESC "
        return render_template('operator.html', application_operator=wraper_read(sql))


def admin():
    return render_template('admin.html')
