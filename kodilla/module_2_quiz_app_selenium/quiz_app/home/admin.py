from django.contrib import admin
from . models import ExtendedUser, Profile, Questions, Scores

# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(Profile)
admin.site.register(Questions)
admin.site.register(Scores)
