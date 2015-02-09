import datetime
import requests

from django.shortcuts import render
from django.http import HttpResponse

from api.models import Keyword

# Create your views here.
def index(request):
    today = datetime.date.today()
    past = today - datetime.timedelta(weeks=1)
    today_str, past_str = today.strftime('%Y-%m-%d'), past.strftime('%Y-%m-%d')
    
    keywords = Keyword.objects.all()
    keywords_list = []
    for keyword in keywords:
        keywords_list.append('"' + keyword.keyword + '"')

    keywords_str = ('|').join(keywords_list)

    url = 'http://www.federalregister.gov/api/v1/articles.json?per_page=100&order=relevance&conditions%%5Bterm%%5D=%s&conditions%%5Bpublication_date%%5D%%5Bgte%%5D=%s&conditions%%5Bpublication_date%%5D%%5Blte%%5D=%s' % (keywords_str, past_str, today_str)
    r = requests.get(url)

    context = {'json': r.json(),
               'start_date': past_str,
               'end_date': today_str,
               'keywords': keywords}
    return render(request, 'index.html', context)
