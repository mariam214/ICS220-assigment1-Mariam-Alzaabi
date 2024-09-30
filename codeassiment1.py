class User: #start with  the user class
    def __init__(self, name, email, phone, userID, password):#use init function to initializentheme
        self.name = name# these are the attributes of the user class
        self.email = email
        self.phone = phone
        self.userID = userID
        self.password = password

    # So now i will do the Getter and Setter methods taht i have already identified
    def get_name(self):
        return self.name

    def set_name(self, name):#we will use the def function for all of them
        self.name = name

    def authenticate(self, email, password):
        # in this specific function it is able to check if the user's credentials is valid
        pass

    def view_reservation(self):
        # this function is ablr to return the user's reservation details
        pass
class Reservation:#now i will do the second class which is reservation
    def __init__(self, reservationID, checkInDate, checkOutDate, totalCost, roomNumber, userID):#we will inistialize the attributes
        self.reservationID = reservationID
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.totalCost = totalCost
        self.roomNumber = roomNumber
        self.userID = userID

    # Getter and Setter methods
    def get_reservation_details(self):#i will use the methods that i listed when i did the class diagram for reservation
        # This function would return the reservation details for the user
        pass

    def modify_reservation(self, newDate):
        # in this function it will allow user to  modify the reservation details
        pass

    def cancel_reservation(self):
        # Using this function we are able to cancel the reservation
        pass
class Room:#now we are moving to the third class which is room
    def __init__(self, roomNumber, roomType, pricePerNight, isAvailable, floor, view):#we are going to initialize the attributes
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.pricePerNight = pricePerNight
        self.isAvailable = isAvailable
        self.floor = floor
        self.view = view

    # Getter methods
    def check_availability(self):
        return self.isAvailable

    def get_price(self):
        return self.pricePerNight
class Payment:
    def __init__(self, paymentID, amount, paymentStatus, paymentMethod):
        self.paymentID = paymentID
        self.amount = amount
        self.paymentStatus = paymentStatus
        self.paymentMethod = paymentMethod

    # Now we are going to add the available Payment methods
    def process_payment(self):
        # This function would process the payment
        pass

    def refund_payment(self):
        # In this function we can see that it will be able to  process the refund
        pass
class Service:
    def __init__(self, serviceID, serviceName, serviceCost, serviceAvailability):
        self.serviceID = serviceID
        self.serviceName = serviceName
        self.serviceCost = serviceCost
        self.serviceAvailability = serviceAvailability

    def add_service_to_reservation(self):
        # During this function it would add a service to a reservation if the user want to add
        pass

    def check_service_availability(self):
        return self.serviceAvailability
class Feedback:
    def __init__(self, feedbackID, reservationID, rating, comments, date):
        self.feedbackID = feedbackID
        self.reservationID = reservationID
        self.rating = rating
        self.comments = comments
        self.date = date

    # Now its turn for the Feedback methods
    def submit_feedback(self):
        # This function would submit the feedback
        pass

    def view_feedback(self):
        # In This function It will return for us the feedback details
        pass
class Admin:#we will start now to add also the admin class to the system
    def __init__(self, adminID, name, email, phone):#initialize the admin attributes
        self.adminID = adminID
        self.name = name
        self.email = email
        self.phone = phone

    # Admin methods
    def manage_room_availability(self, roomID, availability):
        # This function is able to manage which room is available or not
        pass

    def manage_reservations(self):
        # This function that im creating is to give the  admin acess  to manage reservations
        pass

    def view_feedback(self):
        # This function would allow admin to view feedback and use it to make the hotel service better
        pass
class Notification:
    def __init__(self, notificationID, notificationType, contactMethod, userID):#initizilse the notifacation class attributes
        self.notificationID = notificationID
        self.notificationType = notificationType
        self.contactMethod = contactMethod
        self.userID = userID

    # Notification methods
    def set_notification_preferences(self, method, notificationType):
        # This function would allow users to set notification preferences
        pass

    def send_notification(self, userID, message):
        # This function would send notifications
        pass
class LoyaltyProgram:
    def __init__(self, programID, userID, pointsBalance, status):
        self.programID = programID
        self.userID = userID
        self.pointsBalance = pointsBalance
        self.status = status

    # Loyalty program methods
    def enroll_user(self, userID):
        # This function would enroll the user into the loyalty program
        pass

    def add_points(self, points):
        # This function would add points to the user’s balance
        pass

    def redeem_points(self, points):
        # This function would redeem points for discounts or offers
        pass
# Creating a User object
user = User(name="Ted Vera", email="tedvera@mac.com", phone="505-661-1110", userID=15549850358, password="password123")

# Creating a Reservation object
reservation = Reservation(reservationID=52523687, checkInDate="2010-08-22 15:00", checkOutDate="2010-08-24 12:00", totalCost=201.48, roomNumber=1, userID=user.userID)

# Creating a Room object
room = Room(roomNumber=1, roomType="2 Queen Beds", pricePerNight=89.95, isAvailable=False, floor=2, view="")

# Creating a Payment object
payment = Payment(paymentID=9904, amount=201.48, paymentStatus="Completed", paymentMethod="Mastercard (ending in 9904)")

# Displaying the decorated information
#Now to test my code, i iwll create objects to populate data and display it in the outcome when we run the code
print("🛎️  *Your Reservation Is Confirmed!* 🛎️")#i decorated it to look like an actual recipt and make it fun
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✨ Thank you for your reservation. Please print your hotel receipt and show it at check-in. ✨")
print(f"👤 *Your Name*: {user.get_name()}")
print(f"📧 *Your Email*: {user.email}")
print(f"🆔 *Priceline Trip Number*: {user.userID}")
print(f"🏨 *Hotel Confirmation Number*: {reservation.reservationID}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("\n🏢  *Hotel Information*  🏢")
print("Comfort Inn & Suites Los Alamos")
print("2455 Trinity Drive, Los Alamos, NM 87544")
print(f"📞 *Phone*: {user.phone}")
print(f"📅 *Check-In*: {reservation.checkInDate}")
print(f"📅 *Check-Out*: {reservation.checkOutDate}")
print(f"🌙 *Number of Nights*: 2")
print(f"🛏️ *Room Type*: {room.roomType}")
print(f"🔑 *Room Number*: {room.roomNumber}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("\n💳  *Summary of Charges*  💳")
print(f"👤 *Billing Name*: {user.get_name()}")
print(f"💳 *Credit Card*: {payment.paymentMethod}")
print(f"💲 *Room Cost (avg. per room, per night)*: ${room.pricePerNight}")
print(f"🏨 *Rooms*: 1")
print(f"🌙 *Nights*: 2")
print(f"💲 *Room Subtotal*: ${room.pricePerNight * 2:.2f}")
print(f"💲 *Taxes and Fees*: ${reservation.totalCost - (room.pricePerNight * 2):.2f}")
print(f"💲 *Total Charges*: ${reservation.totalCost}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("💵 *Prices are in US dollars.* 💵")
print("📜 *Thank you for choosing Comfort Inn & Suites Los Alamos!* 😊")
