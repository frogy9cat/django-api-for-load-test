
# from django.shortcuts import render
# from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.decorators import renderer_classes, api_view
# from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .serializers import UsersSerializer
from .models import Counter




class CounterAPIView(APIView):
    def get(self, request):
        try:
        
            from django.utils import timezone
            from datetime import timedelta

            try:
                try:
                    cc = Counter.objects.get(
                        created_at__gte=timezone.now() - timedelta(seconds=3),
                    )
                except Counter.MultipleObjectsReturned:
                    cc = Counter.objects.first()
                    
            except Counter.DoesNotExist:
                cc = Counter.objects.create()

            cc.icounter += 1
            cc.save(update_fields=['icounter'])
            print('success')
            return Response({"success": f"counter_{cc.icounter}"}, status=200)
            

            # except Counter.MultipleObjectsReturned:

            #     try:
            #         cc = Counter.objects.filter(
            #             created_at__gte=timezone.now() - timedelta(seconds=3),
            #         ).first()
            #     except Counter.DoesNotExist:
            #         cc = Counter.objects.create()

            #     cc.icounter = cc.icounter + 1
            #     cc.save(update_fields=['icounter'])
            #     print('success')
            #     return Response({"success": f"counter_{cc.icounter}"}, status=200)
                
        except Exception as err:
            print(err)
            return Response({"error": str(err)})

    def delete(self, request):
        try:
            Counter.objects.all().delete()
            return Response({"success":"all_counts_successfully_deleted"})
        except:
            return Response({"error":"something went worng"})






class UsersAPI(APIView):

    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        if users:
            return Response(serializer.data)
        else:
            return Response({"error": "there is no any users"})
        

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        import time
        time.sleep(1)
        serializer.save()
        return Response(serializer.data)

