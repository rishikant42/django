from django.shortcuts import render
from django.http import *
from django.shortcuts import *
from models import Article
from forms import ArticleForm
from django.core.context_processors import csrf
from django.db.models import Q
# Create your views here.

def new(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def articles(request):
    return render_to_response('articles.html', {'articles':Article.objects.all() })

def article(request, article_id=1):
    return render_to_response('article.html',
                             {'article':Article.objects.get(id=article_id) })

def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/article/get/%s' %article_id)

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/article/all')
    else:
        form = ArticleForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html',args)

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) 
 		)
        results = Article.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html", {"results": results,"query": query})


def search_titles(request):
    if request.method == "POST":
	search_text = request.POST['search_text']
    else:
	search_text = ''

    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html', {'articles':articles})



