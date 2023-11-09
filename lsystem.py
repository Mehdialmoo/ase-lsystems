from typing import Dict,List
from pen import Pen

class LSystem():

    rules: dict[str,str]    

    def set_rules(self,rules: Dict[str,str]) -> None:
        self.rules = rules

    def generate_next_state(self,current_state) -> str:
        new_state = ""
        for character in current_state:
            if character in self.rules.keys():
                new_state += self.rules[character]
            else:
                new_state += character
        return new_state

class Ltree(LSystem):
    colour : str 
    thickness : int
    length : int
    angle : int
    Pen : Pen
    drawing_stack : list[Dict]
    state_history: List[str]

    def __init__(self,    
    axiom : str,
    colour : str, 
    thickness : int,
    length : int,
    angle : int,
    rules: Dict[str,str]) -> None:
        
        LSystem.__init__(self)
        self.length = length
        self.angle = angle
        self.colour = colour
        self.thickness = thickness
        self.rules = rules
        self.state_history = [axiom]
        self.drawing_stack = []
        self.pen = Pen(
            image_dimensions = (1000,1000),
            pen_pos = (500,1000),
            width = 3
        )
        self.pen.set_heading(-90)
    
    def generate(self,iterations: int) -> None:
        for _ in range(iterations):
            current_state = self.state_history[-1]
            new_state = self.generate_next_state(current_state)
            self.state_history.append(new_state)

    def draw (self, command: str) -> None:
        if command == "L" or command == "I":
            self.pen.forward(self.length)
        elif command == "[":
            pen_state = {
                "position" : self.pen.get_pos(),
                "heading" : self.pen.get_heading()
            }
            self.drawing_stack.append(pen_state)
            self.pen.left(self.angle)
        elif command == "]":
            pen_state = self.drawing_stack.pop()
            self.pen.up()
            self.pen.set_pos(pen_state["position"])
            self.pen.set_heading(pen_state["heading"])
            self.pen.right(self.angle)
            self.pen.down()
            

    def create_image(self) -> None:
        state = self.state_history[-1]
        self.pen.down()
        for command in state:
            self.draw(command)
        self.pen.up()

    def save(self,filename: str):
        self.pen.save(filename = filename)


if  __name__=="__main__":
    rules = {
        "L" : "I[L]L",
        "I" : "II"
    }
    axiom = "L"
    ltree =Ltree(
        axiom=axiom,
        colour="Green",
        thickness=3,
        length=5,
        rules=rules,
        angle=35
    )
    ltree.generate(iterations=7)
    ltree.create_image()
    ltree.save("ltree.png")

