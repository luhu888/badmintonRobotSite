from django.contrib import admin

# Register your models here.
from bad_robot.models import Student, JoinActivity, User, Activity

admin.site.register(Student)
admin.site.register(JoinActivity)
admin.site.register(User)
admin.site.register(Activity)