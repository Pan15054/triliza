#!/usr/bin/python
# -*- coding: utf-8 -*-
piecesB=["SB","MB","LB"] #τα κομματια που θα βοηθησουν στον ελεγχο της τριλιζας διοτι διαφορετικα  
piecesR=["SR","MR","LR"] #με τα κομματια των παιχτων το μηνυμα της τριλιζας θα εμφανιστει 3 φορες
paixths1=["SB","SB","MB","MB","LB","LB"]#τα κομματια των παιχτων
paixths2=["SR","SR","MR","MR","LR","LR"]
q={"0":0,"SB":1, "MB":2, "LB":3,"SR":1, "MR":2, "LR":3}#οι αξιες των κομματιων
Q=["0"]#οι αρχικες τιμες στα "κουτια" της τριλιζας
W=["0"]#ως θεσεις της τριλιζας στις οποιες θα μπουν τα κομματια των παιχτων ειναι:
E=["0"]#Q,W,E για τις πανω θεσεις
A=["0"]#Α,S,D για τις μεσαιες θεσεις
S=["0"]#Z,X,C για τις κατω (οι θεσεις αυτες διαλεχτηκαν ωστε να βολευει τους παθχτες κατα τη διαρκεια του παιχνιδιου)
D=["0"]
Z=["0"]
X=["0"]
C=["0"]
w={"Q":Q, "W":W, "E":E, "A":A, "S":S, "D":D, "Z":Z, "X":X, "C":C}# λεξικο το οποιο θα βοηθησει στη συνεχεια να γινουν ελεγχοι με συναρτησεις
theseis=["Q","W","E","A","S","D","Z","X","C"]
def triliza(row1,pieces):#αναζητα αν υπαρχει τριλιζα και εμφανιζει τα καταλληλα μηνυματα
    global p
    for i in pieces:
        if row1[0]==i:
            for j in pieces:
                if row1[1]==j:
                    for k in pieces:
                        if row1[2]==k:
                            print "TRILIZA"
                            print "GAME OVER"
                            p="game over"
def add_elem(position,play,Q,paixths1,q,J):#μεταφερει το κομματι του παιχτη απο τον ιδιο στην τριλιζα και μετα το αφαιρει απο το "χερι" του
    if position==J and q[play]>q[Q[0]]:
        Q.append(play)
        Q.reverse()
        paixths1.remove(play)
def add_elem2(position2,play,Q,q,W,J):#μεταφερει το κομματι απο το ενα "κουτι" τριλιζας στο αλλο 
    if position2==J and q[play]>q[W[0]]:
        Q.remove(play)
        Q.reverse()
        W.append(play)
        W.reverse()
def print_table(Q,W,E,A,S,D,Z,X,C):#εκτυπωνει τον πινακα της τριλιζας           
    print "%s | %s | %s" %(Q[0],W[0],E[0])
    print "-----------------" 
    print "%s | %s | %s" %(A[0],S[0],D[0])
    print "-----------------"
    print "%s | %s | %s" %(Z[0],X[0],C[0])
