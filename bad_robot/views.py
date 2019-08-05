import json
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Q
from bad_robot import models
from bad_robot.models import JoinActivity


def search_activity(request):
    if request.method == 'POST':
        res = str(request.body)[2:-1]
        # print(res)
        question_id = json.loads(res)['id']
        data = {}
        activity = models.Activity.objects.filter(activity_number=question_id)
        data['list'] = json.loads(serializers.serialize("json", activity))
        # print(data['list'])
        return HttpResponse(data['list'])
    else:
        return HttpResponse('method not allowed')


def join_activity(request):
    if request.method == 'POST':
        res = str(request.body)[2:-1]
        # print(res)
        user_id = json.loads(res)['user_id']
        activity_num = json.loads(res)['activity_num']
        print(user_id, activity_num)
        is_activity = models.Activity.objects.filter(Q(activity_number=activity_num) & Q(is_join=1))
        is_join = models.JoinActivity.objects.filter(Q(activity_number=activity_num) & Q(user_id=user_id))
        print(is_join.count())
        if is_join.count() == 0 & is_activity.count() != 0:  # 活动存在可报名并且没有报名
            join = JoinActivity(activity_number=activity_num, user_id=user_id)
            join.save()
            data = {}
            activity = models.JoinActivity.objects.filter(activity_number=activity_num)
            data['list'] = json.loads(serializers.serialize("json", activity))
            # print(data['list'])
            return HttpResponse(data['list'])
        elif is_join.count() != 0:
            return HttpResponse("repeat")
        else:
            return HttpResponse("not found")
    else:
        return HttpResponse('method not allowed')


def cancel_activity(request):
    if request.method == 'POST':
        res = str(request.body)[2:-1]
        # print(res)
        user_id = json.loads(res)['user_id']
        activity_num = json.loads(res)['activity_num']
        print(user_id, activity_num)
        is_activity = models.Activity.objects.filter(Q(activity_number=activity_num) & Q(is_join=1))
        is_join = models.JoinActivity.objects.filter(Q(activity_number=activity_num) & Q(user_id=user_id))
        print(is_activity.count(), is_join.count())
        if (is_join.count() > 0) & (is_activity.count() > 0):  # 活动存在可报名并且报名了
            models.JoinActivity.objects.get(Q(activity_number=activity_num) & Q(user_id=user_id)).delete()
            data = {}
            activity = models.JoinActivity.objects.filter(activity_number=activity_num)
            data['list'] = json.loads(serializers.serialize("json", activity))
            print(data['list'])
            return HttpResponse(data['list'])
        elif (is_join.count() < 1) & (is_activity.count() > 0):    # 活动存在可报名但没报名
            return HttpResponse('Not Join')
        else:
            return HttpResponse('Not Found')
    else:
        return HttpResponse('method not allowed')
