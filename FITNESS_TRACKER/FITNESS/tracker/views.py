from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from .models import Workout, DailyLog, Profile
from .forms import WorkoutForm, DailyLogForm
import json

@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()
    
    # Get or create today's log
    log, created = DailyLog.objects.get_or_create(user=user, date=today)
    
    # Fetch recent workouts and logs for charts
    workouts = Workout.objects.filter(user=user).order_by('-date')[:7]
    logs = DailyLog.objects.filter(user=user).order_by('-date')[:7]
    
    # Prepare data for Chart.js
    workout_dates = [w.date.strftime('%Y-%m-%d') for w in workouts[::-1]]
    calories_burned = [w.calories_burned for w in workouts[::-1]]
    steps_data = [l.steps for l in logs[::-1]]
    
    context = {
        'log': log,
        'workouts': workouts,
        'workout_dates': json.dumps(workout_dates),
        'calories_burned': json.dumps(calories_burned),
        'steps_data': json.dumps(steps_data),
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def log_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, 'Workout logged!')
            return redirect('dashboard')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/log_workout.html', {'form': form})

@login_required
def log_daily(request):
    if request.method == 'POST':
        form = DailyLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            messages.success(request, 'Daily log updated!')
            return redirect('dashboard')
    else:
        form = DailyLogForm()
    return render(request, 'tracker/log_daily.html', {'form': form})

@login_required
def send_reminder(request):
    user = request.user
    today = timezone.now().date()
    log = DailyLog.objects.filter(user=user, date=today).first()
    
    if not log or log.steps < 5000:  # Example condition for reminder
        send_mail(
            'Fitness Reminder',
            'Don\'t forget to log your steps and stay hydrated!',
            'your_email@gmail.com',
            [user.email],
            fail_silently=False,
        )
        messages.success(request, 'Reminder sent!')
    return redirect('dashboard')