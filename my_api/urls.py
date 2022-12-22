from django.urls import path
from my_api import views

urlpatterns = [
    path('advocates/', views.advocate_list, name='advocate-list'),
    path('advocates/<str:username>/', views.advocate_detail, name='advocate-detail'),
    path('companies/', views.company_list)
    ]
