from django.urls import path
from . import views

urlpatterns = [
    
    # auth
    path('login/', views.login),
    path('logout/', views.logout),
    
    # registration
    path('sign_up/', views.sign_up),

    # password
    path('password_change/', views.password_change),
    path('password_confirm/', views.password_confirm),
    path('password_forgot/', views.password_forgot),
    path('password_reset/', views.password_reset),

]
