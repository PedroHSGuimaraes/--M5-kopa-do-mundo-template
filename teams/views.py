from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from .models import Team
from utils import data_processing


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        teams_list = [model_to_dict(team) for team in teams]
        return Response(teams_list, status=status.HTTP_200_OK)

    def post(self, request):
        test_data = data_processing(**request.data)

        if test_data:
            return Response(test_data, status=status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status=status.HTTP_201_CREATED)


class TeamsDetailView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        team_dict = model_to_dict(team)
        return Response(team_dict, status=status.HTTP_200_OK)

    def patch(self, request, team_id):
        team = Team.objects.filter(id=team_id)

        if not team:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        team.update(**request.data)
        team_updated = model_to_dict(Team.objects.get(id=team_id))
        return Response(team_updated, status=status.HTTP_200_OK)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response(
                {"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND
            )

        team.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
