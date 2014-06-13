from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from .models import Country
from .models import Group
from .models import Match


# User Profile
class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(UserAdmin):
	inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Countries Admin
class CountryAdmin(admin.ModelAdmin):
	def get_ordering(self, request):
		return ['group__name', 'name']

admin.site.register(Country, CountryAdmin)

# Groups Admin

class CountryTabularAdmin(admin.TabularInline):
	model = Country
	max_num = 4


class GroupAdmin(admin.ModelAdmin):
	inlines = (CountryTabularAdmin,)
	ordering = ('name',)

admin.site.register(Group, GroupAdmin)

# Mathces Admin

class MatchAdmin(admin.ModelAdmin):
	ordering = ('datetime',)

admin.site.register(Match, MatchAdmin)