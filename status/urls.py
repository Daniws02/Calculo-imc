from django.urls import path
from status import views

urlpatterns = [
    path('', views.main),
    path('update/<int:id>/', views.update_status, name='update_status'),
    path('update/<int:id>/submit/', views.submit_update_status, name='submit_update_status'),
]