
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Lexicon Database"
admin.site.site_title = "Lexicon Database"
admin.site.index_title = "Welcome to Lexicon Database"

urlpatterns = [
    path('', include('lexicon_database.urls')),
    path('lexicon', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


