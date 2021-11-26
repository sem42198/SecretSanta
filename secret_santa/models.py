from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)

class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='participants')
    secret_santa = models.ForeignKey('Participant', on_delete=models.SET_NULL, null=True, related_name='recipient')

    class Meta:
        unique_together = ('email', 'game')

    def __str__(self):
        return self.email
