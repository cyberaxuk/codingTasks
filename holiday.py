# holiday.py - Task 6 - Practical Task 1

# Calculate the total cost of a holiday

# List City, Flight Cost, Hotel Cost
city1 = {'city' : "Berlin", 'flight_cost' : 150, 'hotel_cost' : 99}
city2 = {'city' : "Paris", 'flight_cost' : 180, 'hotel_cost' : 120}
city3 = {'city' : "London", 'flight_cost' : 80, 'hotel_cost' : 125}
city4 = {'city' : "New York", 'flight_cost' : 300, 'hotel_cost' : 199}
city5 = {'city' : "Newcastle", 'flight_cost' : 80, 'hotel_cost' : 99}


# Ask user for inputs

# List options
print(f"1 - {city1['city']}")
print(f"2 - {city2['city']}")
print(f"3 - {city3['city']}")
print(f"4 - {city4['city']}")
print(f"5 - {city5['city']}")

      
# Dispay the options and ask for a choice (prob should have put some error checking into this)     
city_flight = input(f"\nWhich city are you visiting? :- ")

if city_flight == "1" :
   city_flight = city1

elif city_flight == "2" :
     city_flight = city2

elif city_flight == "3" :
    city_flight = city3

elif city_flight == "4" :
    city_flight = city4

elif city_flight == "5" :
    city_flight = city5

num_nights = int(input(f"How many nights are you staying? :- "))
rental_days = int(input(f"How many days do you need to a hire car? :- "))

# Define the functions to carry out the calculations
def hotel_cost(num_nights, city_flight):
    hotel_cost = city_flight['hotel_cost'] * num_nights
    print(f"\nYour total hotel cost for {num_nights} nights is £{hotel_cost}")
    return (hotel_cost)

def plane_cost(city_flight):
   plane_cost = city_flight['flight_cost'] * 2
   print(f"\nYour return flights to {city_flight['city']} is £{plane_cost}")
   return (plane_cost)

def car_rental(rental_days):
    daily_car_rental_cost = 45
    car_rental = rental_days * daily_car_rental_cost
    print(f"\nYour car rental for {rental_days} days is £{car_rental} ")
    return (car_rental)

def holiday_cost(hotel_cost, plane_cost, car_rental):
    hotel_cost(num_nights, city_flight)
    plane_cost(city_flight)
    car_rental(rental_days)
    holiday_cost = hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days)
    print(f"\n\nThe total cost for your holiday is £{holiday_cost} ")
    return (holiday_cost)

# Call the functions to calculate the costs and output the results
holiday_cost(hotel_cost, plane_cost, car_rental)



