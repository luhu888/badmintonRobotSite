import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, HttpRequest, JsonResponse

from bad_robot import models


def search_activity(request):
    if request.method == 'POST':
        res = str(request.body)[2:-1]
        # print(res)
        question_id = json.loads(res)['id']
        data = {}
        activity = models.Activity.objects.filter(activity_number=question_id)
        data['list'] = json.loads(serializers.serialize("json", activity))
        print(data['list'])
        return HttpResponse('success!!1')
