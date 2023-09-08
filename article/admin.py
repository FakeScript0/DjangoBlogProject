from django.contrib import admin
from .models import Article,Comment#.models onu bildirirki hemin qovluqdaki fayla getdib icinden artikle gotur
# Register your models here.

"""admin.site.register(Article)"""#bunu ederek siteye article clasini importladiq
admin.site.register(Comment)
@admin.register(Article)
class AritcleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]#articles seyfesinde hansi adlar cixacaq gosterir
    list_display_links=["title","created_date"]#bu link kim gosterir artikli
    search_fields=["title"]#bununla ise neye gore axtaris eddecek onu
    list_filter=["created_date"]#bunu verdikde neye gore siralaya bilerik secenek verir filterleyir
    class Meta:#bunun Adi MUtleq meta olmalidi
        model=Article
