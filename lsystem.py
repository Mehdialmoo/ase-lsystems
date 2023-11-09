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
        
        self.length = length
        self.angle = angle
        self.colour = colour
        self.thickness = thickness
        self.rules = rules
        self.state_history = [axiom]
        