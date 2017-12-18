from flask import Flask


from Settings_app import KEY


from Settings_app import (
                          config_debug_local,
                          config_debug_105,
                          config_debug_my_work,
                          config_no_debug
                          )

from views.base_views import (app,
                              signin,
                              users,
                              # upload_file,
                              semple_page_users,
                              users_sms,
                              users_application_pc,
                              users_operational_map,
                              users_update_object_users,
                              users_upload_file,
                              report_tests,
                              operator,
                              # operator_test,
                              engineer,
                              engineer_sms,
                              engineer_test,
                              engineer_users_application_pc,
                              engineer_application_operator,
                              engineer_operational_map,
                              engineer_update_object_users,
                              engineer_upload_file_no_test,
                              admin,
                              semple_page_signin,
                              semple_page_operator,
                              semple_page_engineer,
                              settings_users,
                              settings_phone,
                              logout,
                              info
                              )


app = Flask(__name__)
app.secret_key = KEY


app.add_url_rule('/', view_func=signin, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-signin', view_func=semple_page_signin, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-operator', view_func=semple_page_operator, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-engineer', view_func=semple_page_engineer, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-users', view_func=semple_page_users, methods=['GET', 'POST'])

app.add_url_rule('/users', view_func=users, methods=['GET', 'POST'])
app.add_url_rule('/users-application-pc', view_func=users_application_pc, methods=['GET', 'POST'])
app.add_url_rule('/users-report-tests', view_func=report_tests, methods=['GET', 'POST'])
app.add_url_rule('/users-operational-map', view_func=users_operational_map, methods=['GET', 'POST'])
app.add_url_rule('/users-sms', view_func=users_sms, methods=['GET', 'POST'])
app.add_url_rule('/users-update-object-users', view_func=users_update_object_users, methods=['GET', 'POST'])
app.add_url_rule('/users-upload-file', view_func=users_upload_file, methods=['POST'])

app.add_url_rule('/operator', view_func=operator, methods=['GET', 'POST'])
# на развитие
# app.add_url_rule('/operator-test', view_func=operator_test, methods=['GET', 'POST'])

app.add_url_rule('/engineer', view_func=engineer, methods=['GET', 'POST'])
app.add_url_rule('/engineer-test', view_func=engineer_test, methods=['GET', 'POST'])
app.add_url_rule('/engineer-upload-file-no-test', view_func=engineer_upload_file_no_test, methods=['POST'])
app.add_url_rule('/engineer-users-application-pc', view_func=engineer_users_application_pc, methods=['GET', 'POST'])
app.add_url_rule('/engineer-application-operator', view_func=engineer_application_operator, methods=['GET', 'POST'])
app.add_url_rule('/engineer-operational-map', view_func=engineer_operational_map, methods=['GET', 'POST'])
app.add_url_rule('/engineer-sms', view_func=engineer_sms, methods=['GET', 'POST'])
app.add_url_rule('/engineer-update-object-users', view_func=engineer_update_object_users, methods=['GET', 'POST'])

app.add_url_rule('/admin', view_func=admin, methods=['GET', 'POST'])
app.add_url_rule('/settigs-users', view_func=settings_users, methods=['GET', 'POST'])
app.add_url_rule('/settigs-phone', view_func=settings_phone, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout, methods=['GET'])
app.add_url_rule('/info', view_func=info, methods=['GET'])


# app.add_url_rule('/uploads', view_func=upload_file, methods=['GET','POST'])


# error handlers
from views.error_handlers import page_not_found, page_error, bad_request

app.register_error_handler(400, bad_request)
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, page_error)

if __name__ == '__main__':
    app.run(
            # host='localhost',
            host='192.168.100.74',
            port=5001,
            debug=True
            # debug=False
    )
