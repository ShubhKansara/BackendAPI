from django.db import models


# Create your models here.
class Role(models.Model):
    role_ID = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50)

    def __str__(self):
        return self.role_name


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    role_Id = models.ForeignKey(Role, related_name='role_Id', db_column='role_Id', on_delete=models.CASCADE)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobileNo = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    Country = models.CharField(max_length=15)
    zipCode = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#
# class staffMember(models.Model):
#     staff_id = models.AutoField(primary_key="True")
#     role_Id = models.ForeignKey(Role, related_name='role_Id', db_column='role_Id', on_delete=models.CASCADE)
#     username = models.CharField(max_length=250, unique=True)
#     password = models.CharField(max_length=250)
#     hotelName = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     mobileNo = models.CharField(max_length=15)
#     officeAddress= models.CharField(max_length=255)
#     HotelAddress= models.CharField(max_length=255)
#     city = models.CharField(max_length=15)
#     state = models.CharField(max_length=15)
#     Country = models.CharField(max_length=15)
#     zipCode = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.hotelName
#
#
# class adminMember(models.Model):
#     admin_id = models.AutoField(primary_key="True")
#     role_Id = models.ForeignKey(Role, related_name='role_Id', db_column='role_Id', on_delete=models.CASCADE)
#     username = models.CharField(max_length=250, unique=True)
#     password = models.CharField(max_length=250)
#     name = models.CharField(max_length=50)
#     mobileNo = models.CharField(max_length=15)