from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index

urlpatterns = [
    #path('signup/', signup, name='signup'),
    path('', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)