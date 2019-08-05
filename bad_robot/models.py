from django.db import models


class Student(models.Model):
    name = models.CharField(u'姓名', max_length=100, default='no_name')
    sex = models.CharField(u'性别', max_length=50, default='male')
    sid = models.CharField(u'学号', max_length=100, default='0')

    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)


class Activity(models.Model):
    activity_time = models.DateTimeField('活动时间', default='')
    activity_place = models.CharField('活动地点', max_length=100, default='')
    activity_number = models.IntegerField('活动编号', default=1, primary_key=True)
    is_join = models.BooleanField('允许报名', default=False)


class User(models.Model):
    user_name = models.CharField('用户名', default='user', max_length=100, )
    user_id = models.CharField('用户id', default='userId', max_length=100, primary_key=True)
    wechat_name = models.CharField('微信昵称', max_length=100, default='name')
    password = models.CharField('密码', default='password', max_length=20)


class JoinActivity(models.Model):
    activity_number = models.IntegerField('活动编号')
    user_id = models.CharField('用户id', max_length=100)
    plug = models.BooleanField('是否外挂', default=False)
    substitute = models.BooleanField('是否替补', default=False)
