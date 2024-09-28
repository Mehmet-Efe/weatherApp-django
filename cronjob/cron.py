from django_cron import CronJobBase, Schedule
from web.models import jobs
from .getCity import getCity

class job(CronJobBase):
    
    RUN_EVERY_MINS = 1 # every 1 minutes
    RUN_AT_TIMES = ['23:59']

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
    
    code = 'Cron job #1'    # a unique code

    def do(self):
        
        data = jobs.objects.all()
        for part in data:
            getCity(part.city_name)
            
        
