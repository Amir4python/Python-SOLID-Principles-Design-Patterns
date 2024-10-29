from abc import ABC,abstractmethod


class Publisher(ABC):

    @abstractmethod
    def add_subscriber(self,subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self,subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass


class Subscriber(ABC):

    @abstractmethod
    def update(self,temperature,humidity,pressure):
        pass


class WeatherData(Publisher):
    def __init__(self,temperature,humidity,pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.subscribers = []

    def add_subscriber(self,subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self,subscriber):
        self.subscribers.remove(subscriber)


    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(temperature=self.temperature,humidity=self.humidity,pressure=self.pressure)
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity=humidity
        self.pressure=pressure
        self.notify_subscribers()


class ForecastDisplay(Subscriber):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    def update(self,temperature,humidity,pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        print(f"Forecast Display: Temperature: {self.temperature} Humidity: {self.humidity} Pressure: {self.pressure}")


class CurrentConditionsDisplay(Subscriber):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    def update(self,temperature,humidity,pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        print(f"Current Conditions Display: T: {self.temperature} H: {self.humidity} P: {self.pressure}")


if __name__ == '__main__':
    weather_data = WeatherData(temperature=50,humidity=50,pressure=50)
    weather_data.add_subscriber(ForecastDisplay())
    weather_data.add_subscriber(CurrentConditionsDisplay())
    weather_data.set_measurements(temperature=10,humidity=20,pressure=30)
    weather_data.set_measurements(temperature=100,humidity=220,pressure=130)








