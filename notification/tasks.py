import datetime
import os

import pytz
import requests
from celery.utils.log import get_task_logger
from dotenv import load_dotenv
from notification_test.celery import app

from .models import Client, Mailing, Message

logger = get_task_logger(__name__)

load_dotenv()
URL = os.getenv('URL')
TOKEN = os.getenv('TOKEN')


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, client_id, mailing_id, url=URL, token=TOKEN):
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone)
    mail = Mailing.objects.get(pk=mailing_id)

    if mail.time_start <= now.time() <= mail.time_end:
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            logger.error(f'Ошибка в {data["id"]}')
            raise self.retry(exc=exc)
        else:
            logger.info(f'ID сообщения: {data["id"]}, '
                        f'Отправка статуса: "Отправлено"')
            Message.objects.filter(
                pk=data['id']).update(
                sending_status='Отправлено'
            )
    else:
        time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
                     int(mail.time_start.strftime('%H:%M:%S')[:2]))
        logger.info(f'ID сообщения: {data["id"]}, '
                    f'В данный момент нельзя отправить сообщение, '
                    f'перезапуск задачи через {60 * 60 * time} секунд.')
        return self.retry(countdown=60 * 60 * time)
