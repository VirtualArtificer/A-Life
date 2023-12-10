from typing import List, Dict, Tuple, Any, Union

import numpy as np


# TODO: conventions, terminology and reasonining document

class Brain:
  def __init__(self,agent):
    """
    ## Explicit agent reference on Brain initialization

**Rationale:**

* **Unique relationship:** The Brain component has a unique and tightly coupled relationship with its associated Agent. The Brain requires access to specific Agent properties and methods that wouldn't be relevant to other potential parent objects like "Robot" or "Vat."
* **Efficiency:** Directly referencing the Agent during Brain initialization avoids the overhead of additional data structures or unnecessary lookups required by other approaches like global mediators or introspection.
* **Conceptual clarity:** Explicitly referencing the Agent in the Brain's constructor clearly expresses the intended parent-child relationship and minimizes potential confusion for future developers.

**Alternatives considered:**

* Global mediator: Adds unnecessary complexity and reduces efficiency for this specific use case.
* Introspection: Requires framework support and may not be reliable.
* Table of parents and children: Overkill for this simple one-to-one relationship.

**Conclusion:**

Explicit agent reference on Brain initialization offers the best balance of simplicity, efficiency, and clarity for this specific scenario.
"""
    self.agent = agent
    
  def simulate(self):
    current_row = {}
    for sensor in self.sensors:
      # sensor needs agent for agent property access (remaining energy, position, etc.)
      sensor_value = sensor.simulate(self.agent)
      # convention note: use "_index" suffix to explicitly show this is a sequential integer index (not an obj ref, name, guid, etc.)
      current_row[sensor.output_column_index] = sensor_value
      # consider inlining sensor functions here, for speed
      # types of sensors:
        # introspective (organism health, position etc.)
        # entity property
        # vector field (scents, sounds, heat, etc.)
        # environment (time, terrain, etc.)
        # storage (retrieves values set by previous brain simulation passes)
        # constant
        # oscillator (note - different powers of 10ms should be plenty, no need to have every frequency)
    # design note: making NeuronRow a shell object, but functionality should be inlined here for speed if doable
    for neuron_row in self.neuron_rows:
      for neuron in neuron_row.neurons:
        input_values = [current_row.get(i, 0.0) for i in neuron.input_column_indices]
        output_value = neuron.simulate(input_values)
        current_row[neuron.output_column_index] = output_value
    for organ in self.organs:
      organ.simulate(self.agent)
