import os
from locust import HttpUser, task, TaskSet


class UserBehavior(TaskSet):
    @task
    def access_baidu_page(self):
        self.client.get('/')


class WebsiteUser(HttpUser):
    task_set = UserBehavior
    max_wait = 6000
    min_wait = 3000


if __name__ == '__main__':
    os.system("locust -f locust_demo.py --host=https://www.baidu.com/")
