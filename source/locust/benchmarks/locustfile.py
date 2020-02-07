from locust import HttpLocust, TaskSet
import json

def login(l):
    data = {
    }
    l.client.post('/login', data=data)

def logout(l):
    l.client.post("/logout")

def getMovies100(l):
    data = {
    }
    params = (
         ('filter', '{"limit":100}'),
    )
    l.client.get('/api/Movies', data=data, params=params)


def getMovies1000(l):
    data = {
    }
    params = (
         ('filter', '{"limit":1000}'),
    )
    l.client.get('/api/Movies', data=data, params=params)

def postMovie(l):
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

    l.client.post('/api/Movies', data=json.dumps(payload), cookies=cookies, headers=headers)


class UserBehavior(TaskSet):
    tasks = {
        getMovies100: 1,
        getMovies1000: 1, 
        postMovie: 10
    }

    # def on_start(self):
    #     login(self)

    # def on_stop(self):
    #     logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
