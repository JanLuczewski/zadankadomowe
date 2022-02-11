from django.urls import path
from faktury.views import FakturaListView

urlpatterns = [
    path('',FakturaListView.as_view(), name='faktura'),
]