from flask import Blueprint, request, jsonify
from app.models import db, Task

bp = Blueprint('api', __name__)

@bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
        
    new_task = Task(
        title=data['title'],
        description=data.get('description', '')
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_dict()), 201

@bp.route('/health')
def health_check():
    return {'status': 'healthy'}
