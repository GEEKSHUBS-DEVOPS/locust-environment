from locust import HttpUser, task
import json


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/api/Movies")       
        
    @task 
    def postMovie(self):
        headers = {
            "Authorization": "Bearer XXX", 
            "Content-Type": "application/json" 
        }

        cookies = {
            'Fuck-The-Cookie: XXXX': 'YYYY',
        }
        
        params = (
        )

        payload = {
            'title': 'movie title',
            'overview': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry  standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
            'poster_path': 'https://es.web.img3.acsta.net/r_1280_720/pictures/18/02/21/10/05/2137559.jpg'
        }

        self.client.post('/api/Movies', data=json.dumps(payload), cookies=cookies, headers=headers)
            