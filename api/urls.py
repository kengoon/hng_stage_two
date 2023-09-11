from .views import PersonListCreateView, PersonRetrieveUpdateDeleteView
from django.urls import path


urlpatterns = [
    path("api/", PersonListCreateView.as_view()),
    path("api/<int:pk>/", PersonRetrieveUpdateDeleteView.as_view())
]
