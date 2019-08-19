from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response



# class MileStoneStatus(APIView):
   
#  def get(self,request):
#     total_sites    = Site.objects.all().count()
#     sites_accepted = Site.objects.all().filter(final_acceptance_cert_comment__isnull=False)
#     sites_rejected = total_sites - sites_accepted
#     return Response ({'total_sites':total_sites,'sites_accepted':sites_accepted,'sites_rejected':sites_rejected})

class MileStoneStatus(APIView):
    
    def get(self, request):
        issues = Issues.objects.all().count()
        issues_closed = Issues.objects.filter(closed=True).count()
        issues_open = issues - issues_closed
        return Response({'total_issues': issues, 'issues_closed': issues_closed, 'issues_open': issues_open, })

        
##Still 
class BudgetStatus(APIView):
    def get(self,request):
        return Response({})