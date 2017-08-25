from flask import Flask
from Settings_app import key

from views.base_views import (signin,
                              operator,
                              engineer,
                              admin,
                              semple_page,
                              settings_users,
                              settings_phone,

                              )

app = Flask(__name__)
app.secret_key = key

app.add_url_rule('/', view_func=signin, methods=['GET', 'POST'])
app.add_url_rule('/semple_page', view_func=semple_page, methods=['GET', 'POST'])
app.add_url_rule('/operator', view_func=operator, methods=['GET', 'POST'])
app.add_url_rule('/engineer', view_func=engineer, methods=['GET', 'POST'])
app.add_url_rule('/admin', view_func=admin, methods=['GET', 'POST'])
app.add_url_rule('/settigs_users', view_func=settings_users, methods=['GET', 'POST'])
app.add_url_rule('/settigs_phone', view_func=settings_phone, methods=['GET', 'POST'])

# error handlers
from views.error_handlers import page_not_found

app.register_error_handler(404, page_not_found)

if __name__ == '__main__':
    app.run(debug=True)
