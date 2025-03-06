from django.shortcuts import render,redirect,get_object_or_404
from . forms import *
from . models import *
from django.db.models import Q
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def login(request):
    if request.method == 'POST':
        loginform = LoginCheck(request.POST)
        if loginform.is_valid():
            email=loginform.cleaned_data['email']
            password=loginform.cleaned_data['password']
            try:
                user=LoginTable.objects.get(email=email)
                print('hii')
                if user.password == password:
                    print('hii2')
                    if user.usertype == 'muncipality':
                        request.session['muncipalityid'] = user.id
                        return redirect('muncipality_home')
                    elif user.usertype == 'harithakarma':
                        request.session['harithakarmaid'] = user.id
                        return redirect('harithakarma_home')
                    elif user.usertype == 'public':
                        request.session['publicid'] = user.id
                        return redirect('usertemplate')
                    elif user.usertype == 'driver':
                        request.session['driverid'] = user.id
                        return redirect('driver_home')
                    else :
                        messages.error(request,'Unknown user')
                else:
                    messages.error(request,'invalid credencials')
            except user.DoesNotExist:
                messages.error(request,'user doestnot exist')
    else :
        loginform = LoginCheck()
    return render(request, 'login.html',{'loginform':loginform})
def home(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin.html')
def usertemplate(request):
    return render(request, 'usertemplate.html')
def muncipality_home(request):
    return render(request, 'muncipalityhome.html')
def harithakarma_home(request):
    return render(request, 'harithakarmahome.html')
def driver_home(request):
    return render(request, 'driverhome.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')

def Muncipality_Reg(request,):
    if request.method == 'POST':
        form = MuncipalityRegister(request.POST)
        loginform = LoginForm(request.POST)
        if form.is_valid() and loginform.is_valid():
            logindata = loginform.save(commit=False)
            logindata.usertype='muncipality'
            logindata.save()
            data = form.save(commit=False)
            data.login_id = logindata
            data.save()
            return redirect('/')
    else:    
        form = MuncipalityRegister()
        loginform = LoginForm()
    return render(request, 'muncipal_reg.html',{'form':form,'loginform':loginform})


def Public_Reg(request):
    if request.method == 'POST':
        publicform = PublicRegister(request.POST)
        loginform = LoginForm(request.POST)
        if publicform.is_valid() and loginform.is_valid():
            # Get the selected municipality (MuncipalityReg instance)
            mundata = publicform.cleaned_data['muncipality']  # This is a MuncipalityReg instance
            print(mundata)
            
            # Create a new LoginTable instance for the public user
            logindata = loginform.save(commit=False)
            logindata.usertype = 'public'
            logindata.save()
            
            # Get the LoginTable instance associated with the selected MuncipalityReg
             # This is the LoginTable instance associated with the selected MuncipalityReg
            print(mundata)
            
            # Create the new PublicReg instance but do not save yet
            data = publicform.save(commit=False)
            data.login_id = logindata  # Assign the newly created user's login ID
            
            # Assign the LoginTable instance (not MuncipalityReg) to the muncipality field
            data.muncipality = mundata  # Assign LoginTable instance
            
            data.save()  # Save the PublicReg instance
            
            return redirect('/')
    else:
        publicform = PublicRegister()
        loginform = LoginForm()
    
    return render(request, 'public_reg.html', {'publicform': publicform, 'loginform': loginform})

def Harithakarma_Reg(request,):
    if request.method == 'POST':
        harithakarmaform = HarithakarmaRegister(request.POST)
        loginform = LoginForm(request.POST)
        if harithakarmaform.is_valid() and loginform.is_valid():
            logindata = loginform.save(commit=False)
            logindata.usertype='harithakarma'
            logindata.save()
            data = harithakarmaform.save(commit=False)
            data.login_id = logindata
            data.save()
            return redirect('/')
    else:    
        harithakarmaform = HarithakarmaRegister()
        loginform = LoginForm()
    return render(request, 'harithakarma_reg.html',{'harithakarmaform':harithakarmaform,'loginform':loginform})
def Driver_Reg(request):
    if request.method == 'POST':
        driverform = DriverRegister(request.POST)
        loginform = LoginForm(request.POST)
        if driverform.is_valid() and loginform.is_valid():
            logindata = loginform.save(commit=False)
            logindata.usertype='driver'
            logindata.save()
            mundata=driverform.cleaned_data['municipality']
            mun=mundata.login_id
            data = driverform.save(commit=False)
            data.login_id = logindata
            data.municipality=mundata
            data.save()
            return redirect('/')
    else:    
        driverform = DriverRegister()
        loginform = LoginForm()
    return render(request, 'driver_reg.html',{'driverform':driverform,'loginform':loginform})
def muncipality_adminview(request):
    adminview = MuncipalityReg.objects.all()
    return render(request, 'muncipality_adminview.html', {'muncipality_adminview':adminview}) 

def admin_muncipality_accept(request,id):
    accept = get_object_or_404(LoginTable,id=id)
    accept.status = 1
    accept.save()
    return redirect('muncipality_adminview')

def admin_muncipality_reject(request,id):
    reject = get_object_or_404(LoginTable,id=id)
    reject.status = 2
    reject.save()
    return redirect('muncipality_adminview')


def public_adminview(request):
    adminview = PublicReg.objects.all()
    return render(request, 'public_adminview.html', {'public_adminview':adminview}) 
def harithakarma_adminview(request):
    adminview = HarithakarmaReg.objects.all()
    return render(request, 'harithakarma_adminview.html', {'harithakarma_adminview':adminview}) 

def admin_harithakarma_accept(request,id):
    accept = get_object_or_404(LoginTable,id=id)
    accept.status = 1
    accept.save()
    return redirect('harithakarma_adminview')

def admin_harithakarma_reject(request,id):
    reject = get_object_or_404(LoginTable,id=id)
    reject.status = 2
    reject.save()
    return redirect('harithakarma_adminview')

def driver_adminview(request):
    adminview = DriverReg.objects.all()
    return render(request, 'driver_adminview.html', {'driver_adminview':adminview}) 


def admin_driver_accept(request,id):
    accept = get_object_or_404(LoginTable,id=id)
    accept.status = 1
    accept.save()
    return redirect('driver_adminview')

def admin_driver_reject(request,id):
    reject = get_object_or_404(LoginTable,id=id)
    reject.status = 2
    reject.save()
    return redirect('driver_adminview')


    
def public_update(request):
    id=request.session.get('publicid')
    logindata=get_object_or_404(LoginTable,id=id)
    data = get_object_or_404(PublicReg, login_id=logindata)
    print(data)
    if request.method == 'POST':
        updateform = PublicRegister(request.POST, instance=data)
        logform = LoginForm(request.POST, instance=logindata)
        if updateform.is_valid() and logform.is_valid():
            updateform.save()
            logform.save()
            return redirect('usertemplate')
    else:    
        updateform = PublicRegister(instance=data)
        logform = LoginForm(instance=logindata)
    return render(request, 'public_update.html',{'updateform':updateform,'logform':logform})

def muncipality_update(request):
    id=request.session.get('muncipalityid')
    logindata=get_object_or_404(LoginTable,id=id)
    data = get_object_or_404(MuncipalityReg, login_id=logindata)
    print(data)
    if request.method == 'POST':
        updateform = MuncipalityRegister(request.POST, instance=data)
        logform = LoginForm(request.POST, instance=logindata)
        if updateform.is_valid() and logform.is_valid():
            updateform.save()
            logform.save()
            return redirect('muncipality_home')
    else:    
        updateform = MuncipalityRegister(instance=data)
        logform = LoginForm(instance=logindata)
    return render(request, 'muncipality_update.html',{'updateform':updateform,'logform':logform})

def harithakarma_update(request):
    id=request.session.get('harithakarmaid')
    logindata=get_object_or_404(LoginTable,id=id)
    data = get_object_or_404(HarithakarmaReg, login_id=logindata)
    print(data)
    if request.method == 'POST':
        updateform = HarithakarmaRegister(request.POST, instance=data)
        logform = LoginForm(request.POST, instance=logindata)
        if updateform.is_valid() and logform.is_valid():
            updateform.save()
            logform.save()
            return redirect('harithakarma_home')
    else:    
        updateform = HarithakarmaRegister(instance=data)
        logform = LoginForm(instance=logindata)
    return render(request, 'harithakarma_update.html',{'updateform':updateform,'logform':logform})

def driver_update(request):
    id=request.session.get('driverid')
    logindata=get_object_or_404(LoginTable,id=id)
    data = get_object_or_404(DriverReg, login_id=logindata)
    print(data)
    if request.method == 'POST':
        updateform = DriverRegister(request.POST, instance=data)
        logform = LoginForm(request.POST, instance=logindata)
        if updateform.is_valid() and logform.is_valid():
            updateform.save()
            logform.save()
            return redirect('driver_home')
    else:    
        updateform = DriverRegister(instance=data)
        logform = LoginForm(instance=logindata)
    return render(request, 'driver_update.html',{'updateform':updateform,'logform':logform})

def driver_muncipality_view(request):
    login_id = request.session.get('muncipalityid')

    if not login_id:
        return render(request, 'driver_muncipality_view.html', {'error': 'You are not logged in as a municipality.'})

    try:
        # Fetch the MuncipalityReg object associated with the login_id
        municipalitydata = MuncipalityReg.objects.get(login_id__id=login_id)

        # Fetch all PublicReg objects associated with the municipality
        driverdata = DriverReg.objects.filter(municipality=municipalitydata)

        return render(request, 'driver_muncipality_view.html', {'driver_muncipality_view': driverdata})
    except MuncipalityReg.DoesNotExist:
        return render(request, 'driver_muncipality_view.html', {'error': 'Municipality not found.'})
    # id=request.session.get('muncipalityid')
    # # logindata=get_object_or_404(LoginTable,id=id)
    # # muncipalitydata = MuncipalityReg.objects.get(login_id=id)
    # driverdata = DriverReg.objects.filter(municipality=id)
    # print(driverdata)
    # return render(request, 'driver_muncipality_view.html', {'driver_muncipality_view':driver_muncipality_view}) 
# def muncipality_user_view(request):
#     login_id = request.session.get('muncipalityid')
    
#     # Fetch the municipality based on the login_id in the session
#     muncipalitydata = get_object_or_404(MuncipalityReg, login_id=login_id)

#     # Fetch all PublicReg objects that are related to the municipality
#     publicdata = PublicReg.objects.filter(muncipality=muncipalitydata)
#     return render(request, 'muncipality_user_view.html',{'muncipality_user_view':publicdata}) 

def muncipality_user_view(request):
    # Get the login_id from the session
    login_id = request.session.get('muncipalityid')

    if not login_id:
        return render(request, 'muncipality_user_view.html', {'error': 'You are not logged in as a municipality.'})

    try:
        # Fetch the MuncipalityReg object associated with the login_id
        muncipalitydata = MuncipalityReg.objects.get(login_id__id=login_id)

        # Fetch all PublicReg objects associated with the municipality
        publicdata = PublicReg.objects.filter(muncipality=muncipalitydata)

        return render(request, 'muncipality_user_view.html', {'muncipality_user_view': publicdata})
    except MuncipalityReg.DoesNotExist:
        return render(request, 'muncipality_user_view.html', {'error': 'Municipality not found.'})

    # except MuncipalityReg.DoesNotExist:
    # return render(request, 'muncipality_user_view.html', {'error': 'Municipality not found.'})

def Dustbin_Reg(request):
    id=request.session.get('publicid')
    data=get_object_or_404(LoginTable,id=id)
    print(data)
    if request.method == 'POST':
        dustbinform = DustbinRegister(request.POST)
        # print(amnt)
        if dustbinform.is_valid():
            
            logindata = dustbinform.save(commit=False)
            logindata.login_id = data
            logindata.save()
            print(logindata)
            dustbinkey=logindata.id
            amount=logindata.building_category
            print(amount)
            
            return redirect('payment',logindata=dustbinkey,amount=amount)
    else:    
        dustbinform = DustbinRegister()
    return render(request, 'dustbin.html',{'dustbinform':dustbinform})

def payment(request,logindata,amount):
    amount=int(amount)
    id=request.session.get('publicid')
    dustbindata=get_object_or_404(DustbinReg,id=logindata)
    data=get_object_or_404(LoginTable,id=id)
    if request.method == 'POST':
        # print("dataaaaa....")
        paymentform = PaymentForm(request.POST)
        if paymentform.is_valid():
            
           data1 = paymentform.save(commit=False)
           data1.dustbin_id = dustbindata
           data1.login_id=data
           data1.amount = amount
           dustbindata.status = 1
           data1.save()
           dustbindata.save()
           return redirect('apply_dustbin')
    else:    
        paymentform = PaymentForm()
        dis = DustbinRegister()
    return render(request,'payment.html',{'paymentform':paymentform,'amt':amount})

def muncipality_payment_view(request):
    login_id = request.session.get('muncipalityid')
    logid = get_object_or_404(LoginTable,id = login_id)
    mun = get_object_or_404(MuncipalityReg,login_id = login_id)
  
    if not login_id:
        return render(request, 'muncipality_payment_view.html', {'error': 'You are not logged in as a municipality.'})

    try:
        # data = PublicReg.objects.filter(muncipality=mun)
        publicdata = DustbinReg.objects.filter(muncipality=mun,status = 1).select_related('login_id__log')

        return render(request, 'muncipality_payment_view.html', {'muncipality_payment_view': publicdata})
    except MuncipalityReg.DoesNotExist:
        return render(request, 'muncipality_payment_view.html', {'error': 'Municipality not found.'})

def account(request):
    if request.method == 'POST':
        accountform = AccountForm(request.POST)
        # loginform = LoginForm(request.POST)
        if accountform.is_valid():
           
            data = accountform.save(commit=False)
            data.save()
            return redirect('/')
    else:    
        accountform = AccountForm()
        # loginform = LoginForm()
    return render(request, 'account.html',{'accountform':accountform})

def dustbin_user_view(request):
   
    login_id = request.session.get('publicid')

    if not login_id:
        return render(request, 'dustbin_user_view.html', {'error': 'You are not logged in as a user.'})

    try:
        data = DustbinReg.objects.filter(login_id_id=login_id)

        publicdata = PublicReg.objects.filter(login_id_id=login_id)

        return render(request, 'dustbin_user_view.html', {'dustbin_user_view': data})
    except DustbinReg.DoesNotExist:
        return render(request, 'dustbin_user_view.html', {'error': 'user not found.'})

def dustbin_update(request,id):
    data = get_object_or_404(DustbinReg,id=id)
    # print(data)
    if request.method == 'POST':
        updateform = DustbinRegister(request.POST,instance=data)
      
        if updateform.is_valid():
            updateform.save()
            
            return redirect('dustbin_user_view')
    else:    
        updateform = DustbinRegister(instance=data)
       
    return render(request, 'dustbin_details_update.html',{'updateform':updateform})

def dustbin_details_delete(request, id):
    data = get_object_or_404(DustbinReg,id=id)
    data.delete()
    return redirect('dustbin_user_view')

def Public_Dustbin_Reg(request):
    id=request.session.get('muncipalityid')
    data=get_object_or_404(LoginTable,id=id)
    print(data)
    if request.method == 'POST':
        public_dustbin_form = Public_Dustbin_Form(request.POST)
        if public_dustbin_form.is_valid():
            dustbindata = public_dustbin_form.save(commit=False)
            dustbindata.login_id = data
            dustbindata.save()
            return redirect('muncipality_home')
    else:    
        public_dustbin_form = Public_Dustbin_Form()
    return render(request, 'public_dustbin_reg.html',{'public_dustbinform':public_dustbin_form})

def public_dustbin_view(request):
    login_id = request.session.get('muncipalityid')

    if not login_id:
        return render(request, 'public_dustbin_view.html', {'error': 'You are not logged in as a municipality.'})

    try:
        # Fetch the MuncipalityReg object associated with the login_id
        municipalitydata = MuncipalityReg.objects.get(login_id__id=login_id)

        # Fetch all PublicReg objects associated with the municipality
        dustbindata = Public_Dustbin_Register.objects.all()

        return render(request, 'public_dustbin_view.html', {'public_dustbin_view': dustbindata})
    except MuncipalityReg.DoesNotExist:
        return render(request, 'public_dustbin_view.html', {'error': 'Municipality not found.'})

def public_dustbin_update(request,id):
    data = get_object_or_404(Public_Dustbin_Register,id=id)
    # print(data)
    if request.method == 'POST':
        updateform = Public_Dustbin_Form(request.POST,instance=data)
      
        if updateform.is_valid():
            updateform.save()
            
            return redirect('public_dustbin_view')
    else:    
        updateform = Public_Dustbin_Form(instance=data)
       
    return render(request, 'public_dustbin_update.html',{'updateform':updateform})

def public_dustbin_delete(request, id):
    data = get_object_or_404(Public_Dustbin_Register,id=id)
    data.delete()
    return redirect('public_dustbin_view')


def dustbin_public_search(request):
    search = request.GET.get('search')
    if search:
        dustbindata = Public_Dustbin_Register.objects.filter(Q(location__icontains=search) | Q(dustbin_id__icontains=search))
    else:
        dustbindata = Public_Dustbin_Register.objects.all()
    return render(request, 'dustbin_public_search.html', {'dustbin_public_search': dustbindata})

def wasteupdates(request, id):
    logid = request.session.get('publicid')
    data = get_object_or_404(LoginTable, id=logid)
    
    dustid = id  # Dustbin ID is passed from the URL parameter
    dustbin = get_object_or_404(Public_Dustbin_Register, id=dustid)
    
    print(data)  # Debugging purpose
    
    # Set a point value per unit of weight (adjust this as necessary)
    point_per_kg = 1  # Change this value based on your reward system
    
    if request.method == 'POST':
        form = WasteUpdateForm(request.POST)
        
        if form.is_valid():
            wastedata = form.save(commit=False)
            
            # Get the weight from the form
            weight = form.cleaned_data['weight']
            
            # Calculate reward (points) based on weight
            reward_points = weight * point_per_kg  # Calculate reward points based on the weight
            # print('points',reward_points)
            wastedata.reward = reward_points  # Save the reward points to the WasteData instance (make sure you have a field for this)
            
            wastedata.login_id = data  # Associate the waste data with the current user
            wastedata.dustbin_id = dustbin  # Associate the waste data with the selected dustbin
            wastedata.save()  # Save the waste data

            return redirect('dustbin_public_search')  # Redirect after saving the data
        
    else:
        form = WasteUpdateForm()

    return render(request, 'wastebox.html', {'form': form})

def totalwaste(request,id):

    dustbin = get_object_or_404(Public_Dustbin_Register, id=id)  
    waste_entries = WasteUpdates.objects.filter(dustbin_id=dustbin)

  
    total_waste = waste_entries.aggregate(total=Sum('weight'))['total'] or 0
    rewards = waste_entries.aggregate(total=Sum('reward'))['total'] or 0
    last_entry = waste_entries.order_by('-date').first()
    last_waste_kg = last_entry.weight if last_entry else 0

    context = {            
        'total_waste': total_waste,
        'last_waste_kg': last_waste_kg,
        'rewards': rewards,
  }
    return render(request, 'totalwaste.html', context)

def muncipality_waste_notifications(request):
    # Retrieve the logged-in municipality from session
    login_id = request.session.get('muncipalityid')
    logdata = get_object_or_404(LoginTable, id=login_id)
    
    # Get all dustbins associated with the logged-in municipality
    dustbins = Public_Dustbin_Register.objects.filter(login_id=logdata)

    notifications = []

    for dustbin in dustbins:
        # Get all waste entries for this dustbin and calculate the total weight
        waste_entries = WasteUpdates.objects.filter(dustbin_id=dustbin)
        
        # Convert the weight into a numeric value and sum it up
        total_weight = waste_entries.aggregate(Sum('weight'))['weight__sum']
        
        if total_weight is None:
            total_weight = 0  # In case there are no waste entries yet

        # Check if the total weight has reached 100kg
        if total_weight >= 100:
            notifications.append(f"Alert: The total weight of waste in dustbin {dustbin.dustbin_id} has reached 100kg.")
    
    context = {
        'dustbins': dustbins,
        'notifications': notifications,
    }

    return render(request, 'muncipality_waste_notification.html', context)

def dustbin_harithakarma_search(request):
    search = request.GET.get('search')
    if search:
        dustbindata = Public_Dustbin_Register.objects.filter(
            Q(location__icontains=search) | Q(dustbin_id__icontains=search)
        )
    else:
        dustbindata = Public_Dustbin_Register.objects.all()
    
    return render(request, 'dustbin_harithakarma_search.html', {'dustbin_harithakarma_search': dustbindata})

def dustbin_driver_search(request):
    search = request.GET.get('search')
    if search:
        dustbindata = Public_Dustbin_Register.objects.filter(
            Q(location__icontains=search) | Q(dustbin_id__icontains=search)
        )
    else:
        dustbindata = Public_Dustbin_Register.objects.all()
    
    return render(request, 'dustbin_driver_search.html', {'dustbin_driver_search': dustbindata})


def complaint_reg(request):
    id = request.session.get('publicid')
    data = get_object_or_404(PublicReg, login_id=id)  
    print(data)
    
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)  
            complaint.login_id= data 
            complaint.save() 
            return redirect('usertemplate')
    else:
        form = ComplaintForm()
    
    return render(request, 'complaints.html', {'form': form})


