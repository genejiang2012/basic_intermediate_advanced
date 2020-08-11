class Model:
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 20},
        'short-video': {'number': 1000, 'price': 60}
    }


class View:
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print("For {} {} message,  you may pay {}.".format(
                Model.services[svc]['number'],
                svc,
                Model.services[svc]['price']))


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)


class Client:
    controller = Controller()
    print("Serices Proviced")
    controller.get_services()
    print("Prices")
    controller.get_pricing()


client = Client()
