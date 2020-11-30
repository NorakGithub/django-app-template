from django import models

from model_controller.models import AbstractSoftDeletionCreatedUpdatedUsernameTimestamp


class {{ app_name|title }}(AbstractSoftDeletionCreatedUpdatedUsernameTimestamp):
    pass
