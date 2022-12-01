

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  templates = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(templates.render(context, request))
def add(request):
  templates = loader.get_template('add.html')
  return HttpResponse(templates.render({}, request))
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))