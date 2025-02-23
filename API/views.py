from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Form
from .serializers import FormSerializer

@api_view(['GET'])
def getData(request):
    person = Form.objects.all()
    serializer = FormSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = FormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)