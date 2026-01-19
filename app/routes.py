from flask import Blueprint, request, jsonify, current_app
from app.models import db, Task
import logging

bp = Blueprint('api', __name__)

@bp.before_request
def log_request_info():
    current_app.logger.info(f"Request: {request.method} {request.url}")

@bp.after_request
def log_response_info(response):
    current_app.logger.info(f"Response: {response.status}")
    return response

@bp.route('/tasks', methods=['POST'])
def create_task():
    current_app.logger.info("Creating new task")
    data = request.get_json()

    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
        
    new_task = Task(
        title=data['title'],
        description=data.get('description', '')
    )
    
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error creating task: {str(e)}")
        return jsonify({'error': 'Database error'}), 500
    
    return jsonify(new_task.to_dict()), 201


@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = db.session.get(Task, id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.to_dict()), 200



@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = db.session.get(Task, id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    
    data = request.get_json()
    
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'status' in data:
        if data['status'] not in ['pending', 'completed']:
             return jsonify({'error': 'Invalid status'}), 400
        task.status = data['status']
        
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error updating task: {str(e)}")
        return jsonify({'error': 'Database error'}), 500

    return jsonify(task.to_dict()), 200

@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = db.session.get(Task, id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

        
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error deleting task: {str(e)}")
        return jsonify({'error': 'Database error'}), 500
    return '', 204





@bp.route('/health')
def health_check():
    return {'status': 'healthy'}
