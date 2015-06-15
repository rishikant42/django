from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def current_datetime(request):
    now = datetime.datetime.now()
    fp = open('/home/rishi/djcode/mysite/templates/current_datetime.html')
    t = Template(fp.read())
    c = Context({'current_date':now})
    html = t.render(c)
    fp.close()
    return HttpResponse(html)

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('futuretime.html',{'hour_offset':offset, 'next_time':dt})
    

def my_view(request,month,day):
    html = "You have no data on %s %s" %(month,day)
    return HttpResponse(html)
