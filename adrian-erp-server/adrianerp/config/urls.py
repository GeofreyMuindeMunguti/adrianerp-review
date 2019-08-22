from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('user.urls')),
    url(r'^chats/', include('chat.urls')),
    url(r'^mailservers/', include('emailserver.urls')),
    url(r'^emails/', include('sentmail.urls')),
    url(r'^reports/', include('reports.urls')),
]
