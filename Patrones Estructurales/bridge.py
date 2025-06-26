class Customer:
    def __init__(self, name, country, is_active, total_spent):
        self.name = name
        self.country = country
        self.is_active = is_active
        self.total_spent = total_spent
    def __str__(self):
        return f"{self.name} - {self.country} - ${self.total_spent:.2f}"
class CustomerQuery:
    def __init__(self, customers):
        self._original = customers  
        self._filtered = customers  
    def active(self):
        self._filtered = [c for c in self._filtered if c.is_active]
        return self
    def from_country(self, country):
        self._filtered = [c for c in self._filtered if c.country == country]
        return self
    def with_min_spent(self, min_spent):
        self._filtered = [c for c in self._filtered if c.total_spent >= min_spent]
        return self
    def get(self):
        return self._filtered
if __name__ == "__main__":
    customers = [
        Customer("John Doe", "USA", True, 1500),
        Customer("Roberto Argueta", "El Salvador", True, 1000),
        Customer("Alice Johnson", "USA", False, 1200),
    ]
    query = CustomerQuery(customers)
    result = query.active().from_country("USA").with_min_spent(1000).get()

    for customer in result:
        print(customer)