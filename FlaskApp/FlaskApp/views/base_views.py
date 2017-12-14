import os
from werkzeug.utils import secure_filename
from flask import (Flask,
                   render_template,
                   request,
                   session,
                   escape,
                   url_for,
                   redirect
                   )


from views.executor import (EngineerGet,
                            EngineerUpdate,
                            OperatorCreate,
                            OperatorConfig,
                            OperatorCreateNoTests,
                            OperatorGet,
                            OperatorDel,
                            SettingsUsersRegUser,
                            SettingsUsersRegType,
                            SettingsUsersDel,
                            UsersGet,
                            UsersDel,
                            UsersCreate,
                            OperMap,
                            ObjectsNoTests,
                            UpdateObjectsData
                            )

from Settings_app import (KEY,
                          BASE_DIR
                          )
from views.validators import Validators

app = Flask(__name__)
UPLOAD_FOLDER = BASE_DIR+"/static/media/objects_maps"
UPLOAD_FOLDER_USERS_PHONES = BASE_DIR+"/static/media/Users_Phones"
UPLOAD_FOLDER_NO_TEST = BASE_DIR+"/static/media/NoTests"
ALLOWED_EXTENSIONS = set(['txt','py','pdf','png','jpg','jpeg','xlsx'])


app.secret_key = KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS





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
        if request.form['submit'] == 'opr_app':
            return redirect(url_for('engineer_application_operator'))

        elif request.form['submit'] == 'tests':
            return redirect(url_for('engineer_test'))

        elif request.form['submit'] == 'usr_app':
            return redirect(url_for('engineer_users_application_pc'))

        elif request.form['submit'] == 'engineer_operational_map':
            return redirect(url_for('engineer_operational_map'))


        elif request.form['submit'] == 'engineer_update_object_users':
            return redirect(url_for('engineer_update_object_users'))

    else:
        return redirect(url_for('engineer'))


def semple_page_users():
    if request.method =='POST':
        if request.form['submit']=='users_application_pc':
            return redirect(url_for('users_application_pc'))

        if request.form['submit']=='report_tests':
            return redirect(url_for('report_tests'))

        if request.form['submit']=='users_update_object_users':
            return redirect(url_for('users_update_object_users'))

        if request.form['submit']=='users_operational_map':
            return redirect(url_for('users_operational_map'))

# -------------------------------------------------Users----------------------------------------------------------------
def users():
    return render_template('users/users.html', user=get_sesion_user(), type_footer=get_sesion_user())


def users_application_pc():
    if request.method =='POST':
        if request.form['submit']=='create_note':
            UsersCreate(
                name_user=get_sesion_user(),
                message=str(request.form['select_operation']+' '+request.form['add_comment']).replace("'","\"")
            ).create_application_pc()
            return redirect(url_for('users_application_pc'))

        elif request.form['submit']=='delete':
            UsersDel(id=request.form['optradio']).delete_application_pc()
            return redirect(url_for('users_application_pc'))
    else:
        return render_template('users/users_application_pc.html',
                           user=get_sesion_user(),
                           type_footer=get_sesion_user(),
                           users_application_pc=UsersGet().get_application_pc()
                           )






def report_tests():
    if request.method == 'POST':
        if request.form['submit']=='update':
            print("update no test users page")
            ObjectsNoTests(id=request.form['optradio'],username=get_sesion_user()).update_report_no_test_objects()
            return redirect(url_for('report_tests'))
    else:
        return render_template('users/report_tests.html',
                               user=get_sesion_user(),
                               type_footer=get_sesion_user(),
                               list_no_test=ObjectsNoTests().get_report_no_tests_objects(),
                               list_files=os.listdir(UPLOAD_FOLDER_NO_TEST)
                               )


def users_upload_file():
    try:
        if request.method == 'POST':
            print("POST")
            if request.files['file']:
                file = request.files['file']
                if file and allowed_file(file.filename):

                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        OperMap(
                            username=get_sesion_user(),
                            message_text=str(request.form['add_comment']),
                            link_file=str(filename),
                            object_number=str(request.form['object_number'])
                        ).create_map()
                        # return redirect(url_for('users_operational_map'))

    except:
        return redirect(url_for('users_operational_map'))
    finally:
        return redirect(url_for('users_operational_map'))



