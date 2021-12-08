class poly():
    def __init__(self, polynome):
        self.p = polynome
        self.l = []
        self.s = ""
        self.Traitement()

    def Traitement(self):
        poly = ""
        for i in self.p:
            if i != " ":
                poly = poly + i
        self.p = poly

        preL = []
        element = ""
        for i in range(len(self.p)):
            if(i != 0 and (self.p[i] == "+" or self.p[i] == "-") and self.p[i - 1] != "^"):
                preL.append(element)
                element = self.p[i]
            else:
                element = element + self.p[i]
        preL.append(element)

        preL = [i.split("x") for i in preL]

        for i in preL:
            element = []
            if(i[0][0] == "+"):
                element.append(i[0][1:])
            else:
                element.append(i[0])
            if(len(i) == 2):
                if(i[1] != ""):
                    element.append("x")
                    element.append(i[1][1:])
                else:
                    element.append("x")
                    element.append("1")
            else:
                element.append("x")
                element.append("0")
            self.l.append(element)
            self.ListeToStr()

    def isInt_str(self, v):
        v = str(v).strip()
        return v=='0' or (v if v.find('..') > -1 else v.lstrip('-+').rstrip('0').rstrip('.')).isdigit()

    def liste(self):
        return self.l
    
    def ListeToStr(self):
        polynome = ""
        for i in self.l:
            if(i != self.l[0] and i[0][0] != "-" and i[0][0] != "+"):
                i[0] = "+" + i[0]
            if(i[-1] == "0"):
                polynome += i[0]
            elif(i[-1] == "1"):
                polynome += i[0] + i[1]
            else:
                polynome += i[0] + i[1] + "^" + i[2]
            print(polynome)
        self.s = polynome
        return self.s
    
p = poly("24x^2 + 12x - 12")
print(p.liste())