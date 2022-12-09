from django.urls import path

from CentralizedTicketSystem.tickets.views import all_data

urlpatterns = (
    path('data/', all_data, name='all data'),
)
