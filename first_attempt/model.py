from mesa import Model
from agent import BasicAgent
import datetime as dt


class BasicModel(Model):
    def __init__(
        self,
        start_dt: dt.datetime,
        end_dt: dt.datetime,
        step_delta: dt.timedelta,
        num_agents: int = 10,
    ):
        super().__init__()
        self.start = start_dt
        self.end = end_dt
        self.delta = step_delta
        self.time = dt.datetime(self.start.year, self.start.month, self.start.day)

        for _ in range(num_agents):
            BasicAgent(self)

    def step(self):
        self.agents.shuffle_do("step")
        self.time += self.delta

    def run_model(self):
        self.running = True
        while self.time < self.end:
            self.step()
        self.running = False
