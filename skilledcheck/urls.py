
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.storage import staticfiles_storage
from accounts.views import *


admin.site.site_header = 'SkilledCheck Admin Page'
admin.site.site_title = 'SkilledCheck'


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('', include('hub.urls')),
    path('admin/', admin.site.urls),
    path('core/', include("core.urls")),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
