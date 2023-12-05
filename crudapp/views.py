from django.shortcuts import render
from crudapp import models,serializers
from crudapp.models import PlacementDetails
from crudapp.serializers import Placeserializer,Custom1
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListAPIView
from datetime import datetime
from django.db.models import F,Avg,Sum
#check the candidate_name(Demene Wilson) that is already in, if yes change the candidate_name to Andreson
class Renameclass(GenericAPIView):
    serializer_class = serializers.Custom1
    #queryset = models.PlacementDetails
    def put(self,request,**kwargs):
        query=models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name']).update(candidate_name=request.data['rename_name'])
        #serializer_class=serializers.Placeserializer(query)
        return Response('Updated')
#check the candidate_name(Shakir Terry) that is already in,if yes get Shakir his details
class Getnamedetails(GenericAPIView):
    serializer_class = serializers.Customnamedetail
    queryset = models.PlacementDetails
    def post(self,request,**kwargs):
        query=models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name'])
        serializer_class=serializers.Placeserializer(query,many=True)
        return Response(serializer_class.data)
# get only Lincare Holdings Inc.(client)  and Customer Support (business unit)
class Getnamebusiness(GenericAPIView):
    serializer_class = serializers.Customnamebusiness
    queryset = models.PlacementDetails

    def post(self, request, **kwargs):
        query=models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name'],business_unit=request.data['business_unit'])
        serializer_class=serializers.Placeserializer(query,many=True)
        return Response(serializer_class.data)
# load dump file and  add detail using POST method and show the added response as a json value
class Postdetail(CreateAPIView):
    serializer_class = serializers.Placeserializer
    #queryset = models.PlacementDetails
    def post(self,request):
        return self.create(request)
#4. get only masonite client details
class GetMasonite(GenericAPIView):
    serializer_class =serializers.CustomMasonite
    queryset = models.PlacementDetails
    def post(self,request):
        query=models.PlacementDetails.objects.filter(client=request.data['client'])
        serializer_class=serializers.Placeserializer(query,many=True)
        return Response(serializer_class.data)
#check the candidate_name(Priyanka Agrawal) that is already in,if yes get her business unit
class Getbusiness(GenericAPIView):
    serializer_class = serializers.Customnamedetail
    queryset = models.PlacementDetails
    def post(self,request):
        query=models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name'])
        serializer_class=serializers.Placeserializer(query,many=True)
        data={
              'candidate_name':serializer_class.data[0]['candidate_name'],
              'businessunit':serializer_class.data[0]['business_unit']
              }
        return Response(data)
class Listview(ListAPIView):
    serializer_class = serializers.Placeserializer
    queryset = models.PlacementDetails.objects.all()
    def get(self,request):
        return self.list(request)
class Retrieveview(RetrieveAPIView):
    serializer_class = serializers.Placeserializer
    queryset = models.PlacementDetails.objects.all()
    lookup_field = 'pk'
    def get(self,request,pk):
        return self.retrieve(request,pk)
class Createview(CreateAPIView):
    serializer_class = serializers.Placeserializer
    queryset = models.PlacementDetails.objects.all()
    #lookup_field = 'pk'
    def post(self,request):
        return self.create(request)
class Updateview(UpdateAPIView):
    serializer_class = serializers.Placeserializer
    queryset = models.PlacementDetails
    lookup_field = 'pk'

    def put(self, request, pk):
        return self.update(request, pk)
class Deleteview(DestroyAPIView):
    serializer_class = serializers.Placeserializer
    queryset = models.PlacementDetails
    lookup_field = 'pk'

    def delete(self, request, pk):
        return self.destroy(request, pk)

class Date(GenericAPIView):
    serializer_class = serializers.Customnamedetail
    queryset = models.PlacementDetails
    def post(self,request):
        query=models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name'])
        serializer_class=serializers.Placeserializer(query,many=True)
        datee=((datetime.strptime(serializer_class.data[0]['end_date'],'%Y-%m-%d'))-(datetime.strptime(serializer_class.data[0]['start_date'],'%Y-%m-%d'))).days
        return Response(datee)
class Bill(GenericAPIView):
    serializer_class = serializers.Customnamedetail
    queryset = models.PlacementDetails

    def post(self, request):
        query = models.PlacementDetails.objects.filter(candidate_name=request.data['candidate_name'])
        serializer_class = serializers.Placeserializer(query, many=True)
        bill=models.PlacementDetails.objects.annotate(price=F('bill_rate')+F('pay_rate'))
        for i in bill:
            return Response(i.price)
class Average(GenericAPIView):
    serializer_class = serializers.Placeserializer
    queryset = models.PlacementDetails

    def get(self, request):
        query = models.PlacementDetails.objects.filter(start_date__year=2023).aggregate(price=Avg(F('bill_rate')+F('pay_rate')))
        #serializer_class = serializers.Placeserializer(query, many=True)
        #bill=models.PlacementDetails.objects.aggregate(price=(F('bill_rate')+F('pay_rate')))
        return Response(query)
