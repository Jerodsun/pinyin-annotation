from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import PinyinCodes
from .serializers import UserInputSerializer
from .logic.matcher import match_pinyin


# Create your views here.

class UserInputView(viewsets.ModelViewSet):
    serializer_class = UserInputSerializer
    queryset = PinyinCodes.objects.all()

    http_method_names = ['post']

    def create(self, request):
        # You need to CREATE into a seperate table, but use the QUERYSET as a reference.
        
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            d = serializer.validated_data
            matched_string = match_pinyin(d, PinyinCodes)
            return Response({'message':'success', 'result':matched_string})

        # catch errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
