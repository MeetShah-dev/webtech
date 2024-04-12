"""
    File: request_model
    Location: /model/request_model.py

    This module provides various functionalities for request controller file.

"""
import requests
import psycopg2
from datetime import datetime
from sqlalchemy import func, Text
from db.db_declarative_config import Engine
from logs.logging_handler import success_logger, error_logger
from model.db_model import Comment, Like, Blog


class RequestOperations:
    """
        Class containing functions for request controller file.
    """

    @staticmethod
    def get_likes(likes, blog_id, user_id):
        """
        This function is used to get all likes of the blogs.
        """
        like_session = None
        egn = Engine()
        try:
            current_date = datetime.now()
            like_session = egn.get_engine_session()

            data_updated = like_session.query(Like.value).filter(Like.user_id == user_id, Like.blog_id == blog_id)
            like_data = [data[0] for data in data_updated]

            if len(like_data) == 0:
                like_obj = Like(
                    timestamp=current_date,
                    blog_id=blog_id,
                    user_id=user_id,
                    value=likes)

                like_session.add(like_obj)
                like_session.commit()

                like_count_data = like_session.query(Blog.likes).filter(Blog.id == blog_id).all()
                like_count_data = [data[0] for data in like_count_data]

                like_count = like_count_data[0]
                like_count = like_count + 1

                like_session.query(Blog).filter(Blog.id == blog_id).with_for_update().update({
                    Blog.likes: like_count
                }, synchronize_session=False)
                like_session.commit()

                #Notification for adding likes
                consumer_id = user_id
                author_id = like_session.query(Blog.user_id).filter(Blog.id == blog_id).all()
                author_id = author_id[0][0]
                api_url = "<API_URL>"
                payload = {'type': 'like', 'blog': blog_id, 'sender': consumer_id, 'receiver': author_id}
                if requests.post(api_url, json=payload).status_code == 200:
                    success_logger.info("Notification api called successfully")

                success_logger.info("User has clicked like for the blog.")

            elif like_data[0] == 'false':
                like_session.query(Like).filter(Like.user_id == user_id, Like.blog_id == blog_id).with_for_update().update({
                    Like.value: likes, Like.timestamp: current_date
                }, synchronize_session=False)
                like_session.commit()

                like_count_data = like_session.query(Blog.likes).filter(Blog.id == blog_id).all()
                like_count_data = [data[0] for data in like_count_data]

                like_count = like_count_data[0]
                like_count = like_count + 1

                like_session.query(Blog).filter(Blog.id == blog_id).with_for_update().update({
                    Blog.likes: like_count
                }, synchronize_session=False)
                like_session.commit()
                success_logger.info("User has changed to like the blog.")

            else:
                success_logger.info("User has already liked the blog.")

        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(like_session)

    @staticmethod
    def get_dislikes(dislikes, blog_id, user_id):
        """
        This function is used to get all dislikes of the blogs.
        """
        dislike_session = None
        egn = Engine()
        try:
            current_date = datetime.now()
            dislike_session = egn.get_engine_session()

            # check if user has already liked the blog, then no increase in counter or like table.
            # check if like persist -- value update
            data_updated = dislike_session.query(Like.value).filter(Like.user_id == user_id, Like.blog_id == blog_id)
            dislike_data = [data[0] for data in data_updated]

            if len(dislike_data) == 0:
                dislike_obj = Like(
                    timestamp=current_date,
                    blog_id=blog_id,
                    user_id=user_id,
                    value=dislikes)

                dislike_session.add(dislike_obj)
                dislike_session.commit()

                dislike_count_data = dislike_session.query(Blog.likes).filter(Blog.id == blog_id).all()
                dislike_count = [data[0] for data in dislike_count_data]

                dislike_count = dislike_count[0]
                dislike_count = dislike_count - 1
                if dislike_count >= 0:
                    dislike_session.query(Blog).filter(Blog.id == blog_id).with_for_update().update({
                        Blog.likes: dislike_count,
                    }, synchronize_session=False)
                    dislike_session.commit()
                success_logger.info("Value added for disliking the blog.")

            elif dislike_data[0] == 'true':
                dislike_session.query(Like).filter(Like.user_id == user_id,
                                                Like.blog_id == blog_id).with_for_update().update({
                    Like.value: dislikes, Like.timestamp: current_date
                }, synchronize_session=False)
                dislike_session.commit()

                dislike_count_data = dislike_session.query(Blog.likes).filter(Blog.id == blog_id).all()
                dislike_count = [data[0] for data in dislike_count_data]

                dislike_count = dislike_count[0]
                dislike_count = dislike_count - 1
                if dislike_count >= 0:
                    dislike_session.query(Blog).filter(Blog.id == blog_id).with_for_update().update({
                        Blog.likes: dislike_count
                    }, synchronize_session=False)
                    dislike_session.commit()

                success_logger.info("User has changed to dislike the blog.")

            else:
                success_logger.info("User has already disliked the blog.")

        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(dislike_session)

    @staticmethod
    def add_comments(text, blog_id, user_id):
        """
        This function is used to add comments for the blogs.
        """
        add_comment_session = None
        egn = Engine()
        try:
            current_date = datetime.now()
            add_comment_session = egn.get_engine_session()

            comment_obj = Comment(
                timestamp=current_date,
                blog_id=blog_id,
                user_id=user_id,
                text=text)

            add_comment_session.add(comment_obj)
            add_comment_session.commit()

            add_comment_data = add_comment_session.query(Blog.comments).filter(Blog.id == blog_id).all()
            add_comment_count = [data[0] for data in add_comment_data]

            add_comment_count = add_comment_count[0]
            add_comment_count = add_comment_count + 1
            add_comment_session.query(Blog).filter(Blog.id == blog_id).with_for_update().update({
                Blog.comments: add_comment_count
            }, synchronize_session=False)
            add_comment_session.commit()

            #Notification for adding comments
            consumer_id = user_id
            author_id = add_comment_session.query(Blog.user_id).filter(Blog.id == blog_id).all()
            author_id = author_id[0][0]
            api_url = "<API_URL>"
            payload = {'type': 'comment', 'blog': blog_id, 'sender': consumer_id, 'receiver': author_id}
            if requests.post(api_url, json=payload).status_code == 200:
                success_logger.info("Notification api called successfully")

            success_logger.info("add comments function successfully implemented.")

        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(add_comment_session)

    @staticmethod
    def delete_comments(blog_id, user_id, comment_id):
        """
        This function is used to delete comments for the blogs.
        """
        delete_comment_session = None
        egn = Engine()
        try:
            delete_comment_session = egn.get_engine_session()
            delete_comment_session.query(Comment).filter(Comment.blog_id == blog_id, Comment.user_id == user_id, Comment.id == comment_id).delete()

            delete_comment_session.commit()

            delete_comment_data = delete_comment_session.query(Blog.comments).filter(Blog.id == blog_id).all()
            delete_comment_count = [data[0] for data in delete_comment_data]

            delete_comment_count = delete_comment_count[0]
            delete_comment_count = delete_comment_count - 1

            if delete_comment_count >= 0:
                delete_comment_session.query(Blog).filter(Blog.id == blog_id).with_for_update().update({
                    Blog.comments: delete_comment_count
                }, synchronize_session=False)
                delete_comment_session.commit()
            success_logger.info("delete comments function successfully implemented.")

        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(delete_comment_session)

    @staticmethod
    def edit_comments(text, blog_id, user_id, old_date_time):
        """
        This function is used to re-edit the comments for the blogs.
        """
        edit_comment_session = None
        egn = Engine()
        try:
            current_date = datetime.now()
            edit_comment_session = egn.get_engine_session()

            edit_comment_session.query(Comment).filter(Comment.blog_id == blog_id, Comment.user_id == user_id, func.cast(Comment.timestamp, Text).ilike('%' + old_date_time + '%')).with_for_update().update({Comment.text: text, Comment.timestamp: current_date}, synchronize_session=False)

            edit_comment_session.commit()

            success_logger.info("edit_comments function successfully implemented.")

        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(edit_comment_session)

    @staticmethod
    def get_comment():
        """
        This function is used to get all the comments for the blogs.
        """
        comment_session = None
        egn = Engine()
        comment_data = []
        try:
            current_date = datetime.now()
            comment_session = egn.get_engine_session()
            all_comment_data = comment_session.query(Comment.id, Comment.text, Comment.blog_id, Comment.user_id,
                                                     Comment.timestamp).all()
            rows = [row for row in all_comment_data]
            if len(rows) > 0:
                for row in rows:
                    content = {"id": row[0], "text": row[1], "blog_id": row[2],
                               "user_id": row[3], "date_time": row[4]}
                    comment_data.append(content)
            else:
                content = {"id": "Not Found", "text": "No Comment Available", "blog_id":"Not Found",
                           "user_id":"Not Found", "date_time":current_date}
                comment_data.append(content)
        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(comment_session)
        return comment_data

    @staticmethod
    def get_all_likes_for_users():
        """
        This function is used to get all likes made for the blogs.
        """
        like_session = None
        egn = Engine()
        comment_data = []
        try:
            current_date = datetime.now()
            like_session = egn.get_engine_session()
            all_like_data = like_session.query(Like.id, Like.blog_id, Like.user_id, Like.timestamp).filter(Like.value == 'true').all()
            rows = [row for row in all_like_data]
            if len(rows) > 0:
                for row in rows:
                    content = {"id": row[0], "Like": 'Like', "blog_id": row[1],
                               "user_id": row[2], "date_time": row[3]}
                    comment_data.append(content)
            else:
                content = {"id": "Not Found", "text": "No Comment Available", "blog_id": "Not Found",
                           "user_id": "Not Found", "date_time": current_date}
                comment_data.append(content)
        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(like_session)
        return comment_data

    @staticmethod
    def get_all_dislikes_for_users():
        """
        This function is used to get all likes made for the blogs.
        """
        dislike_session = None
        egn = Engine()
        comment_data = []
        try:
            current_date = datetime.now()
            dislike_session = egn.get_engine_session()
            all_dislike_data = dislike_session.query(Like.id, Like.blog_id, Like.user_id, Like.timestamp).filter(Like.value == 'false').all()
            rows = [row for row in all_dislike_data]
            if len(rows) > 0:
                for row in rows:
                    content = {"id": row[0], "Like": 'Dislike', "blog_id": row[1],
                               "user_id": row[2], "date_time": row[3]}
                    comment_data.append(content)
            else:
                content = {"id": "Not Found", "text": "No Comment Available", "blog_id": "Not Found",
                           "user_id": "Not Found", "date_time": current_date}
                comment_data.append(content)
        except (Exception, psycopg2.Error) as error:
            error_logger.exception(error)
            raise
        finally:
            egn.close_session(dislike_session)
        return comment_data
