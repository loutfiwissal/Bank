import random  

compte={56:200,20:360}    #numc,soldec
client={1:"566",2:"836"}  #numcl,mpc
clientcompte={1:56,2:20}   #numcl,numc

def ajouter_client():
    numcl = int(input("customer number: "))
    a = (random.randint(0,100))
    numc = numcl*100+a

    mpc = input ("-The code : ")

    soldec = input ("-The balance : ")

    compte.update({numc : soldec})
    client.update({numcl : mpc})
    clientcompte.update({numcl : numc})

def supprimerClient():
    C = int(input("-The account number you want to delete: "))
    del compte[C]
    for key,value in clientcompte.items():
        if C == value:
            x = key
    del client[x]
    del clientcompte[x]

def modifier_mpc():
    numcl = int(input("-Give me the customer number :"))
    mpc = input("-The new code:")
    client[numcl] = mpc


def deposer_argent():
    numc = int(input("-Give me the account number:"))
    soldec = int(input("Money adds :"))
    for key,value in compte.items():
        if numc == key:        
           s = value + soldec
    compte [numc] = s


def retire_argent():
    numc = int(input("-Give me the account number:"))
    soldec = int(input("-Retirer money :"))
    for key,value in compte.items():
        if numc == key:        
           d = value -soldec
    compte [numc] = d


def affichersolde():
    B = int(input("-Enter your account number : "))
    print(compte[B])


#menu de choix:
print("Are you agent or client ?")
Z = int(input("if you are a client enter 1 , if you are an agent enter 2 :"))

if Z ==1:
   M=input("Menu of choice:\n 1-Edit the pass word \n 2-Show the balance \n 3-Depose money  \n 4-Retirer money")
   X=int(input("Chose 1, 2, 3, 4 : "))

   if X == 1 :
       modifier_mpc()
       print(client)
       

   elif X == 2:
       affichersolde()
       
   elif X == 3:
        deposer_argent()
        print(compte)

   elif X == 4:
       retire_argent()
       print(compte)

else:
    ajouter_client()
    print (compte)
    print(client)
    print (clientcompte)
    supprimerClient()
    print (compte)
    print(client)
    print (clientcompte)

