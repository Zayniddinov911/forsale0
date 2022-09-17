from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonModelSerializer
from little.models import PersonModel




@api_view(['GET'])
def getData(request):
    info = PersonModel.objects.all()
    serializer = PersonModelSerializer(info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDetail(request, pk):
    info = PersonModel.objects.get(id=pk)
    serializer = PersonModelSerializer(info, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = PersonModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




