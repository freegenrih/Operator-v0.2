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
                            OperatorCreateNoTests,
                            OperatorGet,
                            OperatorDel,
                            SettingsUsersRegUser,
                            SettingsUsersRegType,
                            SettingsUsersDel,
                            UsersGet
                            )

from views.validators import Validators


def type_user():
    # Get type user list
    return UsersGet().get_type_user()


def get_sesion_user():
    # Get user sesion
    if escape(session['username']):
        user = escape(session['username'])
    else:
        user = 'None'
    return user


def signin():
    # Render page Sign In
    return render_template('signin.html')


def logout():
    # delete sesion and out
    session.pop('username', None)
    return redirect(url_for('signin'))


def info():
    return render_template('info/info.html', user=get_sesion_user(), type_footer=get_sesion_user())


def semple_page_signin():
    if request.method == 'POST':
        # redirect page operator
        if request.form['user_type'] == 'Оператор':
            session['username'] = request.form['user_name']
            return redirect(url_for('operator'))

        # redirect page admin
        elif request.form['user_type'] == 'Администратор':
            session['username'] = request.form['user_name']
            return redirect(url_for('admin'))

        # redirect page engineer
        elif request.form['user_type'] == 'Инженер':
            session['username'] = request.form['user_name']
            return redirect(url_for('engineer'))

        # redirect page users
        elif request.form['user_type'] == 'Пользователь':
            session['username'] = request.form['user_name']
            return  redirect(url_for('users'))

    # redirect page signin
    else:
        return redirect(url_for('signin'))


def semple_page_operator():
    if request.method == 'POST':
        if request.form['submit'] == 'Заявки ИНЖ':
            return redirect(url_for('operator'))

        elif request.form['submit'] == 'Тесты':
            return redirect(url_for('operator_test'))

    else:
        return redirect(url_for('operator'))


def semple_page_engineer():
    if request.method == 'POST':
        if request.form['submit'] == 'Заявки ОПР':
            return redirect(url_for('engineer'))

        elif request.form['submit'] == 'Тесты':
            return redirect(url_for('engineer_test'))

    else:
        return redirect(url_for('engineer'))


def semple_page_users():
    if request.method =='POST':
        if request.form['submit']=='application_pc':
            return redirect(url_for('application_pc'))

        if request.form['submit']=='report_tests':
            return redirect(url_for('report_tests'))

# -------------------------------------------------Users----------------------------------------------------------------
def users():
    return render_template('users/users.html', user=get_sesion_user(), type_footer=get_sesion_user())


def application_pc():
    return render_template('users/application_pc.html', user=get_sesion_user(), type_footer=get_sesion_user())


def report_tests():
    return render_template('users/report_tests.html', user=get_sesion_user(), type_footer=get_sesion_user())
# -----------------------------------------------End Users--------------------------------------------------------------


# ------------------------------------------------Operator--------------------------------------------------------------
def operator():
    # create operator note to engineer
    if request.method == 'POST':
        if request.form['submit'] == 'create_note':
            if Validators(request.form['select_pult'], 'name', min_len=6, max_len=6).valid_name() \
                    and Validators(int(request.form['number_object']), 'id').valid_id() \
                    and Validators(request.form['select_operation'], 'name', min_len=8, max_len=15).valid_name() \
                    and Validators(request.form['add_comment'], 'name', min_len=1, max_len=300).valid_name() == True:

                OperatorCreate(get_sesion_user(),
                               request.form['select_pult'],
                               request.form['number_object'],
                               request.form['select_operation'],
                               request.form['add_comment']
                               ).create_note()
                return redirect(url_for('operator'))
            else:
                return redirect(url_for('operator'))

        # operator delete note by id note
        elif request.form['submit'] == 'delete':
            if Validators(int(request.form['optradio']), 'id').valid_id() == True:
                OperatorDel(request.form['optradio']).delete_note()
                return redirect(url_for('operator'))
            else:
                return redirect(url_for('operator'))

    else:
        return render_template('operator/operator.html',
                               application_operator=OperatorGet().get_list_note(),
                               user=get_sesion_user(),type_footer=get_sesion_user())


