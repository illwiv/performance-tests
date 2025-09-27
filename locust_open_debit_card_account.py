from locust import HttpUser, between, task
from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(1, 3)
    user_id: str

    def on_start(self) -> None:
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number(),
        }

        response = self.client.post("/api/v1/users", json=request)
        self.user_id = response.json()['user']['id']

    @task
    def open_debit_card_account(self):
        request = {
            "userId": self.user_id,
        }
        self.client.post(
            f"/api/v1/accounts/open-debit-card-account",
            json=request,
        )
