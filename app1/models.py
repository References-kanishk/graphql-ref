from django.db import models

# Create your models here.


class Test(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=3000)
    def __str__(self) -> str:
        return str(id)


class Test2(models.Model):
    id=models.AutoField
    test_id=models.ForeignKey(Test,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=30000)