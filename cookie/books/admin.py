from django.contrib import admin

# Register your models here.

from models import Publisher,Author,Book,Article

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Article)
