from django.contrib import admin

from rest_framework_test.models import Student, JoinActivity, User, Activity

admin.site.register(Student)
admin.site.register(JoinActivity)
admin.site.register(User)
admin.site.register(Activity)

# Register your models here.
