from django.urls import path

from . import views

urlpatterns = [

    # pages
    path('', views.decision_page),
    path('<int:decision_index>/', views.decision_page),
    path('<int:decision_index>/save/', views.decision_save),

]
