from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        destination_code = flight_search.get_destination_code(row["city"])

        row["iataCode"] = destination_code

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = (datetime.now() + timedelta(days=1)).strftime('$d/%m/%Y')
six_month_later = (datetime.now() + timedelta(days=180)).strftime('$d/%m/%Y')

email_list = data_manager.get_email_list()

ORIGIN_IATA_CODE = 'LON'
for row in sheet_data:
    flight_data = flight_search.check_flights(origin_city_code=ORIGIN_IATA_CODE, destination_city_code=row['iataCode'],
                                              from_date=tomorrow, to_date=six_month_later)

    if flight_data is not None and flight_data.price < row['lowestPrice']:

        message = f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}" \
                  f"-{flight_data.origin_airport} to {flight_data.destination_city[0]}" \
                  f"-{flight_data.destination_airport[0]}, from {flight_data.depart_date[0]} to " \
                  f"{flight_data.return_date}."
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight_data.origin_airport}." \
               f"{flight_data.destination_airport[0]}.{flight_data.depart_date[0]}*{flight_data.destination_airport[0]}." \
               f"{flight_data.origin_airport}.{flight_data.return_date}"
        if flight_data.stop_overs[0] > 0:
            message += f"\nFlight has {flight_data.stop_overs[0]} stop over, via {flight_data.via_city}."

        notification_manager.send_email_notification(message, email_list, link)

# {'prices': [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]}
