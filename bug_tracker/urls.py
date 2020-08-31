"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from homepage.views import assign_user_to_ticket
from homepage.views import create_ticket_view
from homepage.views import edit_ticket_view
from homepage.views import homepage_view
from homepage.views import login_view
from homepage.views import logout_view
from homepage.views import mark_ticket_done
from homepage.views import mark_ticket_invalid
from homepage.views import ticket_detail
from homepage.views import user_detail_view

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('', homepage_view, name='homepage'),
    path('create_ticket/', create_ticket_view, name='create_ticket_view'),
    path('ticket/<int:ticket_id>', ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/assign',
         assign_user_to_ticket, name='assign_user_to_ticket'),
    path('ticket/<int:ticket_id>/invalid',
         mark_ticket_invalid, name='mark_ticket_invalid'),
    path('ticket/<int:ticket_id>/done',
         mark_ticket_done, name='mark_ticket_done'),
    path('ticket/<int:ticket_id>/edit',
         edit_ticket_view, name='edit_ticket_view'),
    path('user/<int:user_id>/', user_detail_view, name='user_detail_view'),
    path('admin/', admin.site.urls),
]
