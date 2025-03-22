
from django.urls import path
from .views import (
    ClientListCreateView, ClientRetrieveUpdateDestroyView, 
    ProjectListCreateView, ProjectListForUserView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListCreateView.as_view(), name='project-create'),
    path('projects/', ProjectListForUserView.as_view(), name='user-projects'),
]
