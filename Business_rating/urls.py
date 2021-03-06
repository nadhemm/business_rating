"""Business_rating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from Business_rating import views, settings

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('search/', views.SearchAPI.as_view(), name='search-api'),
    path('business-details/', views.BusinessDetailsAPI.as_view(), name='business-details'),
    path('add-business/', views.AddBusinessAPI.as_view(), name='add-business'),
    path('review-business/', views.ReviewBusinessAPI.as_view(), name='review-business'),
    path('businesses-list/', views.BusinessesListAPI.as_view(), name='businesses-list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
