from typing import List


class Sensor:
    pass
        # types of sensors:
        # introspective (organism health, position etc.)
        # entity property
        # vector field (scents, sounds, heat, etc.)
        # environment (time, terrain, etc.)
        # storage (retrieves values set by previous brain simulation passes)
        # constant
        # oscillator (note - different powers of 10ms should be plenty, no need to have every frequency)

class Brain:
    def __init__(self, agent):
        """
        Initializes a Brain object.

        Parameters:
        - agent: The associated agent for the brain.

        Rationale:
        - Unique relationship: The Brain component has a unique and tightly coupled relationship with its associated Agent. 
        - Efficiency: Directly referencing the Agent during Brain initialization avoids additional data structures or unnecessary lookups.
        - Conceptual clarity: Explicitly referencing the Agent in the Brain's constructor expresses the intended parent-child relationship.

        Conclusion:
        Explicit agent reference on Brain initialization offers the best balance of simplicity, efficiency, and clarity.
        """
        self.agent = agent
        self.curent_row = {}

    def simulate(self):
        """
        Simulates the brain's functions.

        Simulation Process:
        - Collects sensor values and stores them in `current_row`.
        - Processes neuron rows to compute output values.
        - Simulates organs' actions on the agent.

        Note:
        - Consider optimizing specific functionalities for speed.
        """
        current_row = self.current_row
        current_row.clear()
        for sensor in self.sensors:
            sensor_value = sensor.simulate(self.agent)
            current_row[sensor.output_column_index] = sensor_value

        for neuron_row in self.neuron_rows:
            for neuron in neuron_row.neurons:
                input_values = [current_row.get(i, 0.0) for i in neuron.input_column_indices]
                output_value = neuron.simulate(input_values)
                current_row[neuron.output_column_index] = output_value

        for organ in self.organs:
            organ.simulate(self.agent)
