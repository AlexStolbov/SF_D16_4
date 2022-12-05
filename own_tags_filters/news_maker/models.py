from django.db import models


class Maker(models.Model):
    name = models.CharField(max_length=100, default="")
    age = models.IntegerField(default=0)
    reg_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.age}'


