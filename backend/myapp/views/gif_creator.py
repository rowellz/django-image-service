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
from drf_yasg.openapi import Parameter, IN_QUERY, IN_FORM, TYPE_FILE


class GIFAPI(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("name", in_=IN_FORM, type="string", description="name of image", required=True),
            Parameter("image", IN_FORM, type=TYPE_FILE, description="picture to upload", required=True),
        ]
    )
    def post(self, request):
        p1 = MyProfileModel(name=request.data["name"], image=request.data["image"])
        p1.save()
        path = f"./media/{p1.image}"
        service = AugmentImageService()
        min = request.data.get("min", 10)
        max = request.data.get("min", 100)
        gif_path = service.create_gif(img_path=path, min=min, max=max)
        p1.gif = gif_path.replace("./media/", "")
        p1.save()

        return FileResponse(open(gif_path, 'rb'))
