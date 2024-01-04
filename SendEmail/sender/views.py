from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Information
from .serializer import InformationSerializer


class SendEmailView(APIView):
    """ get information from user and send email """
    def get(self, request):
        """ show all emails """
        data = Information.objects.all()
        serializer = InformationSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = InformationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # serializer.save()
    #         send_mail(
    #             serializer.subject,
    #             serializer.information,
    #             "mehrshad83sadeghi@gmail.com",
    #             serializer.to_email
    #         )
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        """ send email """
        subject = request.data['subject']
        to_email = request.data['to_email']
        information = request.data['information']
        send_mail(
                    subject,
                    to_email,
                    "mehrshad83sadeghi@gmail.com",
                    [information]
                )
        serializer = InformationSerializer(request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

