from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango import mycalendar

# Create your views here.
def index(request):
    c = mycalendar.HTMLCalendar(2014)
    s = c.printmonth(3, True)
    context = RequestContext(request)
    context_dict = {'boldmessage': 'Jump'}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': 'Run!'}
    return render_to_response('rango/about.html', context_dict, context)
