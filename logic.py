class Proposition:
    def __init__(self,text:str,model:dict):
        self.text=text
        self.model=model

    def parse(self):
        for i in self.text:
            if i.isalpha():
                self.text=self.text.replace(i, str(self.model[i])).strip()
            else:
                pass
        return eval(self.text)

if __name__ == "__main__":
    model={"X":True, "Y":False, "P":True, "Q":False}
    P=Proposition("(X&(Y|(P^Q)))", model)
    print(P.parse())
