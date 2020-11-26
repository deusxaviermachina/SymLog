import re

"""
---------
SYNTAX:
---------
1.) UNARY OPERATIONS
1.1) "P" (PROPOSITION)
1.2) "~P" (NEGATION)

2.) BINARY OPERATIONS
2.1) "P&Q" (AND)
2.2) "P$Q" (INCLUSIVE OR)
2.3) "P^Q" (XOR)
"""
class BinaryProposition:
    def __init__(self, text):
        self.text = text
        self.dictionary = {i: True for i in self.text if i.isalpha()}
        self.truth_val = None


    def parse(expr):
        # returns a list object that stores logic formulae and their corresponding truth values for programmatic use
        st = str(expr.text)
        x = st.replace("(", " ").replace(")", " ")
        x = x.strip(" ")
        for i in range(len(x)):
            if x[i - 1] == "~" and x[i].isalpha():
                expr.dictionary[x[i]] = False
        y = []
        x = x.split(" ")
        for elem in x:
            newelem = elem.replace("~", " ~ ")
            y.append(newelem)
        x = y

        dictionary = {i: None for i in x if i.isalpha()}
        for i in x:
            if len(i) > 1:
                if "&" in i:
                    truth_value = BinaryProposition(i).AND(expr.dictionary)
                    dictionary[i] = truth_value
                elif "$" in i and len(i) > 2:
                    truth_value = BinaryProposition(i).OR(expr.dictionary)
                    dictionary[i] = truth_value
                elif "$" in i and len(i) == 2:
                    i = i.replace("$", " $")
                    truth_value = [expr.dictionary[elem] for elem in i if elem.isalpha()]
                    i = i.replace(" ", "")
                    dictionary[i] = truth_value
                elif "^" in i:
                    truth_value = BinaryProposition(i).XOR(expr.dictionary)
                    dictionary[i] = truth_value
        stack = [(i, dictionary[i]) for i in x if i.isalpha() or len(i) > 1]
        return stack
    
    def AND(expr, dictionary):
        atoms = [i for i in expr.text]
        for i in range(len(atoms)):
            if atoms[i - 1] == "~" and atoms[i].isalpha():
                dictionary[atoms[i]] = False
        operator = [i for i in expr.text if i == "&"]
        expressions = [atom for atom in atoms if atom.isalpha()]
        operator = "&"
        if operator:
            if all(dictionary[expression] == True for expression in expressions):
                return True
            else:
                return False

    def OR(expr, dictionary):
        atoms = [i for i in expr.text]
        for i in range(len(atoms)):
            if atoms[i - 1] == "~" and atoms[i].isalpha():
                dictionary[atoms[i]] = False
        operator = "$"
        expressions = [atom for atom in atoms if atom.isalpha()]
        if operator:
            if all(dictionary[expression] == False for expression in expressions):
                return False
            else:
                return True

    def XOR(expr, dictionary):
        atoms = [i for i in expr.text]
        for i in range(len(atoms)):
            if atoms[i - 1] == "~" and atoms[i].isalpha():
                dictionary[atoms[i]] = False
        expressions = [atom for atom in atoms if atom.isalpha()]
        if any(dictionary[expression] for expression in expressions) and not all(
                dictionary[expression] for expression in expressions):
            return True
        else:
            return False

    def NAND(expr, dictionary):
        atoms = [i for i in expr.text]
        for i in range(len(atoms)):
            if atoms[i - 1] == "~" and atoms[i].isalpha():
                dictionary[atoms[i]] = False
        operator = [i for i in expr.text if i == "."]
        expressions = [atom for atom in atoms if atom.isalpha()]
        operator = "."
        if operator:
            if all(dictionary[expression] == True for expression in expressions):
                return False
            else:
                return True

    def NOR(expr, dictionary):
        atoms = [i for i in expr.text]
        for i in range(len(atoms)):
            if atoms[i - 1] == "~" and atoms[i].isalpha():
                dictionary[atoms[i]] = False
        operator = "-"
        expressions = [atom for atom in atoms if atom.isalpha()]
        if operator:
            if all(dictionary[expression] == False for expression in expressions):
                return True
            else:
                return False

    def XNOR(expr, dictionary):
        atoms = [i for i in expr.text]

        for i in range(len(atoms)):
            if atoms[i - 1] == "~" and atoms[i].isalpha():
                dictionary[atoms[i]] = False
        operator = "_"

        expressions = [atom for atom in atoms if atom.isalpha()]
        if operator:
            if any(dictionary[expression] for expression in expressions) and not all(
                    dictionary[expression] for expression in expressions):
                return False
            else:
                return True

    def evaluate(expr):
        
        """
        will return truth value for a given formula if the formula contains a conjunction (AND) binary operator
        and/or an inclusive or (OR) binary operator(i.e. the ones that can be directly converted into python logical operators).
        It would be trivial to modify the program so that it can also evaluate simple statements (e.g. 'A^B') that contain any
        other binary operator. However, doing so for more complex statements (e.g. '(x&(Y&((~t$q)^(~o$~w))$(m&v)))') may be
        beyond the scope of this project.
        """

        st = str(expr.text)
        x = st
        x = re.sub(r"~\w+", "~T", x)
        x = re.sub(r"\w+", "T", x)
        P = BinaryProposition(x)
        items = x.replace("(", "[").replace(")", "]")
        items2 = items.replace("&", " and ").replace("$", " or ").replace("T", " True ").replace("~", " not ")
        print("%s:%s" % (expr.text, str(eval(items2)).replace("]", "").replace("[", "")))
        return str(eval(items2)).replace("]", "").replace("[", "")

if __name__ == "__main__":
    expression = BinaryProposition("(x&(Y&((~t$q)$(~o$~w))$(m&v)))")
    print(expression.evaluate())
    expression = BinaryProposition("A$B")
    print(expression.evaluate())
    expression2 = BinaryProposition("(W&X)^(Y&Z)")
    print(expression2.parse())
    expression = BinaryProposition("(Y&~X)$(~b^Q)")
    print(expression.parse())
