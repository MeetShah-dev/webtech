"""
    File: request_controller
    Location: /controller/request_controller.py

    This module provides various endpoints for request model file.

"""
from datetime import datetime
from flask import jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from logs.logging_handler import error_logger, success_logger
from controller import app
from model.request_model import RequestOperations


def get_magazine_content(title, release_date, current_date, reschedule, magazine_id):
    """
        Get all the magazine contents for release
    """
    try:
        response_dict = {}
        data = RequestOperations()
        title_of_magazine = title
        data.get_release_content(title_of_magazine, release_date, current_date, reschedule, magazine_id)
        success_logger.info("=====6=====")
        success_logger.info("Content updated in database.")
        response_dict['status'] = '200'
        response_dict['message'] = 'Successfully Fetched Data.'
        success_logger.info("===0====")
        success_logger.info("Successful function run for get_magazine_content function.")
        return response_dict
    except Exception as error:
        error_logger.exception(error)
        raise


schedule = BackgroundScheduler()
schedule.start()


@app.route("/schedule_magazine", methods=['POST'])
def get_scheduled_magazine():
    """
        Scheduling the job for the release of magazine.
    """
    try:
        response_dict = {}
        post_data = request.get_json(force=True)
        year = post_data['year']
        month = post_data['month']
        date = post_data['date']
        hour = post_data['hour']
        minute = post_data['minute']
        second = post_data['second']
        title = post_data['title']
        reschedule = False
        magazine_id = None

        current_date = datetime.now()
        release_date = datetime(year, month, date, hour, minute, second)

        if current_date > release_date or current_date == release_date:
            response_dict['status'] = '205'
            response_dict['message'] = 'Release date and time is less than or equal to the current date and time. Please schedule the magazine again'
            success_logger.info("Release of time error for the release of magazine.")

        else:
            job = schedule.add_job(get_magazine_content, trigger="cron", month=month, day=date, hour=hour, minute=minute,
                                   second=second,
                                   args=[title, release_date, current_date, reschedule,
                                         magazine_id])
            job_id = job.id

            data = RequestOperations()
            data.store_jobs(job_id, title, release_date, magazine_id=False)

            response_dict['status'] = '200'
            response_dict['message'] = 'Scheduled successfully.'
            success_logger.info("Successfully scheduled the release of magazine.")

    except Exception as error:
        error_logger.exception(error)
        raise
    return jsonify(response_dict)


@app.route("/reschedule_magazine", methods=['POST'])
def reschedule_magazine():
    """
        Scheduling the job for the release of magazine.
    """
    try:
        response_dict = {}
        reschedule = True
        post_data = request.get_json(force=True)
        year = post_data['year']
        month = post_data['month']
        date = post_data['date']
        hour = post_data['hour']
        minute = post_data['minute']
        second = post_data['second']
        magazine_id = post_data['magazine_id']

        current_date = datetime.now()
        release_date = datetime(year, month, date, hour, minute, second)

        if current_date > release_date or current_date == release_date:
            response_dict['status'] = '205'
            response_dict['message'] = 'Release date and time is less than or equal to the current date and time. Please reschedule the magazine again'
            success_logger.info("Release of time error for the release of magazine.")

        else:
            data = RequestOperations()
            job_id, title = data.remove_job(magazine_id)
            data.update_status(magazine_id)
            schedule.remove_job(job_id)
            job = schedule.add_job(get_magazine_content, trigger="cron", month=month, day=date, hour=hour, minute=minute,
                                   second=second,
                                   args=[title, release_date, current_date, reschedule, magazine_id])
            job_id = job.id
            data = RequestOperations()
            data.store_jobs(job_id, title, release_date, magazine_id)

            response_dict['status'] = '200'
            response_dict['message'] = 'Rescheduled successfully.'
            success_logger.info("Successfully scheduled the release of magazine.")

    except Exception as error:
        error_logger.exception(error)
        raise
    return jsonify(response_dict)
