from mesa import Agent


class BasicAgent(Agent):
    def step(self):
        print(
            f"Agent {self.unique_id} executing step {self.model.steps} at time {self.model.time}"
        )
