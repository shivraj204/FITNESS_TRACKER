from django import forms
from .models import Workout, DailyLog

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'activity', 'duration', 'calories_burned']

class DailyLogForm(forms.ModelForm):
    class Meta:
        model = DailyLog
        fields = ['date', 'steps', 'calories_consumed', 'water_glasses']