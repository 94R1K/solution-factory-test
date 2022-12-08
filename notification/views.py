from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        queryset_mailing = Mailing.objects.all()
        get_object_or_404(queryset_mailing, pk=pk)
        queryset = Message.objects.filter(mailing_id=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullinfo(self, request):
        total_count = Mailing.objects.count()
        mailing = Mailing.objects.values('id')
        content = {
            'Общее количество рассылок': total_count,
            'Количество отправленных сообщений': ''
        }
        result = {}

        for row in mailing:
            res = {'Всего сообщений': 0, 'Отправлено': 0, 'Не отправлено': 0}
            mail = Message.objects.filter(mailing_id=row['id']).all()
            group_sent = mail.filter(sending_status='Отправлено').count()
            group_no_sent = mail.filter(sending_status='Не отправлено').count()
            res['Всего сообщений'] = len(mail)
            res['Отправлено'] = group_sent
            res['Не отправлено'] = group_no_sent
            result[row['id']] = res

        content['Количество отправленных сообщений'] = result
        return Response(content)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
