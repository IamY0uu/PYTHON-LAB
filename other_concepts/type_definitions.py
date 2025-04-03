# these annotations makes code self-documentary
n : int = 5
s : str = "win/lose"

def sum (a : int,b : int ) -> int:
    return a+b
sum(3, 5)




from typing import List, Union, Tuple, Dict

numbers: List[int] = [1,2,3,4,5]
person: Tuple[str, int] = ("Lucky",21)
scores: Dict[str, int] = {"Ind":99, "Aus":86}

identifier: Union[str, int] = "ID345"  # union type for variables that can handle multiple types
identifier: 1234


