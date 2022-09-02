from ast import arg
from email.mime import image
from rest_framework import generics
from .serializers import MyProfileSerializers, MyProfileImageSerializers
from .models import MyProfileModel
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import FileResponse, HttpResponse, response

class MyProfileListView(generics.ListCreateAPIView):
    '''This class is a view that lists all the MyProfileModel objects
    and allows to create new ones'''
    parser_classes = (FormParser, MultiPartParser)
    queryset = MyProfileModel.objects.all()
    serializer_class = MyProfileSerializers


class MyProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''This class allows to retrieve, update, or
    delete a specific instance of the MyProfileModel'''
    parser_classes = (FormParser, MultiPartParser)
    queryset = MyProfileModel.objects.all()
    serializer_class = MyProfileSerializers

    def Image_view(request):
        img=open("./media/images/snackeeper.jpg")
        return FileResponse(img)


class MyModelView(generics.CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    queryset = MyProfileModel.objects.all()
    serializer_class = MyProfileImageSerializers
    

    def post(self, request):
        """
            Create a MyModel
            ---
            parameters:
                - name: source
                  description: file
                  required: True
                  type: file
            responseMessages:
                - code: 201
                  message: Created
        """
        # name = self.kwargs['name']
        # name = kwargs.get('name', 'Default Value if not there')
        print("dhjajfkd", request, request.data)
        p1 = MyProfileModel(name=request.data["name"], image=request.data["image"])
        p1.save()
        return HttpResponse('<h1>Hello HttpResponse</h1>')
    
    def get(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MyProfileImageSerializers(queryset, many=True)
        return HttpResponse(serializer.data)

    def patch(self, *args, **kwargs):
        pass
