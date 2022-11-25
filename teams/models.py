from django.db import models
from django.forms.models import model_to_dict


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(default=0, null=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    founded_at = models.DateField(null=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"

    def to_dict(self) -> dict:
        return model_to_dict(self)

    @classmethod
    def to_list_dict(cls) -> list[dict]:
        teams = cls.objects.all()

        teams_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return teams_list
