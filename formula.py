import re

unary_operators={"~":"not"}
binary_operators ={
    "&":"and",
    "|":"or"
}

def is_unary(variable:str):
    return variable=="~" or variable == "NOT"

def is_binary(variable:str):
    return (variable == "&" or variable == "AND") or (variable == "|" or variable == "OR")

def is_variable(variable:str):
    return all(char.isalpha() and char.isupper() for char in variable)

def is_T_or_F_constant(variable:str):
    return variable=="T" or variable=="F"

class Formula:
    def __init__(self, root:str, first=None, second=None):
        self.root=root
        self.first=first
        self.second=second

    def write(self):
        if type(self.first)==Formula:
            self.first=self.first.write()
        if type(self.second)==Formula:
            self.second=self.second.write()
        if self.first is not None and self.second is None:
            return f"{self.root}{self.first}"
        elif self.first is not None and self.second is not None:
            return f"({self.first}{self.root}{self.second})"
        elif self.first is None and self.second is None:
            return f"{self.root}"

f1=Formula("&", Formula("&","P", Formula("&","X","Y")), Formula("~","A"))
print(f1.write())

def evaluate(formula,model:dict):
    for i in formula:
        if is_variable(i):
            formula=formula.replace(i,str(model[i]))
        elif is_binary(i):
            formula=formula.replace(i, f" {binary_operators[i]} ")
        elif is_unary(i):
            formula=formula.replace(i, f" {unary_operators[i]} ")
        else:
            pass
    print(formula)
    return eval(formula)

print(evaluate(f1.write(), {"P":True, "X":True, "Y":True, "A":False}))
