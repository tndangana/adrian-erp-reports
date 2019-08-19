from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

class SiteRework(APIView):
   def get(self,request):
       return Response({})
