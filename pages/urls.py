from django.urls import path
from django.contrib import admin
#from pages.views import home,post_details,login,create,json,About,create_account


from . import views
app_name = "pages"
urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path("create/",views.create,name="create"),
    path("json/",views.json,name="json"),
    path("<int:year>/<int:month>/<int:day>/<slug:url>/",views.post_details,name="post_details"),
    path("About/", views.About , name="about"),
    path("login/create-account/",views.create_account, name='create-account'),

    # Add more URL patterns as needed
]

