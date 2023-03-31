from django.shortcuts import render
from apps.user.models import MentorUser
from apps.api.user import MentorUserSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response




@csrf_exempt

def user_list(request):
    if request.method == 'GET':
        user = MentorUser.objects.all()
        serializer = MentorUserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['username'] = data.get('email')
        serializer = MentorUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = MentorUser.objects.get(email=email)
            if user.check_password(password):
                user_data = {
                    'email': user.email,
                    'name': user.full_name,
                    'contact': user.contact
                }
                return JsonResponse(user_data, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)


