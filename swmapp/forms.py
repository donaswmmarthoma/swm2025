from django import forms
from . models import *
class MuncipalityRegister(forms.ModelForm): 

    class Meta:
        model = MuncipalityReg 
        fields = ['muncipality_name','address','city','thaluk','contact_no']
        widgets = {
            'muncipality_name':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'address':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'city':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'thaluk':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'contact_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'}) 
        }
class LoginForm(forms.ModelForm): 
    class Meta:
        model = LoginTable
        fields = ['email','password'] 
        widgets ={
            'email':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'password':forms.TextInput(attrs={'class':'contact-one__form-input-box'})
        }  
class PublicRegister(forms.ModelForm):
    muncipality = forms.ModelChoiceField(queryset=MuncipalityReg.objects.all(), empty_label="Select Muncipality") 
    class Meta:
        model = PublicReg
        fields = ['name','address','district','city','muncipality','village','contact_no','rationcard_no']  
        widgets ={
            'name':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'address':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'district':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'city':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'muncipality':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'village':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'contact_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'rationcard_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),

        }   
 
class HarithakarmaRegister(forms.ModelForm): 
    class Meta:
        model = HarithakarmaReg
        fields = ['harithakarma_id','muncipality','contact_no'] 
        widgets ={
            'harithakarma_id':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'muncipality':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'contact_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
        }    

class DriverRegister(forms.ModelForm): 
    municipality = forms.ModelChoiceField(queryset=MuncipalityReg.objects.all(), empty_label="Select Municipality")
    class Meta:
        model = DriverReg
        fields = ['name','gender','age','municipality','contact_no'] 
        widgets={
            'name':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'gender':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'age':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'muncipality':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'contact_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'})
}
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
        widgets ={
            'building_category':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'address':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'muncipality':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'contact_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'}) 
        }

class PaymentForm(forms.ModelForm): 
    
    class Meta:
        model = Payment
        fields = ['card_no','name','cvv','expiry_month','expiry_year'] 
        widgets ={
            'card_no':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'name':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'cvv':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'expiry_month':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'expiry_date':forms.TextInput(attrs={'class':'contact-one__form-input-box'}) 
        }
class AccountForm(forms.ModelForm):
    class Meta:
        model =Account
        fields=['bank_name','account_holder','card_no','cvv','expiry_month','expiry_year','bank_balance']
class Public_Dustbin_Form(forms.ModelForm): 
    
    class Meta:
        model = Public_Dustbin_Register
        fields = ['dustbin_id','location'] 
        widgets ={
            'dustbin_id':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
            'location':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),
        }

class WasteUpdateForm(forms.ModelForm): 
    
    class Meta:
        model = WasteUpdates
        fields = ['weight']
        widgets = {
             'weights':forms.TextInput(attrs={'class':'contact-one__form-input-box'})}

        
class ComplaintForm(forms.ModelForm): 
    
    class Meta:
        model = Complaints
        fields = ['complaints'] 
        widgets = {
             'complaints':forms.TextInput(attrs={'class':'contact-one__form-input-box'})}

class ReplyForm(forms.ModelForm): 
    
    class Meta:
        model = Complaints
        fields = ['reply'] 
        widgets = {
             'reply':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),}

class NotificationForm(forms.ModelForm): 
    
    class Meta:
        model = Notifications
        fields = ['notifications']   
        widgets = {
             'notifications':forms.TextInput(attrs={'class':'contact-one__form-input-box'}),}    
    