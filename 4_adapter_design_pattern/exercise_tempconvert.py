"""
Working with the Adapter Pattern Exercise
In this exercise, you will implement the Adapter Design Pattern to make two incompatible temperature sensor classes work together.

The two classes are:

CelsiusTemperatureSensor: A class that simulates a temperature sensor providing readings in Celsius.

FahrenheitTemperatureSensor: A class that simulates a temperature sensor providing readings in Fahrenheit.

Your task is to create a TemperatureSensorAdapter class that adapts the interface of the FahrenheitTemperatureSensor class to be compatible with the CelsiusTemperatureSensor class. This will allow both classes to be used interchangeably.



To complete this exercise, follow these steps:

Study the provided CelsiusTemperatureSensor and FahrenheitTemperatureSensor classes.

Implement the TemperatureSensorAdapter class that takes a FahrenheitTemperatureSensor object and adapts its interface to match the CelsiusTemperatureSensor class.

Use the provided display_temperature function to display temperature readings from both the CelsiusTemperatureSensor and the adapted FahrenheitTemperatureSensor.

Test your implementation using the provided test code.

This exercise will help you understand how the Adapter Design Pattern can be used to make different classes with incompatible interfaces work together.

"""


class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = 25

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature


class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature


# TODO: Complete the TemperatureSensorAdapter class
class TemperatureSensorAdapter:
    def __init__(self, sensor):
        self._sensor = sensor

    def set_temperature(self, temperature):
        self._sensor.set_temperature(temperature)

    def get_temperature_celsius(self):
        return (self._sensor.get_temperature_fahrenheit() - 32) * 5 / 9

def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")


def test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor):
    adapter.set_temperature(100)
    fahrenheit_sensor.set_temperature(100)
    assert abs(adapter.get_temperature_celsius() - 37.7778) < 0.0001, "Adapter conversion is incorrect"

    celsius_sensor.set_temperature(0)
    adapter.set_temperature(32)
    assert abs(celsius_sensor.get_temperature_celsius() - adapter.get_temperature_celsius()) < 0.0001, "Adapter conversion is incorrect"

    print("All tests passed!")


if __name__ == "__main__":
    celsius_sensor = CelsiusTemperatureSensor()
    fahrenheit_sensor = FahrenheitTemperatureSensor()
    adapter = TemperatureSensorAdapter(fahrenheit_sensor)

    display_temperature(celsius_sensor)
    display_temperature(adapter)

    test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor)
