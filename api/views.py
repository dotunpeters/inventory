
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# import models
from .models import User, Tank
from .serializers import TankSerializer, UserSerializer, RegisterSerializer

# Create your views here.


@api_view(['GET'])
def user_all(request):
    try:
        serializer = UserSerializer(User.objects.all(), many=True)
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_404_NOT_FOUND
            )
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user(request):
    try:
        serializer = UserSerializer(User.objects.get(pk=request.GET['id']))
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_404_NOT_FOUND
            )
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def user_update(request):
    value = User.objects.get(pk=request.data['id'])
    serializer = UserSerializer(value, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.validated_data,
                status=status.HTTP_202_ACCEPTED
                )
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_404_NOT_FOUND
            )


@api_view(['DELETE'])
def user_delete(request):
    try:
        value = User.objects.get(pk=request.data['id'])
        value = value.delete()
        return Response(
            data={"success": f"Deleted user id {request.data['id']}"},
            status=status.HTTP_200_OK
            )
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_501_NOT_IMPLEMENTED
            )


@api_view(['POST'])
def user_register(request):
    try:
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.validated_data,
                status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                data={"error": "invalid data"},
                status=status.HTTP_501_NOT_IMPLEMENTED
                )
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(['POST'])
def user_login(request):
    pass


@api_view(['POST'])
def user_logout(request):
    pass


@api_view(['POST'])
def tank_create(request):
    try:
        serializer = TankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.validated_data,
                status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                data={"error": "invalid data passed"},
                status=status.HTTP_501_NOT_IMPLEMENTED
                )
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(['POST'])
def tank_update(request):
    try:
        value = Tank.objects.get(pk=request.data['id'])
    except value.DoesNotExist:
        return Response(
            data={"error": "Tank does not exist"},
            status=status.HTTP_404_NOT_FOUND
            )
    try:
        serializer = TankSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.validated_data,
                status=status.HTTP_202_ACCEPTED
                )
        else:
            return Response(
                data={"error": "invalid data"},
                status=status.HTTP_501_NOT_IMPLEMENTED
                )
    except Exception as e:
        return Response(
            data={"error": f"{e}"},
            status=status.HTTP_404_NOT_FOUND
            )
