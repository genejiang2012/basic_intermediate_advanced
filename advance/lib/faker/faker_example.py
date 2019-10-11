from faker import Faker
import csv

# fake.first_name()
# fake.last_name()
# fake.postalcode()
# fake.company()
# fake.credit_card_expire
# fake.credit_card_security_code
# fake.street_name
# fake.city()

fake = Faker()

RECORD_COUNT = 1000
with open("fake_date.csv", "w", newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'email', 'address', 'postalcode',
                  'city', 'state',
                  'country']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(RECORD_COUNT):
        writer.writerow(
            {
                'first_name': fake.name(),
                'last_name': fake.name(),
                'email': fake.email(),
                'address': fake.street_aname(),
                'postalcode': fake.postalcode(),
                'city': fake.city(),
                'state': fake.state(),
                'country': fake.country()
            }

        )
