
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import UserDetails
from . serializer import UserDetailsSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class LoginAPI(APIView):
    permission_classes = []
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors)
        else:
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            
        if not user:
            return Response({'error': 'Invalid username or password'}, status=400)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'Message': 'Login successful'})
    
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    people = {
        'name' : "Finu",
        'job' : "IT",
        'age' : 29,
    }
    return Response(people)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        data = UserDetails.objects.all()
        serializer = UserDetailsSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = UserDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        user = UserDetails.objects.get(id=data['id'])
        serializer = UserDetailsSerializer(user, data=data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        user = UserDetails.objects.get(id=data['id'])
        serializer = UserDetailsSerializer(user, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        data = request.data
        user = UserDetails.objects.get(id=data['id'])
        user.delete()
        return Response("Deleted")

class PersonView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        data = UserDetails.objects.all()
        serializer = UserDetailsSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = UserDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)