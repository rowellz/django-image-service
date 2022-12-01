from ast import arg
from email.mime import image
from rest_framework.views import APIView
from rest_framework import generics
from myapp.serializers import MyProfileSerializers, MyProfileImageSerializers
from myapp.services.gif_maker_service import AugmentImageService
from myapp.models import MyProfileModel
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, IN_FORM, TYPE_FILE, TYPE_INTEGER


class GIFAPI(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("name", in_=IN_FORM, type="string", description="name of image", required=True),
            Parameter("image", in_=IN_FORM, type=TYPE_FILE, description="picture to upload", required=True),
            Parameter("min", in_=IN_FORM, type=TYPE_INTEGER, description="a number to set the minimum random distortion rate. Defualt 10"),
            Parameter("max", in_=IN_FORM, type=TYPE_INTEGER, description="a number to set the maximum random distortion rate. Defualt 30"),
            Parameter("fps", in_=IN_FORM, type=TYPE_INTEGER, description="a number to set the frames per second for the denerated gif, Defualt 24"),
        ]
    )
    def post(self, request):
        p1 = MyProfileModel(name=request.data["name"], image=request.data["image"])
        p1.save()
        path = f"./media/{p1.image}"
        service = AugmentImageService()
        min = request.data.get("min", 10)
        max = request.data.get("max", 30)
        fps = request.data.get("fps", 24)
        print("view", min, max)
        gif_path = service.create_gif(img_path=path, min=min, max=max, fps=fps)
        p1.gif = gif_path.replace("./media/", "")
        p1.save()

        return FileResponse(open(gif_path, 'rb'))
