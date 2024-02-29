"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from share_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('group_creation/',views.groupCreation,name="groupcreation"),
    path('main_page/',views.mainPage,name='mainpage'),
    path('show_groups/',views.showGroups,name='show_groups'),
    path('add_expenses/',views.addExpenses,name='add_expenses'),
    path('show_user_expenses/',views.showUserExpenses,name='show_user_expenses'),
    #path('about_app/',views.aboutApp,name='about_app'),
]
