"""
URL configuration for crudproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from crudapp import views
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rename/',views.Renameclass.as_view()),
    path('getnamedetail/',views.Getnamedetails.as_view()),
    path('getnamebusiness/',views.Getnamebusiness.as_view()),
    path('postdetail/',views.Postdetail.as_view()),
    path('postmasonite/',views.GetMasonite.as_view()),
    path('getbusiness/',views.Getbusiness.as_view()),
    path('listview/',views.Listview.as_view()),
    path('retrieveview/<int:pk>',views.Retrieveview.as_view()),
    path('updateview/<int:pk>',views.Updateview.as_view()),
    path('createview/',views.Createview.as_view()),
    path('deleteview/<int:pk>',views.Deleteview.as_view()),
    path('date/',views.Date.as_view()),
    path('bill/',views.Bill.as_view()),
    path('Avg/', views.Average.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