def complaint_muncipality_view(request):
    login_id = request.session.get('muncipalityid')
    data = get_object_or_404(MuncipalityReg,login_id=login_id)
    complaintdata = Complaints.objects.filter(login_id__muncipality=data)
    return render(request, 'complaint_muncipality_view.html', {'complaint_muncipality_view': complaintdata})
    
def complaint_update(request, id):
    data = get_object_or_404(Complaints, id=id)
    
    if request.method == 'POST':
        updateform = ComplaintForm(request.POST, instance=data)
        
        if updateform.is_valid():
            updateform.save()
            return redirect('complaint_user_view')  
    else:
        updateform = ComplaintForm(instance=data) 
    
    return render(request, 'complaint_update.html', {'updateform': updateform})

def complaint_delete(request, id):
    data = get_object_or_404(Complaints,id=id)
    data.delete()
    return redirect('complaint_user_view')



def complaint_user_view(request):
    login_id = request.session.get('publicid')
  
    # data = get_object_or_404(MuncipalityReg, login_id=login_id)
    complaintdata = Complaints.objects.all()
    
    return render(request, 'complaint_user_view.html', {'complaint_user_view': complaintdata})


def reply(request,id):
    data = get_object_or_404(Complaints,id=id)  
    print(data) 
    print(id)
    
    if request.method == 'POST':
        rply = request.POST.get('reply')
        data.reply = rply
        data.save()
        return redirect('muncipality_home')
    # else:
        
        
    return render(request, 'reply.html')

    

