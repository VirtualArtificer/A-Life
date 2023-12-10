from typing import List, Dict, Tuple, Any, Union

import numpy as np


class Brain:
  def simulate(self):
    current_row = {}
    for sensor in self.sensors:
      # sensor functions are inlined here for speed
      # types of sensors:
        # introspective (organism health, position etc.)
        # entity property
        # vector field (scents, sounds, heat, etc.)
        # environment (time, terrain, etc.)
        # storage (retrieves values set by previous brain simulation passes)
        # constant
        # oscillator (note - different powers of 10ms should be plenty, no need to have every frequency)
      
        

class Sensor:

  def __init__(self, data: Dict[str, Any]):
    self.type = data["type"]
    self.position = np.array(data["position"])
    self.sensitivity = data["sensitivity"]

  def evaluate(self, environment: Dict[str, np.ndarray]) -> np.ndarray:
    field = environment[self.type]
    sensor_value = field[self.position] * self.sensitivity
    return sensor_value

class Neuron:

  def __init__(self, data: Dict[str, Any]):
    self.input_columns = data["input_columns"]
    self.output_column = data["output_column"]
    self.function = data["function"]
    self.parameters = data["parameters"]

class Organism:

  def __init__(self, sensors: List[Sensor], neurons: List[Neuron], output_columns: List[int]):
    self.sensors = sensors
    self.neurons = neurons
    self.output_columns = output_columns

def simulate_brain(organism: Organism, environment: Dict[str, np.ndarray]) -> np.ndarray:
  current_row = np.zeros(len(organism.neurons))

  for sensor in organism.sensors:
    sensor_value = sensor.evaluate(environment)
    current_row[sensor.output_column] = sensor_value

  for neuron in organism.neurons:
    input_values = [current_row[i] for i in neuron.input_columns]
    output_value = apply_neuron_function(neuron.function, input_values, neuron.parameters)
    current_row[neuron.output_column] = output_value

  output_values = current_row[organism.output_columns]

  return output_values

def apply_neuron_function(function: str, input_values: List[float], parameters: List[float]) -> float:
  if function == "threshold":
    threshold = parameters[0]
    return 1.0 if any(i > threshold for i in input_values) else 0.0
  elif function == "addition":
    return sum(input_values) + parameters[0]
  # ...

  raise ValueError(f"Unknown neuron function: {function}")
