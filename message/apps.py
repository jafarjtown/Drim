from django.apps import AppConfig


class MessagesConfig(AppConfig):
    name = 'message'

    def ready(self):
        import message.signals