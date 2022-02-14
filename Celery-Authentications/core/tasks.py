from celery import  shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from django.core.mail import send_mail
logger = get_task_logger(__name__)

@task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return('first_task_done')

@shared_task
def check_for_orders():      
    orders = Order.objects.all()
    now = datetime.datetime.utcnow().replace(tzinfo=utc,second=00, microsecond=00)
    week_old = now - datetime.timedelta(week=1)
    for order in orders:
        if order.manu_date.date() == week_old.date():
            send_mail('Manufacturing Reminder',
                '{} is due {}'.format(order.id, order.manu_date),
                'dummyguy1680@gmail.com',
                ['gummy@gmail.com.com'])
            return None
        