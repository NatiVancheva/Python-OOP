
# class MovieWorld:
#     def __init__(self, name):
#         self.name = name
#         self.customers = []
#         self.dvds = []
    
#     @staticmethod
#     def dvd_capacity():
#         return 15
    
#     @staticmethod
#     def customer_capacity():
#         return 10
    
#     def add_customer(self, customer):
#         if len(self.customers) < self.customer_capacity():
#             self.customers.append(customer)

#     def add_dvd(self, dvd):
#         if len(self.dvds) < self.dvd_capacity():
#             self.dvds.append(dvd)

#     def rent_dvd(self, customer_id, dvd_id):
#         customer = next((c for c in self.customers if c.id == customer_id), None)
#         dvd = next((d for d in self.dvds if d.id == dvd_id), None)
#         if customer is None or dvd is None:
#             return "Customer or DVD not found"
#         if dvd in customer.rented_dvds:
#             return f"{customer.name} has already rented {dvd.name}"
        
#         if dvd.is_rented:
#             return "DVD is already rented"
        
#         if customer.age < dvd.age_restriction:
#             return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        
#         dvd.is_rented = True
#         customer.rented_dvds.append(dvd)
#         return f"{customer.name} has successfully rented {dvd.name}"
    
#     def return_dvd(self, customer_id, dvd_id):
#         customer = next((c for c in self.customers if c.id == customer_id), None)
#         dvd = next((d for d in self.dvds if d.id == dvd_id), None)
#         if customer is None or dvd is None:
#             return "Customer or DVD not found"

#         if dvd in customer.rented_dvds:
#             customer.rented_dvds.remove(dvd)
#             dvd.id_rented = False
#             return f"{customer.name} has successfully returned {dvd.name}"
#         return f"{customer.name} does not have that DVD"

#     def __repr__(self):
#         result = "\n".join([c.__repr__() for c in self.customers]) + "\n"
#         result += "\n".join([d.__repr__() for d in self.dvds])
#         return result
    
class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)

        if customer is None or dvd is None:
            return "Customer or DVD not found"

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)

        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)

        if customer is None or dvd is None:
            return "Customer or DVD not found"

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers_part = "\n".join(str(c) for c in self.customers)
        dvds_part = "\n".join(str(d) for d in self.dvds)

        if customers_part and dvds_part:
            return customers_part + "\n" + dvds_part
        return customers_part + dvds_part   