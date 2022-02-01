import numpy as np #import des bibliothèques
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
        polynome = ""#créer un string vide
        for i in self.p:#enlève les espaces
            if i != " ":
                polynome = polynome + i
        self.p = polynome #remet dans une liste

        preL = [] #creer une novelle liste vide
        element = "" #initilise un element du polynome
        for i in range(len(self.p)):#coupe les différents elements en liste d'elements
            if(i != 0 and (self.p[i] == "+" or self.p[i] == "-") and self.p[i - 1] != "^"): #si est i de self.p est un plus ou un moins 
                preL.append(element) # alors ajoutez element à preL
                element = self.p[i] # elément deviens l'indice i de self.p
            else:
                element = element + self.p[i] # ajouter la valeur de self.p[i] à element (c'est donc un chiffre ou un "^"
        preL.append(element)#ajouter l'element à la liste preL

        preL = [i.split("x") for i in preL]#redimentionne les x
        
        for i in preL:#pour chaque élément de preL nommé i
            elements = [] #crée une liste vide 
            if(len(i) != 0 and len(i[0]) != 0):#si i est différent de 0 et non vide
                if(i[0][0] == "+"): # et que son premier élément est un plus 
                    elements.append(i[0][1:]) # ajouter tout le premier élement de i a elements sans le premier symbole (un +)
                elif(i[0][0] == "-"): #si son premier élément est un moins
                    elements.append(i[0])# ajouter le premier element de i a element 
                else:
                    elements.append("+" + i[0])# sinon, ajouter le premier element  de i a élément avec un plus devant
                if(len(i) == 2):#si i contient uniquement deux éléments
                    if(i[1] != ""):# et que le deuxieme est non vide
                        elements.append("x") # ajouter x a element
                        elements.append(i[1][1:])#ajouter la fin de i
                    else:#sinon
                        elements.append("x")# ajouter x a élément 
                        elements.append("1")# ajouter 1 a élément
                else:#si i est plus petit que 2
                    elements.append("x")#ajouter un x a élément 
                    elements.append("0")#ajouter un 0 a élément 
                self.l.append(elements)# ajouter l'élément fianlement créé à self.l
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
        derive = []#crée une liste vide 
        for partie in self.l:# pour chaque éleemnt de self.l
            if int(partie[2]) >= 1:#si l'élément possède un coef 
                if int(partie[0])>0:#si l'élément possède un multiplicateur 
                    bloc = ["+" + str(int(partie[0]) * int(partie[2]))]#ajouter en str la multiplication du coef et de la valeur 
                else:
                    bloc = [str(int(partie[0]) * int(partie[2]))]#mettre dans bloc en str la multiplication du coef et de la valeur 
                bloc.append(partie[1])#ajouter l'élément (le x par ex)
                bloc.append(str(int(partie[2])-1))# réduire de 1 le coef total
                derive.append(bloc)# ajouter le bloc créé a la dérivée 
        n = poly(self.toText(derive))#transformer la liste crée en un polynome 
        return n #renvoyer le polynome 
    
    def seconde(self):#trouve la seconde du polynome initiale
        return self.derive().derive()
    
    def toText(self,listpoly):#polynome en texte
        phrase = ""#création d'une "phrase" pour stocker la transformation
        for mot in listpoly:#pour chaque élement de listpoly
            if mot[2] == "0":#si l'élément n'a aucun coef
                phrase = phrase +" "+ mot[0]# ajouter la valeur brut a la "phrase"
            elif mot[2] == "1":# si l'élément possède un coef de 1
                phrase = phrase +" "+ mot[0] + mot[1]# ajouter l'élement a coté du symbole actuel (souvent x)
            else:
                phrase = phrase +" "+ mot[0] + mot[1] + "^" + mot[2]# si le coef est superieur ou égal a 2, ajouter le signe, a coté du multiplivateur, et du symbole avec un symbole pour le coef
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
