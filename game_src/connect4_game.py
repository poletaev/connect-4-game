
from unicodedata import name
from base_game import Game
from base_states import GameAction, GameState
from base_agent import Agent

class Connect4Action(GameAction):
    def __init__(self, max_col=6) -> None:
        self.max_col = max_col

    @property
    def action(self):
        return self.action

    @action.setter
    def action(self, value):
        if value < 0 or value > self.max_col:
            raise ValueError(f"Incorrect action: must be between 0 and {self.max_col}")
        self._action = value

class Connect4State(GameState):
    def __init__(self, width: int = 7, height: int = 6) -> None:
        super().__init__()
        self.width = width
        self.height = height

    def next_actions(self) -> list[int]:
        return list(range(self.width))

    def update(self, action: Connect4Action):
        return self

    def __str__(self) -> str:
        return f"{self.width} x {self.height}"


class KeyboardAgent(Agent):
    def __init__(self, name: str, max_col: int = 7) -> None:
        super().__init__()
        self.name = name
        self.max_col = max_col

    def get_action(self, state: Connect4State) -> Connect4Action:
        print(f"Available actions: {state.next_actions()}")
        while True:
            col = int(input())
            print(f"got request {col} from {self.name}")
            # зря переносил логику проверки в класс Action, 
            # видимо будет проще проверить здесь
            if col in state.next_actions():
                action = Connect4Action(max_col=self.max_col)    
                action.action = col
                return action

class Connect4Game(Game):
    def __init__(self,
                 agents: list[Agent],
                 width:int = 7,
                 height:int = 6) -> None:
        super().__init__(agents)
        if len(agents) != 2:
            raise ValueError(f"Incorrect number of agents = {len(agents)}. Use two agents!")
        self.state = self.init_state(width, height)
        self.width = width

    def init_state(self, w, h) -> Connect4State:
        return Connect4State(width=w, height=h)

    def update_state(self, action) -> Connect4State:
        return self.state.update(action)

    def is_game_over(self) -> bool:
        return False

    def display_state(self) -> None:
        print(self.state)
        

if __name__ == "__main__":
    agent1 = KeyboardAgent(name="agent1")
    agent2 = KeyboardAgent(name="agent2")
    game = Connect4Game(agents=[agent1, agent2],
                        width=7,
                        height=6
                       )
    game.run()        