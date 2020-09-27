from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Player(models.Model):
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.x_position)