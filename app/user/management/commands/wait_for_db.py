"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Custom Django management command to wait for the database to be available.

    Usage: python manage.py wait_for_db
    """

    def handle(self, *args, **options):
        """
        Handle method for the 'wait_for_db' command.

        This method continuously checks if the database is available.
        If the database is not available, it waits for 1 second and retries until successful.

        Parameters:
        - args: Command line arguments (not used in this command).
        - options: Command options (not used in this command).
        """
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
