from django.contrib import admin 
from .models import Freelancer, User, Client,Freelancer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'first_name',)


admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Freelancer)

class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('middle_name', 'skill', 'user', 'phone_number')
    list_filter = ('phone_number', 'skill', 'city', 'state', 'lga')
    search_fields = ('middle_name', 'skill')
    prepopulated_fields = {'slug' : ('middle_name',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'phone_number'
    ordering =  ('skill', 'phone_number')

# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('middle_name', 'skill', 'user', 'phone_number')
#     list_filter = ('phone_number', 'skill', 'user')
#     search_fields = ('middle_name', 'skill')
#     prepopulated_fields = {'slug' : ('middle_name',)}
#     raw_id_fields = ('user',)
#     date_hierarchy = 'phone_number'
#     ordering =  ('skill', 'phone_number')
