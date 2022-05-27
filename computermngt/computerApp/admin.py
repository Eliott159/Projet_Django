from django.contrib import admin

from .models import Machine
from .models import Personnel

# Register your models here.

admin.site.register(Machine)
admin.site.register(Personnel)

