from django.urls import path
from .views import TeamView, TeamViewById

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<team_id>", TeamViewById.as_view()),
]
