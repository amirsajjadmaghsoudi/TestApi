"""
Test custome Django management command.
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopng2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTest(SimpleTestCase):
    """
    Test Command.
    """
    def Test_wait_for_db_ready(self,patched_check):
        """
        Test waiting for database if database is ready.
        """
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(database=['default'])

    @patch('time.sleep')
    def Test_wait_for_db_delay(self,patched_sleep,patched_check):
        """
        waiting for database when getting operational error.
        """
        patched_check.side_effect = [Psycopng2Error] * 2 + \
            [OperationalError] * 3 + [True]
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count,6)
        patched_check.assert_called_with(database=['default'])
