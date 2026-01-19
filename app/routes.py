from flask import Blueprint

# Blueprint will be defined here
bp = Blueprint('api', __name__)

@bp.route('/health')
def health_check():
    return {'status': 'healthy'}
