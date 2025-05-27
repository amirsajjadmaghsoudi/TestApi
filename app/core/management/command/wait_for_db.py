"""
wait for django database tobe avalable.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
   """
   Django Command to wait for DataBase
   """
   def handle(self, *args, **options):
      pass
