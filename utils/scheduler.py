from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from loguru import logger

scheduler = AsyncIOScheduler()

def schedule_task(task_name, task_func, run_at: datetime):
    logger.info(f"Scheduling task {task_name} at {run_at}")
    scheduler.add_job(task_func, "date", run_date=run_at, id=task_name)

def start_scheduler():
    scheduler.start()
    logger.info("Scheduler started")