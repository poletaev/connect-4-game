
from tabnanny import check
from base_game import Game
from base_states import GameAction, GameState
from base_agent import Agent

class Connect4Action(GameAction):
    def __init__(self, player_num: int, max_col:int =6) -> None:
        self.max_col = max_col
        self.player_num = player_num
        self.action = None

    # todo: заготовка на будущее
    # @property
    # def action(self):
    #     return self.action

    # @action.setter
    # def action(self, value):
    #     if value < 0 or value > self.max_col:
    #         raise ValueError(f"Incorrect action: must be between 0 and {self.max_col}")
    #     self._action = value

class Connect4State(GameState):
    def __init__(self, width: int = 7, height: int = 6) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.grid = []
        self.player_won = None
        for i in range(height):
            self.grid.append([])
            for _ in range(width):
                self.grid[i].append(0)

    def is_game_over(self):
        self.player_won = self.check4()
        if self.player_won is not None:
            print(f"player {self.player_won} won!")
            return True

    def next_actions(self) -> list[int]:
        if self.is_game_over():
            return []

        res = []
        for i in range(self.width):
            if self.grid[self.height - 1][i] == 0:
                res.append(i)
        return res

    def _get_rows(self) -> list[int]:
        for r in self.grid:
            yield r

    def _get_columns(self) -> list[int]:
        for i in range(self.width):
            col = []
            for j in range(self.height):
                col.append(self.grid[j][i])
            yield col

    def _get_diag(self) -> list[int]:
        j = 0
        for start in range(3, self.width + 3):
            diag = []
            for i, j in zip(range(start, -1, -1), range(0, self.height)):
                if 0 <= i < self.width and 0 <= j < self.height:
                    diag.append(self.grid[j][i])
            yield diag

    def _get_diag2(self) -> list[int]:
        j = 0
        for start in range(-3, self.width - 3):
            diag = []
            for i, j in zip(range(start, self.width), range(0, self.height)):
                if 0 <= i < self.width and 0 <= j < self.height:
                    diag.append(self.grid[j][i])
            yield diag

    def check4(self) -> int:
        for p in range(1, 3):
            # check per row:
            for row in self._get_rows():
                per_row = 0
                for i in range(len(row)):
                    if row[i] == p:
                        per_row += 1
                        if per_row == 4:
                            return p
                    else:
                        continue
            # check per column:
            for col in self._get_columns():
                per_col = 0
                for i in range(len(col)):
                    if col[i] == p:
                        per_col += 1
                        if per_col == 4:
                            return p
                    else:
                        continue
            for col in self._get_diag():
                per_col = 0
                for i in range(len(col)):
                    if col[i] == p:
                        per_col += 1
                        if per_col == 4:
                            return p
                    else:
                        continue
            for p in range(1, 3):
                for col in self._get_diag2():
                    per_col = 0
                    for i in range(len(col)):
                        if col[i] == p:
                            per_col += 1
                            if per_col == 4:
                                return p
                        else:
                            continue


    def update(self, action: Connect4Action):
        if action is not None:
            print(f"got action from player #{action.player_num} = {action.action}")
            for i in range(0, self.height):
                if self.grid[i][action.action] == 0:
                    self.grid[i][action.action] = action.player_num
                    self.is_game_over()
                    return

    def __str__(self) -> str:
        s =  f"{self.width} x {self.height} \n"
        for i in range(self.height - 1, -1, -1):
#            s += f"{self.grid[i]} \n"
            s += "\n"
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    s += ". "
                elif self.grid[i][j] == 1:
                    s += "X "
                elif self.grid[i][j] == 2:
                    s += "O "
        return s 


class KeyboardAgent(Agent):
    def __init__(self, name: str, num: int, max_col: int = 7) -> None:
        super().__init__()
        self.num = num # todo: инициализировать в игре при создании списка игроков
        self.name = name
        self.max_col = max_col

    def get_action(self, state: Connect4State) -> Connect4Action:
        print(f"Available actions: {state.next_actions()}")
        if len(state.next_actions()) > 0:
            while True:
                col = int(input(f"{self.name} >"))
                print(f"got request {col} from {self.name}")
                # зря переносил логику проверки в класс Action, 
                # видимо будет проще проверить здесь
                if col in state.next_actions():
                    action = Connect4Action(player_num=self.num, max_col=self.max_col)    
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
        return self.state.is_game_over()

    def display_state(self) -> None:
        print(self.state)
        

if __name__ == "__main__":
    agent1 = KeyboardAgent(name="Player #1", num=1)
    agent2 = KeyboardAgent(name="Player #2", num=2)
    game = Connect4Game(agents=[agent1, agent2],
                        width=7,
                        height=6
                       )
    game.run()        