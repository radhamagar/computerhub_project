
# Register your models here.
from django.contrib import admin
from .models import ComputerBrands, ComputerSpecification, Computer, ComputerGeneration

admin.site.register(ComputerBrands)
admin.site.register(ComputerSpecification)
admin.site.register(Computer)
admin.site.register(ComputerGeneration)

