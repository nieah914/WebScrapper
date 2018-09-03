from django.db import models


class Scrapper(models.Model):
    required_keywords = models.CharField(max_length=100, null = True)
    optional_keywords = models.CharField(max_length=100, null = True)
    except_keywords = models.CharField(max_length=1000, null = True)


class searchList(models.Model):
    testList = models.CharField(max_length=1000)