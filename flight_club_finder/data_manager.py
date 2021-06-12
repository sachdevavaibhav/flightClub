import requests


class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "SHEETY API HERE"
        self.destination_data = None
        self.email_list = []

    def get_destination_data(self):
        sheety_response = requests.get(url=f"{self.SHEETY_ENDPOINT}/prices")
        sheety_data = sheety_response.json()
        self.destination_data = sheety_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(url=f"{self.SHEETY_ENDPOINT}/prices/{row['id']}", json=new_data)
            response.raise_for_status()

    def get_email_list(self):
        sheety_response = requests.get(url=f"{self.SHEETY_ENDPOINT}/users")
        data = sheety_response.json()["users"]
        for row in data:
            email = row["email"]
            self.email_list.append(email)
        return self.email_list




