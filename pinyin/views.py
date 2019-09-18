from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import PinyinCodes, UserInput
from .serializers import UserInputSerializer
from .logic.matcher import match_pinyin

# Create your views here.

class UserInputView(viewsets.ModelViewSet):
    serializer_class = UserInputSerializer
    queryset = UserInput.objects.all()

    http_method_names = ['get', 'post']

    def create(self, request):
        # CREATE into a seperate table, but use the QUERYSET as a reference.
        
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip_address=self.get_client_ip(request))
            d = serializer.validated_data
            matched_string = match_pinyin(d['input_string'], PinyinCodes)

            return Response({'message':'success', 'result': matched_string })

        # catch errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        return Response({'message':'Please post a string < 200 chars.'})

    def retrieve(self, request, pk):
        # also temporarily block id selections
        return Response({'message':'Please post a string < 200 chars.'})

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
