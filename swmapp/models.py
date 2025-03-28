from django.db import models

# Create your models here.
class LoginTable(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    usertype = models.CharField(max_length=20,null=True)
    status = models.IntegerField(default=0)
    
class MuncipalityReg(models.Model):
    muncipality_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    thaluk = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE) 
    def __str__(self):
         return self.muncipality_name
    # def __int__(self):
    #     return self.id
class PublicReg(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    muncipality = models.ForeignKey(MuncipalityReg,on_delete=models.CASCADE)
    village = models.CharField(max_length=100)
    contact_no = models.IntegerField(unique=True)
    rationcard_no = models.IntegerField(unique=True)
    login_id = models.OneToOneField(LoginTable,on_delete=models.CASCADE,related_name="log")
    
class HarithakarmaReg(models.Model):
    harithakarma_id = models.CharField(max_length=100,unique=True)
    muncipality = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE)


class DriverReg(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    municipality = models.ForeignKey(MuncipalityReg,on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    login_id= models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name="loginid")

class DustbinReg(models.Model):
    building_category = models.CharField(max_length=100)
    address = models.TextField()
    muncipality= models.ForeignKey(MuncipalityReg,on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,related_name='public') 
    date =  models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)
    collection_status = models.IntegerField(default=0)


class Payment(models.Model):
    card_no = models.IntegerField()
    name = models.CharField(max_length=100)
    cvv = models.IntegerField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    amount = models.IntegerField()
    dustbin_id =  models.ForeignKey(DustbinReg,on_delete=models.CASCADE)
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE) 
    date =  models.DateField(auto_now_add=True)

class Account(models.Model):
    bank_name = models.CharField( max_length=50)
    account_holder = models.CharField( max_length=50)
    card_no = models.IntegerField()
    cvv = models.IntegerField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    bank_balance = models.IntegerField()

class Public_Dustbin_Register(models.Model):
    dustbin_id= models.IntegerField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)

class WasteUpdates(models.Model):
    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE) 
    dustbin_id =  models.ForeignKey(Public_Dustbin_Register,on_delete=models.CASCADE, related_name='waste_enteries') 
    weight = models.CharField( max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    reward = models.CharField( max_length=50)

class Complaints(models.Model):
    complaints = models.CharField( max_length=100)
    login_id = models.ForeignKey(PublicReg,on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)
    reply =  models.CharField( max_length=100)

class Notifications(models.Model):
    notifications = models.CharField( max_length=100)
    login_id = models.ForeignKey(MuncipalityReg,on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)

class WasteCollection(models.Model):
    dustbin_id = models.ForeignKey(DustbinReg,on_delete=models.CASCADE) 
    harithakarma_id = models.ForeignKey(HarithakarmaReg,on_delete=models.CASCADE) 
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

 