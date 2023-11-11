from django.db import models


class SomeModel(models.Model):
    some_field = models.CharField(max_length=100)


class SomeOtherModel(models.Model):
    another_field = models.CharField(max_length=100)


class AnotherModel(models.Model):
    one_more_field = models.CharField(max_length=100)
