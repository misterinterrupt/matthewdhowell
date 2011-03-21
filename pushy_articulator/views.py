from django.shortcuts import render_to_response
from matthewdhowell.pushy_articulator.models import PushyArticle

def index(request):
    articles = PushyArticle.objects.all()
    data = {'articles':articles}
    return render_to_response('index.html', data)