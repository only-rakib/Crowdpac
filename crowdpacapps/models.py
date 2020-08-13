from django.db import models

# Create your models here.


class Endorsement_list(models.Model):
    end_pro_pic = models.CharField(max_length=70)
    end_name = models.CharField(max_length=50)
    end_status = models.CharField(max_length=10)
    end_comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.end_name


class Donar_list(models.Model):
    donar_name = models.CharField(max_length=50)
    time_ago = models.CharField(max_length=10)
    donate_amount = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.donar_name
