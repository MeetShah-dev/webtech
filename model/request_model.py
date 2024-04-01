"""
    File: request_model
    Location: /model/request_model.py

    This module provides various functionalities for request controller file.

"""
import psycopg2
from datetime import datetime
from db.db_declarative_config import Engine
from logs.logging_handler import success_logger, error_logger
from model.db_model import Magazine, Job
from sqlalchemy import func, Text


class RequestOperations:
    """
        Class containing functions for request controller file.
    """

    @staticmethod
    def get_release_content(magazine_title, release_date, current_date, reschedule, magazine_id):
        """
        This function is used to get all content for release of magazine.
        """
        msg = []
        magazine_session = None
        egn = Engine()
        try:
            magazine_session = egn.get_engine_session()
            magazine_data = magazine_session.query(Magazine.id).filter(Magazine.flag == 'upcoming').all()
            magazine_content_id = [row[0] for row in magazine_data]
            if len(magazine_content_id) > 0:
                magazine_content_id = str(magazine_content_id[0])

                magazine_session.query(Magazine).filter(Magazine.id == magazine_content_id).with_for_update().update(
                    {Magazine.flag: 'released'}, synchronize_session=False)

                if reschedule and magazine_id is not None:
                    mag_id_from_job = magazine_id
                else:
                    current_new_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
                    job_mag_id = magazine_session.query(Job.magazine_id).filter(Job.magazine_title == magazine_title, func.cast(Job.updated_time, Text).ilike('%' + current_new_date + '%')).all()
                    job_mag = [data[0] for data in job_mag_id]
                    mag_id_from_job = job_mag[0]

                magazine_obj = Magazine(
                    id=mag_id_from_job,
                    title=magazine_title,
                    date_created=current_date,
                    date_released=release_date,
                    flag='upcoming')
                magazine_session.add(magazine_obj)
                magazine_session.commit()
                msg.append("Successfully updated the magazine")

                success_logger.info("=====7=====")
                success_logger.info("No upcoming draft of magazine remaining.")
        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(magazine_session)
        return msg

    @staticmethod
    def store_jobs(job_id, title, release_date, magazine_id):
        """
        This function is used to store all the job ids.
        """
        job_session = None
        egn = Engine()
        try:
            current_date = datetime.now()
            if not magazine_id:
                job_session = egn.get_engine_session()
                magazine_data = job_session.query(Magazine.id).filter(Magazine.flag == 'upcoming').all()
                magazine_content_id = [row[0] for row in magazine_data]

                job_mag_id = job_session.query(Job.magazine_id).all()
                job_mag_id = [data[0] for data in job_mag_id]

                if len(magazine_content_id) > len(job_mag_id):
                    magazine_content_id = str(magazine_content_id[0])
                    magazine_id = str(magazine_content_id)
                elif len(magazine_content_id) < len(job_mag_id):
                    magazine_id = max(job_mag_id) + 1
                else:
                    magazine_id = max(job_mag_id) + 1
            else:
                magazine_id = magazine_id

            job_session = egn.get_engine_session()
            job_obj = Job(
                magazine_id=magazine_id,
                job_id=job_id,
                magazine_title=title,
                updated_time=current_date,
                status='scheduled',
                release_date=release_date)
            job_session.add(job_obj)
            job_session.commit()

            success_logger.info("Job added successfully.")

        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(job_session)

    @staticmethod
    def remove_job(magazine_id):
        """
        This function is used to get magazine id for removing jobs.
        """
        rem_job_session = None
        egn = Engine()
        try:
            rem_job_session = egn.get_engine_session()
            rem_job_id_data = rem_job_session.query(Job.job_id, Job.magazine_title).filter(
                Job.magazine_id == magazine_id, Job.status == 'scheduled').all()
            job_id = rem_job_id_data[0][0]
            mag_title = rem_job_id_data[0][1]
            success_logger.info("Job id fetched successfully.")
        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(rem_job_session)
        return job_id, mag_title

    @staticmethod
    def update_status(magazine_id):
        """
        This function is used to update status if magazine has been rescheduled.
        """
        status_session = None
        egn = Engine()
        try:
            # current_date = datetime.now()
            status_session = egn.get_engine_session()
            status_session.query(Job). \
                filter(Job.magazine_id == magazine_id, Job.status == 'scheduled'). \
                with_for_update().update(
                {Job.status: 'rescheduled'},
                synchronize_session=False)
            status_session.commit()
            success_logger.info("Job id fetched successfully.")
        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(status_session)

    @staticmethod
    def fetch_all_magazine():
        get_magazine_session = None
        egn = Engine()
        content_data = []
        try:
            get_magazine_session = egn.get_engine_session()
            get_magazine_data_from_scheduled_jobs = get_magazine_session.query(Job.magazine_id). filter(Job.status == 'scheduled').all()
            jobs_magazine_id = [row[0] for row in get_magazine_data_from_scheduled_jobs]
            get_magazine_data_from_magazine = get_magazine_session.query(Magazine.id).all()
            magazine_id = [row[0] for row in get_magazine_data_from_magazine]

            magazine_ids_left_to_release = list(set(jobs_magazine_id) - set(magazine_id))
            if len(magazine_ids_left_to_release) > 0:
                for ids in magazine_ids_left_to_release:
                    ids = str(ids)

                    data_for_reschedule = get_magazine_session.query(Job.magazine_id, Job.magazine_title, Job.updated_time, Job.release_date).filter(Job.magazine_id == ids, Job.status == 'scheduled').all()
                    rows = [row for row in data_for_reschedule]
                    content = {"magazine_id": rows[0][0], "magazine_title":rows[0][1], "created_date_time": rows[0][2], "release_date_time": rows[0][3]}
                    content_data.append(content)
            else:
                content_data = "No magazine found for reschedule."
        except (Exception, psycopg2.errors) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(get_magazine_session)
        return content_data
