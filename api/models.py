from django.db import models
# from django.utils import timezone
# Create your models here.


class Project(models.Model):
    mname = models.CharField(max_length=250)
    # mtime = models.DateTimeField(default=timezone.now)
    movied = models.CharField(max_length=100000)
    moviei = models.CharField(max_length=350)
    moviet = models.CharField(max_length=250)
    dl1 = models.CharField(max_length=250)
    dl2 = models.CharField(max_length=250)

    def __str__(self):
        return self.mname
