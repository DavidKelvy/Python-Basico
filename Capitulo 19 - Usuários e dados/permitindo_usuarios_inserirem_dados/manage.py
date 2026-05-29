#!/usr/bin/env python
"""Utilitário de linha de comando do Django para tarefas administrativas."""
import os
import sys


def main():
    """Execute tarefas administrativas."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')
    try:
# Requisitos: pip install django
# Import: from django.core.management import execute_from_command_line
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
