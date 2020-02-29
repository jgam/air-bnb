from django.core.management.base import BaseCommand
from django_seed import Seed
import random

from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love you?",)

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int,
                            help="How many users do you want?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(room_models.Room, number, {
            'host': lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "name": lambda x: seeder.faker.address(),
            "price": lambda x: random.randint(50, 300),
            "beds": lambda x: random.randint(0, 5),
            "bedrooms": lambda x: random.randint(0, 5),
            "baths": lambda x: random.randint(0, 5)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(
            "rooms are created successfully!"))
