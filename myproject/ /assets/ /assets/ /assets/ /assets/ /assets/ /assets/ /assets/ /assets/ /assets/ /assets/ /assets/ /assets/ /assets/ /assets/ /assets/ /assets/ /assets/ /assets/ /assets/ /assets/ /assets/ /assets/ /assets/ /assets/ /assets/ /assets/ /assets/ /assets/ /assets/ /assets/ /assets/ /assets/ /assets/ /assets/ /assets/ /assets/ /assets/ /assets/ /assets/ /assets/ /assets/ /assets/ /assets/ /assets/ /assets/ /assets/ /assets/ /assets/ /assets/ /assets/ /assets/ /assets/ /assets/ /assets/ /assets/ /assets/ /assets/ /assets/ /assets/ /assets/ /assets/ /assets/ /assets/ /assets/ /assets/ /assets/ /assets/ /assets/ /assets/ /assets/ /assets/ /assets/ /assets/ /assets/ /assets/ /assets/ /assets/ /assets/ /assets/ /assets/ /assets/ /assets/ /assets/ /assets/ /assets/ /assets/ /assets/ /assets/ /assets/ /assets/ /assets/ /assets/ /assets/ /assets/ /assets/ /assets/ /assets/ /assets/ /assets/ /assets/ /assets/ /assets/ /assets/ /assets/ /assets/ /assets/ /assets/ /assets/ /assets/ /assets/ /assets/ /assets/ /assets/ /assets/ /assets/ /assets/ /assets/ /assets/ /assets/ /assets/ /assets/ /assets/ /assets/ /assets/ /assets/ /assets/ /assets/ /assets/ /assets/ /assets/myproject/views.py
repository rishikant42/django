from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def time(request):
    now = datetime.datetime.now()
    return render_to_response("ct2.html",{'current_date':now})

def future(request,offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('ft2.html')
    c = Context({'hour_offset':offset, 'next_time':dt})
    html = t.render(c)
    return HttpResponse(html)
