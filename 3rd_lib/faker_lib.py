from faker import Faker, Factory

fake = Faker("zh_CN")


for _ in range(5):
    print(fake.address())