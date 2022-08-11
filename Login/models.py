from django.db import models

class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField(max_length=255,null=False)
    password = models.TextField(max_length=255,null=False)
    building_id = models.IntegerField()
    type_user = models.IntegerField()