from apscheduler.schedulers.background import BackgroundScheduler
from app.main import process_emails  # function that reads & replies

scheduler = BackgroundScheduler()
scheduler.add_job(process_emails, 'interval', seconds=30, max_instances=1)
scheduler.start()