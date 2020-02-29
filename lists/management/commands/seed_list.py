from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
import random

from lists import models as list_models
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love you?",)

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int,
                            help=f"How many {NAME} do you want?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List, number, {

                "user": lambda x: random.choice(users),

            }
        )

        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5): random.randint(6, 30)]
            # this will be a querset and I want elements inside of the queryset
            list_model.rooms.add(*to_add)

        self.stdout.write(self.style.SUCCESS(
            f"{NAME} are created successfully!"))
