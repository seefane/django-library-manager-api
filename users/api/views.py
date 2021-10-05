from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import RegistrationSerializer, StudentSerializer, UserSerializer
from ..models import Student


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data ={}
        if serializer.is_valid():
            user = serializer.save()
            data['response']= 'User registration successful'
            data['username'] = user.username
            data['email'] = user.email
            print(Token.objects.filter(user=user))
            token = str(Token.objects.filter(user=user).first())
            data['token'] = token
            print(data)
        else:
            data = serializer.errors
        return Response(data)

class loginAuthtoken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        isAdmin ="False"
        if user.is_superuser: isAdmin="True"

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'isAdmin': isAdmin,
            'first_name': user.first_name,
            'last_name': user.last_name,

        })
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editUserinfo(request,userpk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    student = Student.objects.get(user=user)
    student_serializer = StudentSerializer(student,data=request.data)
    user_serializer = UserSerializer(user,data=request.data)
    student_serializer_is_valid = False
    user_serializer_is_valid = False
    response={}
    serializer_errors={}
    if student_serializer.is_valid():
        student_serializer_is_valid = True


    serializer_errors.update(student_serializer.errors)
    if user_serializer.is_valid():
        password = user_serializer.validated_data.get('password')
        user_serializer.validated_data['password'] = make_password(password)
        user_serializer_is_valid =True

    serializer_errors.update(user_serializer.errors)
    if user_serializer_is_valid and student_serializer_is_valid:
        student_serializer.save()
        user_serializer.save()
        user.is_active=True
        user.save()
        response["success"] = "Update completed successfully"
        return Response(data=response)
    return Response(serializer_errors, status=status.HTTP_400_BAD_REQUEST)




