from django import models

from model_controller.models import AbstractSoftDeletionCreatedUpdatedUsernameTimestamp


class {{ camel_case_app_name }}(AbstractSoftDeletionCreatedUpdatedUsernameTimestamp):
    pass
