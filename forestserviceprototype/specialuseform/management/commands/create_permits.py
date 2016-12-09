#! /usr/bin/env python3
from django.core.management.base import BaseCommand, CommandError
from specialuseform.factories import PermitFactory


class Command(BaseCommand):
    help = 'Create some permits'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            action='store',
            default=5,
            help='the number of permits to create'
        )

    def handle(self, *args, **options):
        number = int(options['number'])

        PermitFactory.create_batch(number)
