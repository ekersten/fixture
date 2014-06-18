from django.contrib.auth.models import User
from main.models import Profile

class DniBackend(object):
	def authenticate(self, dni=None):
		try:
			profile = Profile.objects.get(dni=dni)
			return profile.user
		except Profile.DoesNotExist:
			return none

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
