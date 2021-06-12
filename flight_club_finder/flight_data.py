

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

