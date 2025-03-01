from django import forms
from . models import *
class MuncipalityRegister(forms.ModelForm): 

    class Meta:
        model = MuncipalityReg 
        fields = ['muncipality_name','address','city','thaluk','contact_no']
class LoginForm(forms.ModelForm): 
    class Meta:
        model = LoginTable
        fields = ['email','password']   
class PublicRegister(forms.ModelForm):
    muncipality = forms.ModelChoiceField(queryset=MuncipalityReg.objects.all(), empty_label="Select Muncipality") 
    class Meta:
        model = PublicReg
        fields = ['name','address','district','city','muncipality','village','contact_no','rationcard_no']     
 
class HarithakarmaRegister(forms.ModelForm): 
    class Meta:
        model = HarithakarmaReg
        fields = ['harithakarma_id','muncipality','contact_no']     

class DriverRegister(forms.ModelForm): 
    municipality = forms.ModelChoiceField(queryset=MuncipalityReg.objects.all(), empty_label="Select Municipality")
    class Meta:
        model = DriverReg
        fields = ['name','gender','age','municipality','contact_no']     
        

class LoginCheck(forms.Form):
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

class DustbinRegister(forms.ModelForm): 
    building = [('50','HOME'),
                ('100','OFFICE')]
    building_category = forms.ChoiceField(choices=building,widget=forms.Select())
    muncipality = forms.ModelChoiceField(queryset=MuncipalityReg.objects.all(), empty_label="Select Municipality")
    class Meta:
        model = DustbinReg
        fields = ['building_category','address','muncipality','contact_no']

class PaymentForm(forms.ModelForm): 
    
    class Meta:
        model = Payment
        fields = ['card_no','name','cvv','expiry_month','expiry_year'] 
class AccountForm(forms.ModelForm):
    class Meta:
        model =Account
        fields=['bank_name','account_holder','card_no','cvv','expiry_month','expiry_year','bank_balance']
class Public_Dustbin_Form(forms.ModelForm): 
    
    class Meta:
        model = Public_Dustbin_Register
        fields = ['dustbin_id','location'] 

class WasteUpdateForm(forms.ModelForm): 
    
    class Meta:
        model = WasteUpdates
        fields = ['weight'] 

class ComplaintForm(forms.ModelForm): 
    
    class Meta:
        model = Complaints
        fields = ['complaints'] 

class ReplyForm(forms.ModelForm): 
    
    class Meta:
        model = Complaints
        fields = ['reply'] 

class NotificationForm(forms.ModelForm): 
    
    class Meta:
        model = Notifications
        fields = ['notifications']       
    