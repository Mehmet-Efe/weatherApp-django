from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import scheduler

def start():
  sched = BackgroundScheduler()
  sched.add_job(scheduler,'interval', hours=10)
  print("iş başladı")
  sched.start()