
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.static import serve
from yykt import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)