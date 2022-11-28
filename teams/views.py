from rest_framework.views import APIView, Request, Response, status
from .models import Team


class TeamView(APIView):
    def get(self, _: Request):
        teams = Team.to_list_dict()
        return Response(teams, status.HTTP_200_OK)

    def post(self, request: Request):
        newTeam: Team = Team.objects.create(**request.data)
        return Response(newTeam.to_dict(), status.HTTP_201_CREATED)


class TeamViewById(APIView):
    def get(self, _: Request, team_id: str):
        try:
            team = Team.objects.get(id=team_id).to_dict()
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        return Response(team, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: str):
        try:
            team = Team.objects.get(id=team_id)

        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)
        team.save()

        return Response(team.to_dict(), status.HTTP_200_OK)

    def delete(self, _: Request, team_id: str):
        try:
            person = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        person.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
