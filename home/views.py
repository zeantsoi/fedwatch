import datetime
import requests

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    today = datetime.date.today()
    past = today - datetime.timedelta(weeks=1)
    today_str, past_str = today.strftime('%Y-%m-%d'), past.strftime('%Y-%m-%d')
    url = 'https://www.federalregister.gov/api/v1/articles.json?per_page=100'
    r = requests.get(url)
    context = {'json': r.json()}
    return render(request, 'index.html', context)
