from django.urls import path
from .views import TeamView, TeamsDetailView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<team_id>/", TeamsDetailView.as_view()),
]
