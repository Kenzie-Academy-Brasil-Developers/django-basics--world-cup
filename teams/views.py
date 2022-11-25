from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def get(self, _: Request):
        teams = Team.to_list_dict()
        return Response(teams, status.HTTP_200_OK)

    def post(self, request: Request):
        try:
            newTeam: Team = Team.objects.create(**request.data)
            return Response(newTeam.to_dict(), status.HTTP_201_CREATED)
        except TypeError:
            return Response(
                {
                    "message": f"The request body has the following unknown keys: {[*request.data.keys()]}"
                },
                status.HTTP_400_BAD_REQUEST,
            )
