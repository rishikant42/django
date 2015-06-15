from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from models import Book,Publisher
from forms import ContactForm
from django.core.mail import send_mail
from django.template import loader, Context
import csv
from reportlab.pdfgen import canvas
from cStringIO import StringIO
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import gettext
# Create your views here.

def new(request):
    html = "<html><body><h2>This is book data</h2></body></html>"
    return HttpResponse(html)

def search(request):
    query = request.GET.get('q', '')
    if query:
	qset = (
	    Q(title__icontains=query) 
#	    Q(authors__first_name__icontains=query) |
#	    Q(authors__last_name__icontains=query)
	)
	results = Book.objects.filter(qset).distinct()
    else:
	results = []
    return render_to_response("search.html", {"results": results,"query": query})


def contact(request):
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
	    topic = form.clean_data['topic']
	    message = form.clean_data['message']
	    sender = form.clean_data.get('sender', 'noreply@example.com')
	    send_mail(
		'Feedback from your site, topic: %s' % topic,
		message, sender,
		['administrator@example.com']
		)
	    return HttpResponseRedirect('/contact/thanks/')


    else:
        form = ContactForm()
    return render_to_response('contact.html',{'form':form})


#def my_image(request):
#    image_data = open("/home/rishi/rk.png", "rb").read()
#    return HttpResponse(image_data, mimetype="image/png")


UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]

def unruly_passengers_csv(request):
# Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse()#mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'
# Create the CSV writer using the HttpResponse as the "file"
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
	writer.writerow([year, num])
    return response



def hello_pdf(request):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment, filename=my.pdf'
    
    p = canvas.Canvas(response)
    p.drawString(100, 100, "this is self created pdf file")
    p.showPage()
    p.save()
    return response

def new_pdf(request):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment, filename=self.pdf'

    temp = StringIO()

    p = canvas.Canvas(temp)

    p.drawString(100, 100, "Hello This is my pdf file.")
    p.showPage()
    p.save()

    response.write(temp.getvalue())
    return response
   


