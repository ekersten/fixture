from django.contrib import admin
from .models import Country
from .models import Group
from .models import Match

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