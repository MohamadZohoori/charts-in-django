from django.shortcuts import render
from django.views.generic import View
from .models import Data   
from rest_framework.views import APIView
from rest_framework.response import Response

   
class home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')

   
class chart(APIView):
    def get(self, request, format = None):
        db_len = Data.objects.all().values().count()
        labels = []

        for i in range(db_len):
            data = Data.objects.get(id = i + 1)
            labels.append(str(data.date))

        bp = []

        for i in range(db_len):
            data = Data.objects.get(id = i + 1)
            bp.append(int(data.bloodpressure))

        bp2 = []

        for i in range(db_len):
            data = Data.objects.get(id = i + 1)
            bp2.append(int(data.bp2))

        data = {
            'labels' : labels,
            'chartLabel': 'blood pressure record(1)',
            'chartdata' : bp,
            'chartdata2': bp2, 
            }

        return Response(data)