import csv

from django.core.management.base import BaseCommand
from school.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        all_students = Student.objects.all()
        for student in all_students:
            student.teachers.add(student.teacher.id)
