# Requisitos: pip install django
# Import: from django.apps import AppConfig
from django.apps import AppConfig


class LearningLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learning_logs'
