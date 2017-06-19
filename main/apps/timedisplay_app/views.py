from django.shortcuts import render, HttpResponse
from django.utils import timezone
import datetime

# Create your views here.

def index(request):
    print "Time Display"
    request.session['now'] = timezone.localtime(timezone.now()).strftime("%b %d, %Y at %I:%M %p")
    now=request.session['now']

    return render(request, 'timedisplay_app/index.html')


