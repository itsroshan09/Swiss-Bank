from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserAccount)
admin.site.register(Transaction)

admin.site.register(Creditdebit)
admin.site.register(Loan_Application)
admin.site.register(Insurance_Application)