from django.db import models
from django.contrib.auth.models import User


class SchoolManagement(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    school_name  = models.CharField(max_length =100,blank =True)
    dise_code  = models.CharField(max_length =100,blank =True)
    address  = models.CharField(max_length =100,blank =True)
    school_type  = models.CharField(max_length =100,blank =True)


    def __str__(self):
        return self.school_name



class StudentDetail(models.Model):
    school = models.ForeignKey(SchoolManagement,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length =20,blank =True)
    last_name  = models.CharField(max_length =20,blank =True)
    father_name  = models.CharField(max_length =20,blank =True)
    student_class  = models.CharField(max_length =20,blank =True)
    roll_no  = models.IntegerField(null =True)
    student_type  = models.CharField(max_length =30,blank =True)
    address  = models.CharField(max_length =100,blank =True)


    def __str__(self):
        return f' MR. {self.first_name}  {self.last_name} class - {self.student_class} '
    