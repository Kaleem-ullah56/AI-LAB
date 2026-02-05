class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.last_action = None  # remembers the previous action

    def act(self, current_temperature):
        # Decide action based on temperature
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"

        # Avoid repeating the same action unnecessarily
        if action == self.last_action:
            action_output = f"{action} (No change, same as last)"
        else:
            action_output = action
            self.last_action = action  # update last action

        return action_output

# Simulate different rooms with their current temperatures
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)

# Run the agent for each room
for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")