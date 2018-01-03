from rest_framework.decorators import api_view, list_route, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.http import JsonResponse

from rest_api.simple_api.serializers import SimpleSerializer
from rest_api.simple_api.resources import SimpleClass

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'hello': reverse('simple-hello', request=request, format=format),
        'list': reverse('simple-list', request=request, format=format),
    })


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


@api_view(['GET', 'POST' ])
def simple_list(request):
    """Simple list of names, country and language."""
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SimpleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    my_data = [SimpleClass('ross', 'us', 'urdu'), SimpleClass('ujjwal', 'india', 'english')]
    results = SimpleSerializer(my_data, many=True)
    return Response(results.data)