from celery import  shared_task


@shared_task(bind =True)
def test_celery(self):
    for i in range(1,7):
        print(i,end="")
    return  "Done2"