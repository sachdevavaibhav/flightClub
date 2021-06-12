import requests
from flight_data import FlightData

# API_KEY = "Ux8132fkc2wz_xWlS8lqPA1ynTP821QA"
# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:
    def __init__(self):
        self.API_KEY = "Ux8132fkc2wz_xWlS8lqPA1ynTP821QA"
        self.TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city):
        headers = {'apikey': self.API_KEY}
        parameters = {'term': city, "location_types": "city"}
        response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/locations/query", headers=headers, params=parameters)
        response.raise_for_status()
        destination_code = response.json()["locations"][0]["code"]
        return destination_code

    def check_flights(self, origin_city_code, destination_city_code, from_date, to_date):
        headers = {'apikey': self.API_KEY}
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from ": from_date,
            "date_to ": to_date,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,

        }
        response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/v2/search", headers=headers, params=parameters)
        try:
            data = response.json()["data"][0]
        except IndexError:
            parameters['max_stopovers'] = 1
            response = requests.get(url=f"{self.TEQUILA_ENDPOINT}/v2/search", headers=headers, params=parameters)
            try:
                data = response.json()["data"][0]
                
                flight_data = FlightData(
                    price=data['price'],
                    origin_city=data['route'][0]['cityFrom'],
                    origin_airport=data['route'][0]['flyFrom'],
                    destination_city=data['route'][1]['cityTo'],
                    destination_airport=data['route'][1]['flyTo'],
                    depart_date=data['route'][0]['local_departure'].split('T')[0],
                    return_date=data['route'][2]['local_departure'].split('T')[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city[0]}: £{flight_data.price}")
                return flight_data
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                stop_overs=0,
                depart_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0]
            )
            print(f"{flight_data.destination_city[0]}: £{flight_data.price}")

            return flight_data

