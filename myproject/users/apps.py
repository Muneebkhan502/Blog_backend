from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals  #Django does not automatically know that you want to run the code in signals.py.

                          #So, you have to manually import your signals.py file when the app is ready, to connect the signals.


