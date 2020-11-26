from conditional import *

UNIVERSE = {}
ATOMS = []

def add_to_universe(expr):
    ATOMS.append(expr.premise)
    for i in expr.consequences:
        ATOMS.append(i)
    UNIVERSE[expr.premise] = []
    UNIVERSE[expr.premise].append(expr.premise)
    for i in expr.consequences:
        if i not in UNIVERSE[expr.premise]:
            UNIVERSE[expr.premise].append(i)
        else:
            pass
    return (UNIVERSE.items())

def update_universe(x, y):
    subjects=[]
    predicates=[]
    for (subject, predicate) in UNIVERSE.items():
        subjects.append(subject)
        for j in predicates:
            predicates.append(j)

    if x.does_a_imply_b(y) and y in subjects:
        for i in UNIVERSE[y]:
            UNIVERSE[x.premise].append(i)
    print(UNIVERSE.items())

def query(item, *attributes, Boole=""):
    if item not in UNIVERSE.keys():
        return
    if Boole=="":
        if len(attributes)>1:
            return "Error"
        elif attributes[0] in UNIVERSE[item]:
            return True
        else:
            return False
    elif Boole=="and":
        if all(attribute in UNIVERSE[item] for attribute in attributes):
            return True
        else:
            return False
    elif Boole=="or":
        if any(attribute in UNIVERSE[item] for attribute in attributes):
            return True
        else:
            return False
#tests
if __name__ == "__main__":
    expr = conditionalize("Socrates", "Man", "Philosopher", "Greek", "Dead")
    (add_to_universe(expr))
    expr2 = conditionalize("John Doe", "Man", "American", "Alive")
    (add_to_universe(expr2))
    expr3 = conditionalize("Man", "Mortal", "Rational")
    (add_to_universe(expr3))
    update_universe(expr, expr3.premise)
    update_universe(expr2, expr3.premise)
    print(query("Socrates","Greek", "Man", Boole="and"))
        if "Rational" in set(UNIVERSE["Socrates"]):
        print(True, UNIVERSE["Socrates"], set(UNIVERSE["Socrates"]))
    else:
        print(False)
