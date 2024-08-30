from django.contrib import admin
from toys.models import Toy
# Register your models here.



class Toyadmin(admin.ModelAdmin):
    list_display = [
        
        "name",
        "description",
        "release_date",
        "toy_category",
    ]
    search_fields=["name", "toy_category"]
    list_filter=["toy_category","release_date","was_included_in_home"]
    
admin.site.register(Toy,Toyadmin)