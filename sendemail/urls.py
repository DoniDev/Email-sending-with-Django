from django.urls import path
from . import views


urlpatterns = [
    path('email/',views.email_view,name='email-view'),
    path('success/',views.success_view,name='success'),

]