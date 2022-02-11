from locust import HttpUser, task

class GudlftWebSite(HttpUser):

    @task
    def index(self):
        self.client.get(url="/")

    @task
    def showSummary(self):
        self.client.post(
            url="/showSummary",
            data={
                'email': 'user@locust.fr'})

    @task
    def book(self):
        self.client.get(url="/book/Locust test/Locust User")

    @task
    def purchasePlaces(self):
        self.client.post(
            url="/purchasePlaces",
            data={
                'competition': "Locust test",
                'club': 'Locust User',
                'places': '1'
            })

    @task
    def logout(self):
        self.client.get(url="/logout")
