from ast import arg
from io import StringIO
from email.mime import image
from rest_framework.views import APIView
from rest_framework import generics
from myapp.serializers import MyProfileSerializers, MyProfileImageSerializers
from myapp.services.lip_sync_service import LipSyncService
from myapp.models import AlignmentModel
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, IN_FORM, TYPE_FILE


class LipSyncAPI(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("text", in_=IN_FORM, type=TYPE_FILE, description="transcropt of audio file", required=True),
            Parameter("audio", IN_FORM, type=TYPE_FILE, description="audio file to upload", required=True),
        ]
    )
    def post(self, request):
        print("fsdaffdsfdas", request.data, request.query_params)
        # p1 = MyProfileModel(name=request.data["name"], image=request.data["image"])
        # p1.save()
        # path = f"./media/{p1.image}"

        
        # output = StringIO()
        # output.write(request.data["text"])
    
        # # Retrieve file contents -- this will be
        # # 'First line.\nSecond line.\n'
        # contents = output.getvalue()

        align = AlignmentModel(audio_file=request.data["audio"], text_file=request.data["text"])

        align.save()
        
        service = LipSyncService()
        lip_sync = service.sync_audio_and_text(request.data["audio"], request.data["text"], align)

        return HttpResponse(lip_sync, 200)
