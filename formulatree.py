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

class FormulaTree:
    def __init__(self, root:str, branch1=None, branch2=None):
        self.root=root
        self.branch1=branch1
        self.branch2=branch2

    def write(self):
        if type(self.branch1)==FormulaTree:
            self.branch1=self.branch1.write()
        if type(self.branch2)==FormulaTree:
            self.branch2=self.branch2.write()
        if self.branch1 is not None and self.branch2 is None:
            return f"{self.root}{self.branch1}"
        elif self.branch1 is not None and self.branch2 is not None:
            return f"({self.branch1}{self.root}{self.branch2})"
        elif self.branch1 is None and self.branch2 is None:
            return f"{self.root}"

f=FormulaTree("&", FormulaTree("&", "P", FormulaTree("&", "X", "Y")), FormulaTree("~", "A"))
print(f.write())

def evaluate(formula:FormulaTree,model:dict)->bool:
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

print(evaluate(f.write(), {"P":True, "X":True, "Y":True, "A":False}))
