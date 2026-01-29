from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        # Login once per simulated user
        self.client.post("/login", data={
            "username": "PESXUGXXCS447",
            "password": "PESXUGXXCS447"
        })

    @task
    def view_my_events(self):
        with self.client.get("/my-events", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to load my-events")
