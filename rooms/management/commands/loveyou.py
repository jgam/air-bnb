from django.core.management.base import BaseCommand


class Command(BaseCommand):
    print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?",)

    def handle(self, *args, **options):
        times = options.get("times")
        print(args, options)
        for i in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
        print("I love you")
