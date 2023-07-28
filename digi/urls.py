from django.urls import path
from digi import views
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("index2/", views.index2, name='index2'),
   
    path("login/", views.login, name="login"),
    path("logoutUser/", views.logoutUser, name="logoutUser"),
    path("register/", views.register, name="register"),
    path("sendmoney/", views.sendmoney, name="sendmoney"),
    path("deposite/", views.deposite, name="deposite"),
    path("withdraw/", views.withdraw, name="withdraw"),
    path("transaction/", views.transaction, name="transaction"),
    path("userinfo/", views.userinfo, name="userinfo"),
    path("creditdebit/", views.creditdebit, name="creditdebit"),
    path("loanreg/", views.loanreg, name="loanreg"),
    path("insureg/", views.insureg, name="insureg"),
    path("balance/", views.balance, name="balance"),
    path("razorpay/", views.razorpay, name="razorpay")
    
    
]
