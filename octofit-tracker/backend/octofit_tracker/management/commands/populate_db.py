from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name, is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name, is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name, is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name, is_superhero=True)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        running = Workout.objects.create(name='Running', description='Run 5km', difficulty='medium')

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=date.today())
        Activity.objects.create(user=steve, type='cycle', duration=45, date=date.today())
        Activity.objects.create(user=bruce, type='swim', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='fly', duration=120, date=date.today())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=200, rank=1)
        Leaderboard.objects.create(user=steve, score=180, rank=2)
        Leaderboard.objects.create(user=bruce, score=170, rank=3)
        Leaderboard.objects.create(user=clark, score=160, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
