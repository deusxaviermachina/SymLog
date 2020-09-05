from binaryproposition import BinaryProposition

class Conditional:
    def __init__(self, premise, *args):
        self.premise=premise
        self.consequences=[]

    def implies(self, *args):
        for arg in args:
            self.consequences.append(arg)

    def does_a_imply_b(self, consequent):
        if consequent in self.consequences:
            return True
        else:
            return False

    def converse(self, b):
        if b not in self.consequences:
            return
        if self.does_a_imply_b(b) == True:
            return Conditional(b)
        else:
            return

    def negation(self):
        premise=BinaryProposition(f"~{self.premise}")
        x={premise:eval(premise.evaluate())}
        for (i, j) in x.items():
            return [i.text, j]

    def contrapositive(self, arg):
        if arg not in self.consequences:
            return
        else:
            contra=Conditional(Conditional(arg).negation())
            contra.implies(self.premise)
            print(f"({self.premise}->{arg})->({contra.premise[0]}->{self.premise})")
            return {f"{contra.premise[0]}->{self.premise}":True}


    def inverse(self, arg):
        if arg not in self.consequences:
            return
        else:
            inversion=Conditional(f"~{self.premise}")
            negated_conclusion=f"~{arg}"
            inversion.implies(negated_conclusion)
            return {f"{inversion.premise}-->{negated_conclusion}"}


def conditionalize(condition, *args):
    antecedent=Conditional(condition, *args)
    for arg in args:
        antecedent.consequences.append(arg)
    return antecedent



expr = conditionalize("A", "B", "C", "D")
expr.implies("F", "Z")
exp2 = expr.converse("F")
# A-->F, ~necessarily F--->A, possibly F--->A (modal logic parsing capacities may be useful for situations like this)
exp2 = conditionalize(exp2.premise, "A")
# F----->A is True, ergo A iff F is True
print(expr.does_a_imply_b("F"))
print(exp2.does_a_imply_b("A"))
if expr.does_a_imply_b(exp2.premise) == False or exp2.does_a_imply_b(expr.premise) == False:
    print("biconditional is false")
else:
    print("True")
    print(expr.contrapositive("F"))

print(expr.inverse("F"))
