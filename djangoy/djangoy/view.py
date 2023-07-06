import json
from django.http import JsonResponse
import lightgbm as lgb
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import render
import random
import os
from django.conf import settings
from django.http import JsonResponse


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def my_api(request):
    # 获取参数值
    lat = float(request.GET.get('lat', 0))
    lon = float(request.GET.get('lon', 0))
    area = float(request.GET.get('area', 0))
    sub_distance = random.randint(150, 1500)
    convenience = random.randint(70, 95)
    floor_encode = random.randint(0, 2)
    towards_encode = random.randint(1, 33)
    # 加载模型
    loaded_gbm = lgb.Booster(model_file='D:\project\Python\project2\djangoy\model\model.model')

    new_data = np.array([[area, sub_distance, convenience, floor_encode, lat, lon, towards_encode]])
    # 进行预测

    pred = loaded_gbm.predict(new_data)

    data = {'message': pred[0]}
    return JsonResponse(data)



def my_page(request):
    return render(request, 'demo1.html')

def upload_file(request):
    return render(request, 'chatupload.html')



def uploadapi(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, 'static', uploaded_file.name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return JsonResponse({'message': '文件上传成功'})
    return JsonResponse({'error': '无效的请求'})