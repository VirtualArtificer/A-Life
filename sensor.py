from enum import Enum
from time import time_ns

class SensorType(Enum):
    INTROSPECTIVE = 1
    ENTITY_PROPERTY = 2
    VECTOR_FIELD = 3
    ENVIRONMENT = 4
    STORAGE = 5
    CONSTANT = 6
    OSCILLATOR = 7


class Sensor:
    """
    Base class for all sensors in the organism.
    """

    def __init__(self, sensor_type: SensorType):
        self.sensor_type = sensor_type
        self.relative_position = Vector()

    def simulate(self, agent: "Agent"):
        """
        Simulates the sensor's activity for one timestep.

        Args:
            agent: The Agent instance this sensor belongs to.

        Returns:
            The sensor's output value after any filtering or transformation.
        """

        # Initial value based on sensor type
        sensor_value = Vector()

        # Introspective sensor
        if self.sensor_type == SensorType.INTROSPECTIVE:
            sensor_value = agent.data.get(self.query)

        # Entity property sensor
        elif self.sensor_type == SensorType.ENTITY_PROPERTY:
            entity = resource_manager.get_entity_at_point(agent.center + self.relative_position)
            if entity is not None:
                sensor_value = entity.data.get(self.query)

        # Vector field sensor
        elif self.sensor_type == SensorType.VECTOR_FIELD:
            sensor_value = resource_manager.get_field_value(self.field_type, agent.center + self.relative_position)

        # Environment sensor
        elif self.sensor_type == SensorType.ENVIRONMENT:
            sensor_value = resource_manager.get_environment_value(self.environment_property)

        # Storage sensor
        elif self.sensor_type == SensorType.STORAGE:
            sensor_value = agent.brain.storage.get(self.storage_key)

        # Constant sensor
        elif self.sensor_type == SensorType.CONSTANT:
            sensor_value = self.constant_value

        # Oscillator sensor
        elif self.sensor_type == SensorType.OSCILLATOR:
            current_time = time_ns()
            reversed_time_string = str(current_time)[::-1]
            sensor_value = Vector([int(digit) for digit in reversed_time_string])

        # Chose not to filter or transform output, as this would hinder evolution of reactive behavior

        # ...

        return sensor_value

    # TODO: Consider adding a note about exploring "decoding" as an intelligence test.
