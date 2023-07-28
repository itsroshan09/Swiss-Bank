
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model, logout
# from digi.models import CustomUser, UserAccount
from decimal import Decimal
from datetime import datetime
import random
User = get_user_model()
# Create your views here.


def load(request):
    return render(request, "loading.html")

def index2(request):
    return render(request, "index.html")

def razorpay(request):
    return render(request, "razorpay.html")
   


def insureg(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        dateOfBirth = request.POST.get('dateOfBirth')
        contactNumber = request.POST.get('contactNumber')
        email = request.POST.get('email')
        bankName = request.POST.get('bankName')
        accountNumber = request.POST.get('accountNumber')
        insuranceType = request.POST.get('insuranceType')
        insrueg1 = Insurance_Application.objects.create(fullName=fullName,dateOfBirth=dateOfBirth,contactNumber=contactNumber,email=email,bankName=bankName,accountNumber=accountNumber,
        insuranceType=insuranceType)
        return redirect("razorpay") #Razorpay
    return render(request, "insureg.html")

def loanreg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        loanamount = request.POST.get('loanamount')
        ssn = request.POST.get('ssn')
        monthlyincome = request.POST.get('monthlyincome')
        bankaccount = request.POST.get('bankaccount')
        loantype = request.POST.get('loantype')

        loanreg1 = Loan_Application.objects.create(name=name,email=email,phone=phone,loanamount=loanamount,ssn=ssn,
        monthlyincome=monthlyincome,bankaccount=bankaccount,loantype=loantype)
        return redirect('home')
    else:
        return render(request, "loanreg.html")


def creditdebit(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        bankName = request.POST.get('bankName')
        accountNumber = request.POST.get('accountNumber')
        cardType = request.POST.get('cardType')
        credit = Creditdebit.objects.create(fullName=fullName,email=email,phone=phone,bankName=bankName,accountNumber=accountNumber,cardType=cardType)
        return redirect('home')
        
    return render(request, "creditdebit.html")

def index(request):
    return render(request, "index2.html")


def userinfo(request):
    userinfo = CustomUser.objects.filter(username=request.user).first()
    context = {
        'userinfo': userinfo
    }
    return render(request, "userinfo.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login Successfully")
            
            # try:
            #     user_account = UserAccount(
            #     user = request.user,
            #     balance = 100
            # )  
            #     user_account.save()
            # except:
            #     messages.success(request, "Error Try again!")
            #     return redirect("/login")
            return redirect("index2")
        else:
            # Authentication failed
            return render(request, "/login.html")
    else:
        return render(request, "login.html")

def register(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postcode = request.POST.get("postcode")
        ac_type = request.POST.get("actype")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            def generate_random_number():
                min_value = 10**11  # Minimum 12-digit number
                max_value = (10**12) - 1  # Maximum 12-digit number
                return random.randrange(min_value, max_value)

            card_number = generate_random_number()

            CustomUser.objects.create_user(username=username, email=email, phone_number=phone_number, dob=dob, gender=gender, address=address, city=city, postcode=postcode,ac_type=ac_type, password=password1, card_number=card_number)


            # user.save()
            messages.success(request, "Registered Successfully")
            return redirect('/login/')
        else:
            messages.success(request, "Check password")
            return render(request, "register.html")

    else:
        return render(request, "register.html")

def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("/login/")

def transaction(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    transaction = Transaction.objects.filter(sender=request.user).order_by('-date').only()
    context = {
        'transaction': transaction,
    }
    return render(request, "transaction.html", context)

def withdraw(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if request.method == 'POST':
        user = request.user
        amount = Decimal(request.POST['amount'])

        try:
            user_account = UserAccount.objects.get(user=user)
        except UserAccount.DoesNotExist:
            # Handle case when the user account does not exist
            return render(request, 'withdraw.html')

        if amount <= 0 or amount > user_account.balance:
            messages.success(request, "Unsufficient Balance")
            return render(request, 'withdraw.html')

        user_account.balance -= amount
        user_account.save()

        transaction = Transaction(
            sender=user, 
            amount=amount, 
            receiver=user,
            date = datetime.today()
        )
        transaction.save()
        messages.success(request, "Amount Withdrawn Successfully")

        return redirect('/index2/')

    return render(request, 'withdraw.html')

def balance(request):
    print(balance)
def deposite(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if request.method == 'POST':
        user = request.user
        amount = Decimal(request.POST['amount'])

        try:
            user_account = UserAccount.objects.get(user=user)
        except UserAccount.DoesNotExist:
            return render(request, 'deposite.html')

        if amount <= 0:
            messages.success(request, "Enter Valid Amount")
            return redirect("/deposite/")

        user_account.balance += amount
        user_account.save()
        print(datetime.today())

        transaction = Transaction(
            sender=user, 
            amount=amount, 
            receiver=user,
            date = datetime.today()
        )
        transaction.save()
        messages.success(request, "Amount Deposited Successfully")
        return redirect('/index2/')

    return render(request, 'deposite.html')


def sendmoney(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
        

    if request.method == 'POST':
        sender = request.user
        receiver_username = request.POST['receiverUsername']
        amount = request.POST['amount']
        
        sender_account = UserAccount.objects.get(user=sender)

        if Decimal(sender_account.balance) < Decimal(amount):
            return render(request, 'sendmoney.html')
        

        try:
            receiver_user = User.objects.get(username=receiver_username)
            receiver_account = UserAccount.objects.get(user=receiver_user)
        except User.DoesNotExist:
            # Handle case when the receiver's user does not exist
            return render(request, 'sendmoney.html')
            messages.success(request, "Amount Withdrawn Successfully")
        # if not receiver_user.is_present:
        #     messages.success(request, "Receiver Account Is Invalid")
            
        sender_account.balance -=  Decimal(amount)
        sender_account.save()

        receiver_account.balance += Decimal(amount)
        receiver_account.save()

        transaction = Transaction(
            sender=sender,
            receiver=receiver_account.user,
            amount=amount,
            date = datetime.today()
        )
        transaction.save()
        messages.success(request, "Transaction Successfull....!!!!")
        return redirect("/index2/")
    
    return render(request, 'sendmoney.html')
