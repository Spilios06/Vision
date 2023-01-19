from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index
from .views import login

urlpatterns = [
    #path('signup/', signup, name='signup'),
    path('', index, name='index'),
    path('login/', login, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)