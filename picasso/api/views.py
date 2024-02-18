from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.serializers import FileSerializer

from files.tasks import process_file


@api_view(['POST'])
def upload_file(request):
    serializer = FileSerializer(data=request.data)

    if serializer.is_valid():
        file_instance = serializer.save()
        process_file.delay(file_instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
