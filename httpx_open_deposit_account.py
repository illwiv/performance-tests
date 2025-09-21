import httpx
import time

create_user_payload = {
    "email": f"user{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Create user response:", create_user_response_data)
print("Status code", create_user_response.status_code)

create_account_payload = {
  "userId": create_user_response_data['user']['id']
}

create_deposit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=create_account_payload)
create_deposit_account_data = create_deposit_account_response.json()

print("Create deposit account response:", create_deposit_account_data)
print("Status code", create_deposit_account_response.status_code)
