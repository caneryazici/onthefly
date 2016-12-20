from django.apps import AppConfig

from .monkey_patch import patch


class OntheflyConfig(AppConfig):
    name = 'onthelfy'
    patched = False

    def ready(self):
        if not self.patched:
            patch()
            self.patched = True
