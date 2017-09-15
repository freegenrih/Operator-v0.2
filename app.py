from flask import Flask
from Settings_app import (key,
                          config_debug_local,
                          config_debug_105,
                          config_debug_my_work,
                          config_no_debug
                          )

from views.base_views import (signin,
                              operator,
                              operator_test,
                              operator_application_for_electricians,
                              engineer,
                              engineer_test,
                              engineer_application_for_electricians,
                              admin,
                              semple_page_signin,
                              semple_page_operator,
                              semple_page_engineer,
                              settings_users,
                              settings_phone,
                              logout,
                              test
                              )

app = Flask(__name__)
app.secret_key = key

app.add_url_rule('/', view_func=signin, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-signin', view_func=semple_page_signin, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-operator', view_func=semple_page_operator, methods=['GET', 'POST'])
app.add_url_rule('/semple-page-engineer', view_func=semple_page_engineer, methods=['GET', 'POST'])
app.add_url_rule('/operator', view_func=operator, methods=['GET', 'POST'])
app.add_url_rule('/operator-test', view_func=operator_test, methods=['GET', 'POST'])
app.add_url_rule('/operator-application-for-electricians',
                 view_func=operator_application_for_electricians,
                 methods=['GET', 'POST'])
app.add_url_rule('/engineer', view_func=engineer, methods=['GET', 'POST'])
app.add_url_rule('/engineer-test', view_func=engineer_test, methods=['GET', 'POST'])
app.add_url_rule('/engineer-application-for-electricians',
                 view_func=engineer_application_for_electricians,
                 methods=['GET', 'POST'])
app.add_url_rule('/admin', view_func=admin, methods=['GET', 'POST'])
app.add_url_rule('/settigs-users', view_func=settings_users, methods=['GET', 'POST'])
app.add_url_rule('/settigs-phone', view_func=settings_phone, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout, methods=['GET'])
app.add_url_rule('/test', view_func=test, methods=['GET', 'POST'])

# error handlers
from views.error_handlers import page_not_found, page_error

app.register_error_handler(404, page_not_found)
app.register_error_handler(500, page_error)

if __name__ == '__main__':
    app.run(#**config_debug_local,
            #**config_debug_105,
            **config_debug_my_work,
            #**config_no_debug
            )
