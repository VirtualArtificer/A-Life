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
        self.curent_row = defaultdict(Vector)

    def sigmoid(self, value):
        return 1 / (1 + np.exp(-x))

    def rescale(self, value, func, scale):
        return scale*func(value/scale)

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
                input_values = [current_row[i] for i in neuron.input_column_indices]
                output_value = neuron.simulate(input_values)
                current_row[neuron.output_column_index] = output_value

        for organ in self.organs:
            input_value = current_row[organ.input_column_index]
            organ.simulate(input_value,self.agent)
