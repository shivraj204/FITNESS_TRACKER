from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_calorie_goal = models.IntegerField(default=2000)
    daily_step_goal = models.IntegerField(default=10000)
    hydration_goal = models.IntegerField(default=8)  # Glasses per day
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()  # Minutes
    calories_burned = models.IntegerField()
class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    steps = models.IntegerField(default=0)
    calories_consumed = models.IntegerField(default=0)
    water_glasses = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user.username} - {self.date}"

# Create your models here.
