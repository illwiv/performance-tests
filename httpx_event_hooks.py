from httpx import Client, Request, Response
from datetime import datetime


def log_request(request: Request):
    datetime.now()
    request.extensions['start_time'] = datetime.now()
    print(f'{request.method} {request.url}')

def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print(f'{response.status_code} {response.url} {duration}')


client = Client(base_url='http://localhost:8003', event_hooks={"request": [log_request], "response": [log_response]})

response = client.get('/api/v1/users/3fa85f64-5717-4562-b3fc-2c963f66afa6')