from django.core.management.base import BaseCommand, CommandError
from analytics.models import Click

class Command(BaseCommand):
    help = 'Refreshes shorturls for all urls'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return Click.objects.reset_all_counts()