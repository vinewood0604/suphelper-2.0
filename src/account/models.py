from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Defining what we want to happen when a new user/superuser are created.
class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("User must have an email address.")
		if not username:
			raise ValueError("User must have a username.")
		
		user = 	self.model(
				email=self.normalize_email(email),
				username=username
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = 	self.create_user(
				email=self.normalize_email(email),
				password=password,
				username=username
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

# Building our own custom user model
class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined 			= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	last_login 				= models.DateTimeField(verbose_name="last login", auto_now_add=True)
	is_admin 				= models.BooleanField(default=False)
	is_active 				= models.BooleanField(default=True)
	is_staff 				= models.BooleanField(default=False)
	is_L2	 				= models.BooleanField(default=False)
	is_L1	 				= models.BooleanField(default=False)
	is_superuser 			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email' 	# Lets the user to login with this parameter.
	REQUIRED_FIELDS = ['username']

	# We want to tell this account object where the manager is and how to use the manager.
	objects = MyAccountManager()

	def __str__(self):
		#return self.email 	# When we print an account object to a template what do we want to display.
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

class Theme(models.Model):
	color 					= models.CharField(max_length=1000)
	user 					= models.CharField(max_length=1000)

	def __str__(self):
		return self.user