import numpy as np
import matplotlib.pyplot as plt
class poly:
    def __init__(self, polynome):#initialisation avec toutes les variables utiles
        self.p = polynome#polynome brut
        self.l = []#polynome sous forme de liste
        self.s = ""#polunome sous fomre de chaine de charactere
        self.Traitement()#traitement du polynome brut en liste et en chaine de charatere
    
    def __str__(self):#affichage textuel du polynome
        return self.s #revois le string du la classe
    
    def affiche(self,x,y):#affichage graphique du polynome
        x = np.linspace(x, y, 20) #initialiser un graphique
        y = 0
        for i in self.l:
            y = y + int(i[0])*x**int(i[2]) #y ajouter tous les elements
        plt.plot(x,y) #finaliser le graphiqu
        plt.show()#afficher le graphique
    
    def normalAffiche(self):#affichage graphique du polynome simplifié
        return self.affiche(-30,30)
    
    def Traitement(self):#traitement du polynome brut en liste et en chaine de charatere
        polynome = ""#créer un string
        for i in self.p:#enlève les espaces
            if i != " ":
                polynome = polynome + i
        self.p = polynome #remet dans une liste

        preL = [] #creer une novelle liste
        element = "" #initilise un element du polynome
        for i in range(len(self.p)):#coupe les différents elements en liste d'elements
            if(i != 0 and (self.p[i] == "+" or self.p[i] == "-") and self.p[i - 1] != "^"):
                preL.append(element)
                element = self.p[i]
            else:
                element = element + self.p[i]
        preL.append(element)#ajouter l'element à la liste preL

        preL = [i.split("x") for i in preL]#redimentionne les x
        
        for i in preL:#traite les differents elements dans une charte définie
            elements = []
            if(len(i) != 0 and len(i[0]) != 0):
                if(i[0][0] == "+"):
                    elements.append(i[0][1:])
                elif(i[0][0] == "-"):
                    elements.append(i[0])
                else:
                    elements.append("+" + i[0])
                if(len(i) == 2):
                    if(i[1] != ""):
                        elements.append("x")
                        elements.append(i[1][1:])
                    else:
                        elements.append("x")
                        elements.append("1")
                else:
                    elements.append("x")
                    elements.append("0")
                self.l.append(elements)
        self.ListeToStr()

    def isInt_str(self, v):#test si un str peut etre un integer
        v = str(v).strip()
        return v=='0' or (v if v.find('..') > -1 else v.lstrip('-+').rstrip('0').rstrip('.')).isdigit()

    def liste(self):#renvoie la liste
        return self.l
    
    def ListeToStr(self):#Transforme la liste en format str
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
        self.s = polynome
        return self.s
    
    def derive(self):#trouve la dérivé du polynome 
        derive = []
        for partie in self.l:
            if int(partie[2]) >= 1:
                if int(partie[0])>0:
                    bloc = ["+" + str(int(partie[0]) * int(partie[2]))]
                else:
                    bloc = [str(int(partie[0]) * int(partie[2]))]
                bloc.append(partie[1])
                bloc.append(str(int(partie[2])-1))
                derive.append(bloc)
        n = poly(self.toText(derive))
        return n
    
    def seconde(self):#trouve la seconde du polynome initiale
        return self.derive().derive()
    
    def toText(self,listpoly):#polynome en texte
        phrase = ""
        for mot in listpoly:
            if mot[2] == "0":
                phrase = phrase +" "+ mot[0]
            elif mot[2] == "1":
                phrase = phrase +" "+ mot[0] + mot[1]
            else:
                phrase = phrase +" "+ mot[0] + mot[1] + "^" + mot[2]
        return phrase
    
    def racines(self):#trouve les racines du polynome simplifier
        end = "Ce polynome a pour racines : "
        racines = self.findRoots()
        for i in racines:
            end = end + str(i) + " , "
        return end[:-3]
        
    def findRoots(self):#trouve les racines
        coefficients = [int(i[0]) for i in self.l]
        racines = np.roots(coefficients)
        return racines
    
p = poly("2x^2+24x+12")
print(p)
print(p.derive())
print(p.racines())
print(p.seconde())
p.normalAffiche()