def operator_test():
    pass
# ---------------------------------------------End Operator-------------------------------------------------------------


# ------------------------------------------------Engineer--------------------------------------------------------------
def engineer():
    # completion operators note
    if request.method == 'POST':
        if request.form['submit'] == 'completion':
            if Validators(int(request.form['optradio']), 'id').valid_id() == True:
                EngineerUpdate(request.form['optradio'], get_sesion_user()).update_note()
                return redirect(url_for('engineer'))
            else:
                return redirect(url_for('engineer'))
    else:
        return render_template('engineer/engineer.html',
                               application_engineer=EngineerGet().get_list_note(),
                               user=get_sesion_user(),type_footer=get_sesion_user())


def engineer_test():
    return render_template('engineer/engineer_test.html', user=get_sesion_user(), type_footer=get_sesion_user())
# ---------------------------------------------End Engineer-------------------------------------------------------------


# -------------------------------------------------Admin----------------------------------------------------------------
def admin():
    return render_template('admin/admin.html', user=get_sesion_user(),type_footer=get_sesion_user())


def settings_users():
    if request.method == 'POST':
        # Create new user
        if request.form['submit'] == 'Зарегестрировать Пользователя':
            if Validators(request.form['user_name'], 'name', min_len=3, max_len=20).valid_name() \
                    and Validators(request.form['user_password'], 'password', min_len=5, max_len=10).valid_password() \
                    and Validators(request.form['user_type'], 'name', min_len=3, max_len=15).valid_name() == True:
                SettingsUsersRegUser(request.form['user_name'],
                                     request.form['user_password'],
                                     request.form['user_type']).reg_user()
                return redirect(url_for('settings_users'))
            else:
                return redirect(url_for('settings_users'))
        # Delete user
        elif request.form['submit'] == 'delete_user':
            if Validators(int(request.form['optradio']), 'id').valid_id() == True:
                SettingsUsersDel(request.form['optradio']).delete_users()
                return redirect(url_for('settings_users'))
            else:
                return redirect(url_for('settings_users'))

        # Delete user type
        elif request.form['submit'] == 'delete_user_type':
            if Validators(int(request.form['optradio']), 'id').valid_id() == True:
                SettingsUsersDel(request.form['optradio']).delete_user_type()
                return redirect(url_for('settings_users'))
            else:
                return redirect(url_for('settings_users'))

        # Create user type
        elif request.form['submit'] == 'Зарегестрировать Новый Тип Пользователя':
            if Validators(request.form['user_name_type'], 'name', min_len=3, max_len=20).valid_name() == True:
                SettingsUsersRegType(request.form['user_name_type']).reg_new_type()
                return redirect(url_for('settings_users'))
            else:
                return redirect(url_for('settings_users'))
    else:
        return render_template('admin/settings_users.html',
                               users=UsersGet().get_list_user(),
                               type_user=type_user(),
                               user=get_sesion_user(),
                               type_footer=get_sesion_user()
                               )


def settings_phone():
    if request.method == 'POST' and request.form['submit'] == 'confirm':
        # print(request.form['oil'])
        # print(request.form['price_oil'])
        # print(request.form['distance'])
        # print(request.form['price_day'])
        # print(request.form['spent time'])
        result_price_oil = int(request.form['oil']) / 100 * int(request.form['price_oil']) * int(
            request.form['distance'])
        result_peopl_price = int(request.form['price_day']) / 8 * int(request.form['spent time'])
        result_full_price = {'firm': result_price_oil,
                             'people': result_peopl_price,
                             'full_price': result_price_oil + result_peopl_price}
        return render_template('admin/settings_phone.html', user=get_sesion_user(), price=result_full_price)
    else:
        return render_template('admin/settings_phone.html', user=get_sesion_user(),type_footer=get_sesion_user())
# -----------------------------------------------End Admin--------------------------------------------------------------

