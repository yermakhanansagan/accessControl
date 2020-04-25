from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from snippets.models import History, Employees, Access, Devices, Snippet
from snippets.serializers import PersonalSerializer, EmployeesDetailSerializer, SnippetSerializer, HistorySerializer, DeviceSerializer, EmployeesSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def history_list(request):
    if request.method == 'GET':
        history = History.objects.all()
        serializer = HistorySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            access = Access.objects.get(card_id=data['card'])
        except Access.DoesNotExist:
            card_id = data['card']
            access = Access.objects.create(card_id=card_id)
            access.save()
        serializer = HistorySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse({"access":access.access}, status=201)
        return JsonResponse(serializer.errors, status=400)


class EmployeesCreateViewSet(generics.CreateAPIView):
    serializer_class = EmployeesSerializer

class EmployeesListViewSet(generics.ListAPIView):
    # search_fields = ['name','surname','student_id']
    # filter_backends = (filters.SearchFilter, )
    # pagination_class = PostPageNumberPagination
    serializer_class = EmployeesDetailSerializer
    queryset = Employees.objects.all()
    # permission_classes = (IsAuthenticated, )

class EmployeesDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeesDetailSerializer
    queryset = Employees.objects.all()
    # permission_classes = (IsOwnerOrReadOnly, )

class PersonalViewSet(generics.ListAPIView):
    # search_fields = ['name','surname','student_id']
    # filter_backends = (filters.SearchFilter, )
    # pagination_class = PostPageNumberPagination
    serializer_class = PersonalSerializer
    queryset = Employees.objects.all()

class DeviceViewSet(generics.ListAPIView):
    # search_fields = ['device_model','serial_number','device_ip']
    # filter_backends = (filters.SearchFilter, )
    # pagination_class = PostPageNumberPagination
    serializer_class = DeviceSerializer
    queryset = Devices.objects.all()

class DeviceCreateViewSet(generics.CreateAPIView):
    serializer_class = DeviceSerializer

class DeviceDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    queryset = Devices.objects.all()