from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel')
        self.assertEqual(user.email, 'test@hero.com')
        self.assertEqual(user.name, 'Test Hero')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', type='Running', duration=30)
        self.assertEqual(activity.user, 'Test Hero')
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Avengers', points=100)
        self.assertEqual(lb.team, 'Avengers')
        self.assertEqual(lb.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Hero HIIT', difficulty='Hard')
        self.assertEqual(workout.name, 'Hero HIIT')
        self.assertEqual(workout.difficulty, 'Hard')
