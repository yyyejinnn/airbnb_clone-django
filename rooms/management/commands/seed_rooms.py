# python manage.py seed_rooms --number [num]
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import modes as room_models


class Command(BaseCommand):
    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many times do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity()
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))