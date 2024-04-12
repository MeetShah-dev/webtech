"""
    File: request_controller
    Location: /controller/request_controller.py

    This module provides various endpoints for request model file.

"""
from flask import jsonify, request
from logs.logging_handler import error_logger, success_logger
from controller import app
from model.request_model import RequestOperations


@app.route("/update_like_dislike", methods=['POST'])
def get_likes():
    """
        This API is used to get the likes/dislikes by the user for the blogs.
    """
    response_dict = {}
    try:
        post_data = request.get_json(force=True)
        likes_dislikes = post_data['like_dislike'].lower()
        blog_id = post_data['blog_id']
        user_id = post_data['user_id']

        data = RequestOperations()

        if likes_dislikes == 'true':
            data.get_likes(likes_dislikes, blog_id, user_id)
        else:
            data.get_dislikes(likes_dislikes, blog_id, user_id)
        response_dict['status'] = '200'
        response_dict['message'] = 'Data updated successfully.'
        success_logger.info("Likes updated in database table")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        error_logger.exception(error)
    return jsonify(response_dict)

@app.route("/add_comment", methods=['POST'])
def adding_comments():
    """
        This API is used to add/delete the blogs.
    """
    response_dict = {}
    try:
        post_data = request.get_json(force=True)
        text = post_data['text'].lower()
        blog_id = post_data['blog_id']
        user_id = post_data['user_id']

        data = RequestOperations()
        data.add_comments(text, blog_id, user_id)

        response_dict['status'] = '200'
        response_dict['message'] = 'Data updated successfully.'
        success_logger.info("Likes updated in database table")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        error_logger.exception(error)
    return jsonify(response_dict)

@app.route("/edit_comment", methods=['POST'])
def redit_comments():
    """
        This API is used to edit the blogs mistakenly added.
    """
    response_dict = {}
    try:
        post_data = request.get_json(force=True)
        text = post_data['updated_text'].lower()
        blog_id = post_data['blog_id']
        user_id = post_data['user_id']
        old_date_time = post_data['previous_date_time']

        data = RequestOperations()
        data.edit_comments(text, blog_id, user_id, old_date_time)

        response_dict['status'] = '200'
        response_dict['message'] = 'Data updated successfully.'
        success_logger.info("Comment updated in database table")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        error_logger.exception(error)
    return jsonify(response_dict)

@app.route("/get_all_comments", methods=['GET'])
def get_comments():
    """
        This API is used to get all the comments.
    """
    response_dict = {}
    try:
        data = RequestOperations()
        comments = data.get_comment()
        response_dict['status'] = '200'
        response_dict['message'] = 'Data fetched successfully.'
        response_dict['data'] = comments
        success_logger.info("All comments fetched successfully.")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        response_dict['data'] = "No data found."
        error_logger.exception(error)
    return jsonify(response_dict)

@app.route("/delete_comment", methods=['DELETE'])
def delete_comments():
    """
        This API is used to delete the comments mistakenly added.
    """
    response_dict = {}
    try:
        post_data = request.get_json(force=True)
        blog_id = post_data['blog_id']
        user_id = post_data['user_id']
        comment_id = post_data['comment_id']

        data = RequestOperations()
        data.delete_comments(blog_id, user_id, comment_id)

        response_dict['status'] = '200'
        response_dict['message'] = 'Data updated successfully.'
        success_logger.info("Delete comment updated in database table")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        error_logger.exception(error)
    return jsonify(response_dict)

@app.route("/get_all_user_likes", methods=['GET'])
def get_all_user_likes():
    """
        This API is used to get all the user likes for the blogs.
    """
    response_dict = {}
    try:
        data = RequestOperations()
        all_like_data = data.get_all_likes_for_users()
        response_dict['status'] = '200'
        response_dict['message'] = 'Data fetched successfully.'
        response_dict['data'] = all_like_data
        success_logger.info("Delete comment updated in database table")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        error_logger.exception(error)
    return jsonify(response_dict)

@app.route("/get_all_user_dislikes", methods=['GET'])
def get_all_user_dislikes():
    """
        This API is used to get all the user dislikes for the blogs.
    """
    response_dict = {}
    try:
        data = RequestOperations()
        all_like_data = data.get_all_dislikes_for_users()
        response_dict['status'] = '200'
        response_dict['message'] = 'Data fetched successfully.'
        response_dict['data'] = all_like_data
        success_logger.info("Delete comment updated in database table")
    except Exception as error:
        response_dict['status'] = '500'
        response_dict['message'] = 'Please check logs for the error occurred.'
        error_logger.exception(error)
    return jsonify(response_dict)
