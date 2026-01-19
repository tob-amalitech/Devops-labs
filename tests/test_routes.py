def test_create_task(client):
    """US-01: Test creating a new task"""
    response = client.post('/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task'
    })
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test Task'
    assert data['description'] == 'This is a test task'
    assert data['status'] == 'pending'
    assert 'id' in data
    assert 'created_at' in data

def test_create_task_invalid_input(client):
    """US-01: Test creating task with missing title"""
    response = client.post('/tasks', json={
        'description': 'Missing title'
    })
    
    assert response.status_code == 400
