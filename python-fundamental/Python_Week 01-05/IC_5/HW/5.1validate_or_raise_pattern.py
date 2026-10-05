def require(condition, message, exc=ValueError):

    if not condition:
        raise exc(message)

def book_flight(passenger, from_city, to_city, date):
    require(passenger, "passenger name is required")
    require(from_city != to_city, "from and to cities must differ")
    require(date.year >= 2026, "cannot book flights in the past")
    require(len(passenger) >= 2, "passenger name too short")

    return {
        "passenger": passenger,
        "from_city": from_city,
        "to_city": to_city,
        "date": date,
        "status": "booked",

    }
