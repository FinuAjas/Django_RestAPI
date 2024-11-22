from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  
        return self.name
    
class UserDetails(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, default=None)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name