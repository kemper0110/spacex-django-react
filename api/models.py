from django.db import models


class Menu(models.Model):
    class Meta:
        db_table = "menu"

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Benefit(models.Model):
    class Meta:
        db_table = "benefit"

    code = models.TextField()

    def __str__(self):
        return self.code