def users_operational_map():
    if request.method == 'POST':
        if request.form['submit'] == "delete":
            try:
                OperMap(id=request.form['optradio']).delete_map()
                print("delete of DB")
                print(os.path.join(UPLOAD_FOLDER, str(request.form['file_name'])))
                os.remove(os.path.join(UPLOAD_FOLDER, str(request.form['file_name'])))
                print("delete of folder ="+request.form['file_name'])

            except:
                return redirect(url_for('users_operational_map'))
            finally:
                return redirect(url_for('users_operational_map'))

        else:
            return redirect(url_for('users_operational_map'))


    else:
        return render_template("users/users_operational_map.html",
                           user=get_sesion_user(),
                           type_footer=get_sesion_user(),
                           list_files=os.listdir(app.config['UPLOAD_FOLDER']),
                           list_map=OperMap().get_map()
                           )


def users_update_object_users():
    if request.method == 'POST':
        print(request.form['submit'])
        if request.form['submit']== 'delete':
            print("delete object data for id=",request.form['optradio'])
            UpdateObjectsData(id=request.form['optradio']).delete_object_data()
            return redirect(url_for('users_update_object_users'))

        elif request.form['submit']=='create_note':
            print(request.form['object_number'])
            # print(request.form['object_name'])
            # print(request.form['object_address'])
            # print(request.form['message'])
            return redirect(url_for('users_update_object_users'))
        else:
            return redirect(url_for('users_update_object_users'))

    else:
        return render_template("users/users_update_object_users.html",
                               user=get_sesion_user(),
                               type_footer=get_sesion_user(),
                               objects_data=UpdateObjectsData().get_object_data()
                               )



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
                               request.form['select_pult'].replace("'","\""),
                               request.form['number_object'].replace("'","\""),
                               request.form['select_operation'].replace("'","\""),
                               request.form['add_comment'].replace("'","\"")
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
                               user=get_sesion_user(),
                               type_footer=get_sesion_user())


# def operator_test():
#     if request.method == 'POST':
#         if request.form['submit']=='create_note':
#             OperatorCreateNoTests(object_number=request.form['number_object'].replace("'","\""),
#                                   name_operator=get_sesion_user(),
#                                   why_there_is_no_test=request.form['why_there_is_no_test'].replace("'","\"")
#                                   ).create_note_no_test()
#             return redirect(url_for('operator_test'))
#
#         elif request.form['submit']=='copy':
#             OperatorCreateNoTests(object_number=request.form['number_object'],
#                                   name_operator=get_sesion_user(),
#                                   why_there_is_no_test=request.form['why_there_is_no_test']
#                                   ).create_note_no_test()
#             return redirect(url_for('operator_test'))
#
#         elif request.form['submit']=='select_for_date':
#             OperatorConfig(date_save=request.form['date']).write_date_search_no_test()
#             return redirect(url_for('operator_test'))
#
#         elif request.form['submit']=='delete':
#             OperatorDel(id=request.form['optradio']).delete_note_no_tests()
#             return redirect(url_for('operator_test'))
#
#         else:
#             return redirect(url_for('operator_test'))
#     else:
#         return render_template('operator/operator_test.html',
#                        user=get_sesion_user(),
#                        type_footer=get_sesion_user(),
#                        no_tests=OperatorGet().get_list_no_tests_now(),
#                        no_test_date_search=OperatorGet().get_list_no_test_search_date())

# ---------------------------------------------End Operator-------------------------------------------------------------


# ------------------------------------------------Engineer--------------------------------------------------------------
def engineer_upload_file_no_test():
    try:
        if request.method == 'POST':
            print("POST")
            if request.files['file']:
                file = request.files['file']
                if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(UPLOAD_FOLDER_NO_TEST, filename))
                        print("file save no test")
                        print(request.form['month_number'])


                        # return redirect(url_for('users_operational_map'))

    except:
        return redirect(url_for('engineer_test'))
    finally:
        ObjectsNoTests(
            username=get_sesion_user(),
            link_file=str(filename),
            month_number=str(request.form['month_number'])
        ).create_report_no_test_objects()
        print("create no test")
        return redirect(url_for('engineer_test'))


