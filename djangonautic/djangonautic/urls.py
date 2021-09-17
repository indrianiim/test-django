from django import urls
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from rest_framework.authtoken.views import obtain_auth_token
from api.views import TestView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path('home/', article_views.index, name="home"),
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)