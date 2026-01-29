from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        # Login once per user (important for realistic load)
        self.client.post("/login", data={
            "username": "PESXUGXXCSXXX",
            "password": "PESXUGXXCSXXX"
        })

    @task
    def view_events(self):
        with self.client.get("/events", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to load events")
