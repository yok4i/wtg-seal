# locust file generated by wtg-seal (release {})
# See https://github.com/mchoji/wtg-seal for more information

from locust import HttpUser, TaskSet, task
from scipy.stats import pareto


class UserTestSet(TaskSet):
    @task(0)
    def getdoc0(self):
        self.client.get("/1.txt")

    @task(3)
    def getdoc1(self):
        self.client.get("/1.txt")
        self.client.get("/2.txt")
        self.client.get("/3.txt")

    @task(0)
    def getdoc2(self):
        self.client.get("/4.txt")
        self.client.get("/5.txt")
        self.client.get("/6.txt")
        self.client.get("/7.txt")
        self.client.get("/8.txt")
        self.client.get("/9.txt")
        self.client.get("/10.txt")


class WebUserLocust(HttpUser):
    weight = 2
    tasks = [UserTestSet]
    pareto_obj = pareto(b=1.4, scale=1)
    pareto_obj.random_state = 2

    def wait_time(self):
        return self.pareto_obj.rvs()
