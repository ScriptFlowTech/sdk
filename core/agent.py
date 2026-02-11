from .planner import Planner
from .executor import Executor
from .memory import Memory


class Agent:
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.executor = Executor()

    def observe(self, data):
        self.memory.store("observation", data)

    def plan(self, goal):
        plan = self.planner.create(goal, self.memory)
        self.memory.store("plan", plan)
        return plan

    def execute(self):
        plan = self.memory.get("plan")
        return self.executor.run(plan)
