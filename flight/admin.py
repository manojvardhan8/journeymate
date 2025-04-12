
# Register your models here.
from django.contrib import admin
from .models import flight_register,train_register

admin.site.register(flight_register)
admin.site.register(train_register)