def notifications(request):
    id = request.session.get('muncipalityid')
    data = get_object_or_404(MuncipalityReg, login_id=id)  
    print(data)
    
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notify = form.save(commit=False)  
            notify.login_id= data 
            notify.save() 
            return redirect('muncipality_home')
    else:
        form = NotificationForm()
    
    return render(request, 'notifications.html', {'form': form}) 

def notify_muncipality_view(request):
    login_id = request.session.get('muncipalityid')
    data = get_object_or_404(MuncipalityReg,login_id=login_id)
    notifydata = Notifications.objects.filter(login_id=data)
    return render(request, 'notify_muncipality_view.html', {'notify_muncipality_view':notifydata})
    
def notify_update(request, id):
    data = get_object_or_404(Notifications, id=id)
    
    if request.method == 'POST':
        updateform = NotificationForm(request.POST, instance=data)
        
        if updateform.is_valid():
            updateform.save()
            return redirect('notify_muncipality_view')  
    else:
        updateform = NotificationForm(instance=data) 
    
    return render(request, 'notify_update.html', {'updateform': updateform})

def notify_delete(request, id):
    data = get_object_or_404(Notifications,id=id)
    data.delete()
    return redirect('notify_muncipality_view')


def notify_user_view(request):
    login_id = request.session.get('muncipalityid')
  
    # data = get_object_or_404(MuncipalityReg, login_id=login_id)
    notifydata = Notifications.objects.all()
    
    return render(request, 'notify_user_view.html', {'notify_user_view': notifydata})


