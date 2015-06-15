from django.shortcuts import render
from django.http import *
# Create your views here.

def test(request):
    html = ("<html><body>This is django app file</body></html>")
    return HttpResponse(html)
