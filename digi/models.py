from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
# User = get_user_model()

class CustomUser(AbstractBaseUser):

    def has_module_perms(self, digi):
        return True

    def has_perm(self, perm, obj=None):
        return True

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    username = models.CharField(max_length=50, unique=True, primary_key=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=500, null=True)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    ac_type = models.CharField(max_length=50)
    card_number = models.IntegerField(default=8050504020303020)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return self.username
    

class UserAccount(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=100)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sender_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='recipient_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()


    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}: {self.amount}"

class Loan_Application(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    loanamount = models.CharField(max_length=50)
    ssn = models.CharField( max_length=50)
    monthlyincome = models.CharField( max_length=50)
    bankaccount = models.CharField( max_length=50)
    loantype = models.CharField( max_length=50)
# class UserAtm(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     atmno
class Creditdebit(models.Model):
    fullName = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    bankName = models.CharField(max_length=50)
    accountNumber = models.CharField( max_length=50)
    cardType = models.CharField( max_length=50)

    def __str__(self):
        return self.fullName

class Insurance_Application(models.Model):
    fullName = models.CharField( max_length=50)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    contactNumber = models.CharField(max_length=50)
    email = models.CharField( max_length=50)
    bankName= models.CharField( max_length=50)
    accountNumber = models.CharField( max_length=50)
    insuranceType = models.CharField( max_length=50)

    