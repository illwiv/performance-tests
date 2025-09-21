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

create_credit_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=create_account_payload)
create_credit_account_response_data = create_credit_account_response.json()

print("Create credit account response:", create_credit_account_response_data)
print("Status code", create_credit_account_response.status_code)

create_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": create_credit_account_response_data['account']['cards'][0]['id'],
  "accountId":create_credit_account_response_data['account']['id'],
  "category": "taxi"
}
create_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=create_purchase_operation_payload)
create_purchase_operation_response_data = create_purchase_operation_response.json()

print("Create purchase operation response:", create_purchase_operation_response_data)
print("Status code", create_purchase_operation_response.status_code)

get_operation_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{create_purchase_operation_response_data['operation']['id']}")
get_operation_receipt_response_data = get_operation_receipt_response.json()

print("Get operation receipt response:", get_operation_receipt_response_data)
print("Status code", get_operation_receipt_response.status_code)