print_table(Q,W,E,A,S,D,Z,X,C)
p="game on"
remainB=6# τα κομματια που εχει καθε φορα ο πρωτος και αντιστοιχα ο δευτερος
remainR=6
while p=="game on":
    l=False
    while l==False:
        ans=raw_input("from the table player1: ")#διαλεξτε αν θα ναι απο την τρλιζα ή απο το χερι του παιχτη
        if ans=="N":# αν γραψετε "Ν"=Νο τοτε...(κανει την επαναληψη της ερωτησης μεχρι να δεχτει "Υ" ή "Ν"
            l=True
            f=False
            while f==False:
                play=raw_input("make your move player1: ")#διαλεξτε καποιο απο τα κομματα που εχετε γραφοντας πχ SΒ ή ΜΒ κτλ
                i=0
                v=False
                while i<=5 and v==False:
                    if play==paixths1[i]:
                        v=True
                        f=True
                    else:
                        i=i+1
    
            position=raw_input("position?: ")# στο σημειο που θελετε να το τοποθετησετε
            for i in theseis:
                if position==i:
                    add_elem(position,play,w[i],paixths1,q,i)
                    remainB=remainB-1
            print_table(Q,W,E,A,S,D,Z,X,C)
        elif ans=="Y":# αντιστοιχα αν θελετε να αλλαξετε θεση σε κομματι απο την τριλιζα
            l=True
            f=False
            while f==False:
                play=raw_input("choose item: ")#διαλεξτε κομματι
                i=0
                v=False
                while i<=5 and v==False:
                    if play==paixths1[i]:
                        v=True
                        f=True
                    else:
                        i=i+1
            position=raw_input("from?: ")#διαλεξτε απο πιο κουτι θελετε να παρετε το κομματι 
            for i in theseis:
                if position==i:
                    position2=raw_input("position you want to be tansfered player1?: ")# διαλεξτε το κουτι που θελετε να μεταφερθει
                    for j in theseis:
                        if position2==j:
                            add_elem2(position2,play,w[i],q,w[j],j)
            print_table(Q,W,E,A,S,D,Z,X,C)
        row1=[Q[0],W[0],E[0]]#καθε πινακας αντοιστιχει σε καποιο συνδυασμο τριλιζας 
        row2=[A[0],S[0],D[0]]
        row3=[Z[0],X[0],C[0]]
        col1=[Q[0],A[0],Z[0]]
        col2=[W[0],S[0],X[0]]
        col3=[E[0],D[0],C[0]]
        plagia1=[Q[0],S[0],C[0]]
        plagia2=[Z[0],S[0],E[0]]
        trb=[row1,row2,row3,col1,col2,col3,plagia1,plagia2]
        for i in trb:
            triliza(i,piecesB)
    if p=="game over":
        break
    if remainB==0 and remainR==0:# αν κανενας απο τους δυο δεν εχει αλλα κομματια τελειωνει το παιχνιδι
        print "GAME OVER"
        print "TIE"
        p="game over"
    l=False # η ιδια διαδικασια για τον δευτερο παιχτη
    while l==False:
        ans2=raw_input("from the table player2: ")
        if ans2=="N":
            l=True
            f=False
            while f==False:
                play=raw_input("make your move player2: ")
                i=0
                d=False
                while i<=5 and d==False:
                    if play==paixths2[i]:
                        d=True
                        f=True
                    else:
                        i=i+1

            position=raw_input("position?: ")
            for i in theseis:
                if position==i:
                    add_elem(position,play,w[i],paixths2,q,i)
                    remainR=remainR-1
            print_table(Q,W,E,A,S,D,Z,X,C)
        elif ans2=="Y":
            l=True
            f=False
            while f==False:
                play=raw_input("select item: ")
                i=0
                v=False
                while i<=5 and v==False:
                    if play==paixths1[i]:
                        v=True
                        f=True
                    else:
                        i=i+1
            position=raw_input("from?: ")
            for i in theseis:
                if position==i:
                    position2=raw_input("position you want to be tansfered player2?: ")
                    for j in theseis:
                        if position2==j:
                            add_elem2(position2,play,w[i],q,w[j],j)
            print_table(Q,W,E,A,S,D,Z,X,C)
        row1=[Q[0],W[0],E[0]]
        row2=[A[0],S[0],D[0]]
        row3=[Z[0],X[0],C[0]]
        col1=[Q[0],A[0],Z[0]]
        col2=[W[0],S[0],X[0]]
        col3=[E[0],D[0],C[0]]
        plagia1=[Q[0],S[0],C[0]]
        plagia2=[Z[0],S[0],E[0]]
        trb=[row1,row2,row3,col1,col2,col3,plagia1,plagia2]
        for i in trb:
            triliza(i,piecesR)
    if remainB==0 and remainR==0:
        print "GAME OVER"
        print "TIE"
        p="game over"
    
        
