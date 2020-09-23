# https://ithelp.ithome.com.tw/articles/10218874?sc=pt
from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.background import BackgroundScheduler
import time
import urllib.request


sched = BlockingScheduler()

# @sched.scheduled_job('interval', day_of_week='mon-fri', minutes=20)
@sched.scheduled_job('cron', day_of_week='0-6', hour='10-23', minute='*/20')
def timed_job():
    # wake myself
    url2 = "https://wake-line-bot.herokuapp.com/"
    conn = urllib.request.urlopen(url2)
    today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(today, 'This job is run every day twenty minutes.')

@sched.scheduled_job('cron', day_of_week='0-6', hour=23, minute=59, second=20)
def work_in_shifts():
	# wake anther app before sleep
    url = "https://van-linebot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
    today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(today, 'This job is wake aonther server every day at 07:59:59 UTC+8.')


sched.start()