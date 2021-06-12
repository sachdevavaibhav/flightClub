

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport,
                 depart_date, return_date, stop_overs=0, via_city=None):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city,
        self.destination_airport = destination_airport,
        self.stop_overs = stop_overs,
        self.via_city = via_city
        self.depart_date = depart_date,
        self.return_date = return_date


#
# now = datetime.now()
# from_date = (now.date() + timedelta(days=1)).strftime('%d/%m/%Y')
# to_date = (now.date() + timedelta(days=180)).strftime('%d/%m/%Y')
#
# print(from_date, to_date)
#
# SEARCH_API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
# API_KEY = "Ux8132fkc2wz_xWlS8lqPA1ynTP821QA"
# headers = {'apikey': API_KEY}
# params = {
#     "fly_from": "LON",
#     "fly_to": "PAR",
#     "date_from ": from_date,
#     "date_to ": to_date,
#     "flight_type": "round",
#     "curr": "GBP",
#     "one_for_city": 1,
#     "max_stopovers": 0,
#     "nights_in_dst_from": 7,
#     "nights_in_dst_to": 28,
#
# }
# response = requests.get(url=SEARCH_API_ENDPOINT, headers=headers, params=params)
# print(response)
# print(response.json()["data"])
# print(len(response.json()["data"]))
