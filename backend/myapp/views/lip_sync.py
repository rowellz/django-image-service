import base64
import mimetypes
import tempfile
from rest_framework.views import APIView
from rest_framework import generics
from django.core.files.base import ContentFile
from myapp.serializers import MyProfileSerializers, MyProfileImageSerializers
from myapp.services.lip_sync_service import LipSyncService
from myapp.models import AlignmentModel
from rest_framework.parsers import FormParser, MultiPartParser
from django.http import FileResponse, HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_QUERY, IN_FORM, TYPE_FILE
import torch
import torchaudio

class LipSyncAPI(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("audio_file", IN_FORM, type=TYPE_FILE, description="audio file to upload", required=True),
            Parameter("text_file", in_=IN_FORM, type=TYPE_FILE, description="text file containing a transcript of audio file"),
            Parameter("text", in_=IN_FORM, type="string", description="text transcript of audio file"),
            Parameter("auto_text", IN_FORM, type="boolean"),
        ]
    )
    def post(self, request):
        
        text = request.data.get("text", False)
        text_file = request.data.get("text_file", False)
        auto_text = True if request.data.get("auto_text", "false").lower() == "true" else False

        if not text_file and not text and not auto_text:
            return HttpResponse({"bad request!"}, 400)

        if not text_file and text:  
            text_file = ContentFile(text.encode('utf8'), name='temp.txt')
            
        align = AlignmentModel(audio_file=request.data["audio_file"], text_file=text_file)
        align.save()
        print(f"Done creating mapping with id: {align.id}")
        service = LipSyncService()
        print("fsafsda", auto_text)
        lip_sync = service.sync_audio_and_text(align, auto_text)
        video_path = service.create_lazykh_folder(align)
        file = FileResponse(open(video_path, 'rb'), filename=f"{align.name}.webm",)
        return file
        # response = HttpResponse({open(video_path, 'rb')}, content_type=mimetypes.guess_type(video_path)[0],)
        # response['Content-Disposition'] = f'attachment; filename="f"{align.name}.webm""'
        # return response
        # return HttpResponse(lip_sync, 200)


class LipSyncAPI2(APIView):
    parser_classes = (FormParser, MultiPartParser)
    @swagger_auto_schema(
        manual_parameters=
        [
            Parameter("audio_file", IN_FORM, type=TYPE_FILE, description="audio file to upload", required=True),
            Parameter("text_file", in_=IN_FORM, type=TYPE_FILE, description="text file containing a transcript of audio file"),
            Parameter("text", in_=IN_FORM, type="string", description="text transcript of audio file"),
            Parameter("auto_text", IN_FORM, type="boolean", required=True),
        ]
    )
    def post(self, request):
        
        text = request.data.get("text", False)
        text_file = request.data.get("text_file", False)
        auto_text = True if request.data.get("auto_text", "false").lower() == "true" else False

        if not text_file and not text and not auto_text:
            return HttpResponse({"bad request!"}, 400)

        if not text_file and text:  
            text_file = ContentFile(text.encode('utf8'), name='temp.txt')
            
        align = AlignmentModel(audio_file=request.data["audio_file"], text_file=text_file)
        align.save()
        # Create a forced aligner object
        # Define the paths to the acoustic and language models

        return HttpResponse(alignment, 200)

