class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address

    def setCustomerId(self, customer_id):
        self.__customer_id = customer_id

    def getCustomerId(self):
        return self.__customer_id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setPhone(self, phone):
        self.__phone = phone

    def getPhone(self):
        return self.__phone

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def displayCustomerInfo(self):
        return f"Customer ID: {self.__customer_id}, Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone}, Address: {self.__address}"


class DeliveryRequest:
    def __init__(self, request_id, customer_id, items, delivery_date, status):
        self.__request_id = request_id
        self.__customer_id = customer_id
        self.__items = items
        self.__delivery_date = delivery_date
        self.__status = status

    def setRequestId(self, request_id):
        self.__request_id = request_id

    def getRequestId(self):
        return self.__request_id

    def setCustomerId(self, customer_id):
        self.__customer_id = customer_id

    def getCustomerId(self):
        return self.__customer_id

    def setItems(self, items):
        self.__items = items

    def getItems(self):
        return self.__items

    def setDeliveryDate(self, delivery_date):
        self.__delivery_date = delivery_date

    def getDeliveryDate(self):
        return self.__delivery_date

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status

    def displayDeliveryRequestInfo(self):
        return f"Request ID: {self.__request_id}, Customer ID: {self.__customer_id}, Items: {self.__items}, Delivery Date: {self.__delivery_date}, Status: {self.__status}"


class Admin:
    def __init__(self, admin_id, name, email, department, access_level):
        self.__admin_id = admin_id
        self.__name = name
        self.__email = email
        self.__department = department
        self.__access_level = access_level

    def setAdminId(self, admin_id):
        self.__admin_id = admin_id

    def getAdminId(self):
        return self.__admin_id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setDepartment(self, department):
        self.__department = department

    def getDepartment(self):
        return self.__department

    def setAccessLevel(self, access_level):
        self.__access_level = access_level

    def getAccessLevel(self):
        return self.__access_level

    def displayAdminInfo(self):
        return f"Admin ID: {self.__admin_id}, Name: {self.__name}, Email: {self.__email}, Department: {self.__department}, Access Level: {self.__access_level}"


class Payment:
    def __init__(self, payment_id, request_id, amount, payment_date, payment_method):
        self.__payment_id = payment_id
        self.__request_id = request_id
        self.__amount = amount
        self.__payment_date = payment_date
        self.__payment_method = payment_method

    def setPaymentId(self, payment_id):
        self.__payment_id = payment_id

    def getPaymentId(self):
        return self.__payment_id

    def setRequestId(self, request_id):
        self.__request_id = request_id

    def getRequestId(self):
        return self.__request_id

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setPaymentDate(self, payment_date):
        self.__payment_date = payment_date

    def getPaymentDate(self):
        return self.__payment_date

    def setPaymentMethod(self, payment_method):
        self.__payment_method = payment_method

    def getPaymentMethod(self):
        return self.__payment_method

    def displayPaymentInfo(self):
        return f"Payment ID: {self.__payment_id}, Request ID: {self.__request_id}, Amount: {self.__amount}, Payment Date: {self.__payment_date}, Payment Method: {self.__payment_method}"


class DeliveryStaff:
    def __init__(self, staff_id, name, phone, vehicle, is_available):
        self.__staff_id = staff_id
        self.__name = name
        self.__phone = phone
        self.__vehicle = vehicle
        self.__is_available = is_available

    def setStaffId(self, staff_id):
        self.__staff_id = staff_id

    def getStaffId(self):
        return self.__staff_id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhone(self, phone):
        self.__phone = phone

    def getPhone(self):
        return self.__phone

    def setVehicle(self, vehicle):
        self.__vehicle = vehicle

    def getVehicle(self):
        return self.__vehicle

    def setIsAvailable(self, is_available):
        self.__is_available = is_available

    def getIsAvailable(self):
        return self.__is_available

    def displayDeliveryStaffInfo(self):
        return f"Staff ID: {self.__staff_id}, Name: {self.__name}, Phone: {self.__phone}, Vehicle: {self.__vehicle}, Available: {self.__is_available}"


# Example Usage:
customer = Customer(1, "Fatmah Alzahmi", "Fatmah@example.com", "123456789", "123 Street")
delivery_request = DeliveryRequest(101, customer.getCustomerId(), "Product A", "2025-03-01", "Pending")
admin = Admin(1, "Admin Name", "admin@example.com", "Logistics", 3)
payment = Payment(1, delivery_request.getRequestId(), 50.0, "2025-03-01", "Credit Card")
delivery_staff = DeliveryStaff(1, "Staff Name", "987654321", "Van", True)

# Displaying customer info:
print(customer.displayCustomerInfo())
print(delivery_request.displayDeliveryRequestInfo())
print(admin.displayAdminInfo())
print(payment.displayPaymentInfo())
print(delivery_staff.displayDeliveryStaffInfo())
