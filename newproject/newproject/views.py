from django.http import *
from django.template import *
from django.template.loader import *
from django.shortcuts import *
def hello(request):
    html = "<html><body>This is django Project</body></html>"
    return HttpResponse(html)

def temp(request):
    t = Template("<html><body>This is {{name}} singh.</body></html>")
    c = Context({'name':'vikas'})
    html = t.render(c)
    return HttpResponse(html)

def temp2(request):
    fp = open('/home/rishi/djcode/newproject/template/file.html')
    t = Template(fp.read())
    c = Context({'name':'lalit'})
    html = t.render(c)
    fp.close()
    return HttpResponse(html)

def temp3(request):
    t = get_template('file.html')
    c = Context({'name':'amit'})
    html = t.render(c)
    return HttpResponse(html)

def temp4(request):
    return render_to_response('file.html',{'name':'narender'})
