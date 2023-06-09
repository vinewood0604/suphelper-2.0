from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account, Theme


# Creating custom admin class
class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_L1', 'is_L2')
	search_fields = ('email', 'username')
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Theme)