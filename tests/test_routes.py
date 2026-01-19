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

def test_list_tasks(client):
    """US-02: Test retrieving all tasks"""
    # Create a task first
    client.post('/tasks', json={'title': 'Task 1'})
    client.post('/tasks', json={'title': 'Task 2'})
    
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['title'] == 'Task 1'

def test_update_task(client):
    """US-03: Test updating a task"""
    # Create task
    client.post('/tasks', json={'title': 'Task to Update'})
    
    # Update it
    response = client.put('/tasks/1', json={
        'status': 'completed',
        'title': 'Updated Title'
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'completed'
    assert data['title'] == 'Updated Title'


