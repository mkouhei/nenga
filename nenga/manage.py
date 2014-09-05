#!/usr/bin/env python
""" manage.py of Nenga as Django App. """
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    from django.core.management import execute_from_command_line

    if django.VERSION > (1, 7, 0):
        django.setup()

    execute_from_command_line(sys.argv)
