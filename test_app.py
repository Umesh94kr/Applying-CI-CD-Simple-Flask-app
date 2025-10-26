from app import app 

def test_app():
    client = app.test_client()   # <-- parentheses here
    response = client.get('/')   # now you can call .get()
    
    assert response.status_code == 200
    assert b'Hello World!' in response.data