def dustbin_harithakarma_view(request):
   
    login_id = request.session.get('publicid')
    

    
    try:
        data = DustbinReg.objects.all()
        print(data)
        # publicdata = PublicReg.objects.filter(login_id_id=login_id)

        return render(request, 'dustbin_harithakarma_view.html', {'dustbin_harithakarma_view': data})
    except DustbinReg.DoesNotExist:
        return render(request, 'dustbin_harithakarma_view.html', {'error': 'user not found.'})


def dustbin_driver_view(request):
   
    login_id = request.session.get('publicid')
    
    try:
        data = DustbinReg.objects.all()
        print(data)
        # publicdata = PublicReg.objects.filter(login_id_id=login_id)

        return render(request, 'dustbin_driver_view.html', {'dustbin_driver_view': data})
    except DustbinReg.DoesNotExist:
        return render(request, 'dustbin_driver_view.html', {'error': 'user not found.'})

def wastecollection(request,id):
    dustbin = get_object_or_404(DustbinReg,id=id)
    log_id = request.session.get('harithakarmaid')
    haritha_id = get_object_or_404(HarithakarmaReg,login_id = log_id)
    WasteCollection.objects.create(
        dustbin_id = dustbin,
        harithakarma_id = haritha_id
        )
    dustbin.collection_status = 1
    dustbin.save()
    return redirect('dustbin_harithakarma_view')



def muncipality_waste_view(request):
    login_id = request.session.get('muncipalityid')
    
 
    data = WasteCollection.objects.all()
    
    return render(request, 'muncipality_waste_view.html', {'muncipality_waste_view': data})
    
def logout(request):
    request.session.flush()
    return redirect('/')    
    
  













       

     







    




