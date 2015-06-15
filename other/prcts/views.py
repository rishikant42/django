from django.http import HttpResponse

def home(request):
    html = "<html><body><title>HomePage</title><h2>This is home page</h2></body></html>"
    return HttpResponse(html)