def engineer():
    # completion operators note
    if request.method == 'POST':
        return redirect(url_for('engineer'))
    else:
        return render_template('engineer/engineer.html',
                               application_engineer=EngineerGet().get_list_note(),
                               user=get_sesion_user(),
                               type_footer=get_sesion_user(),
                               count_application_pc_no_checed=EngineerGet().get_count_application_pc_no_checed(),
                               count_application_pc_checed=EngineerGet().get_count_application_pc_checed(),
                               operator_application_no_checked=EngineerGet().get_count_operator_application_no_checked(),
                               operator_application_checked=EngineerGet().get_count_operator_application_checked(),
                               count_operator_application_all=EngineerGet().get_count_operator_application_all(),
                               count_application_pc_all=EngineerGet().get_count_application_pc_all(),
                               count_application_map_no_checked =EngineerGet().count_application_map_no_checked(),
                               count_application_map_checked =EngineerGet().count_application_map_checked(),
                               count_application_map_all =EngineerGet().count_application_map_all(),
                               )


def engineer_application_operator():
    # completion operators note
    if request.method == 'POST':
        if request.form['submit'] == 'completion':
            if Validators(int(request.form['optradio']), 'id').valid_id() == True:
                EngineerUpdate(request.form['optradio'], get_sesion_user()).update_note()
                return redirect(url_for('engineer_application_operator'))
            else:
                return redirect(url_for('engineer_application_operator'))
    else:
        return render_template('engineer/engineer_application_operaor.html',
                               application_engineer=EngineerGet().get_list_note(),
                               user=get_sesion_user(),type_footer=get_sesion_user())


def engineer_test():
    if request.method == 'POST':
        if request.form['submit']=='delete':
            try:
                ObjectsNoTests(id=request.form['optradio']).delete_report_no_test_objects()
                print("delete of DB")
                print(os.path.join(UPLOAD_FOLDER_NO_TEST, str(request.form['file_name'])))
                os.remove(os.path.join(UPLOAD_FOLDER_NO_TEST, str(request.form['file_name'])))
                print("delete of folder ="+request.form['file_name'])

            except:
                return redirect(url_for('engineer_test'))
            finally:
                return redirect(url_for('engineer_test'))

    return render_template('engineer/engineer_test.html',
                           user=get_sesion_user(),
                           type_footer=get_sesion_user(),
                           list_no_test=ObjectsNoTests().get_report_no_tests_objects(),
                           list_files=os.listdir(UPLOAD_FOLDER_NO_TEST)
                           )


def engineer_users_application_pc():
    if request.method == 'POST':
        if request.form['submit']=='completion':
            EngineerUpdate(
                id_update_note=request.form['optradio'],
                name_user=get_sesion_user(),
                comment=request.form['add_comment'].replace("'","\"")
            ).update_application_pc()
            return redirect(url_for('engineer_users_application_pc'))

    else:
        return render_template('engineer/engineer_application_pc_users.html',
                               user=get_sesion_user(),
                               type_footer=get_sesion_user(),
                               users_application_pc=UsersGet().get_application_pc()
                               )


def engineer_operational_map():
    if request.method =="POST":
        if request.form['submit']=='completion':
            print("update app map"+request.form['optradio'])
            try:
                OperMap(username=get_sesion_user(), id=request.form['optradio']).update_map()
            except:
                return redirect(url_for('engineer_operational_map'))
            finally:
                return redirect(url_for('engineer_operational_map'))
    else:
        return render_template("engineer/engineer_operational_map.html",
                               user=get_sesion_user(),
                               type_footer=get_sesion_user(),
                               list_files=os.listdir(app.config['UPLOAD_FOLDER']),
                               list_map=OperMap().get_map())


def engineer_update_object_users():
    return render_template("engineer/engineer_update_object_users.html", user=get_sesion_user(), type_footer=get_sesion_user())
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
