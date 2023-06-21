from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model


User = get_user_model()


class MultiDBRouter:
    keep_models_in_default = ["Session", "ContentType", "User", "AdminLog"]

    def get_db(self, model, **kwargs):
        if hasattr(self, "request"):
            if (
                model.__name__ not in self.keep_models_in_default
            ):
                return self.request.session.get("DB", "default")

        return "default"

    def db_for_read(self, model, **hints):
        return self.get_db(model, **hints)

    def db_for_write(self, model, **hints):
        return self.get_db(model)

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return True

    def allow_migrate(self, *args, **kwargs):
        return True
