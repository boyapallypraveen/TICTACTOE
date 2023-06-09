class tictactoe:
  def __init__(self):
    self.d = []
    for i in range(1,11):
      self.d.append(0)
  def addx(self,n):
    if self.d[n]==0:
      self.d[n]="X"
    else:
      print("already place is occupied")
  def addo(self,n):
    if self.d[n]==0:
      self.d[n]="O"
    else:
      print("already place is occupied")
  def show(self):
    for i in range(1,10):
      if i%3!=0:
        print(self.d[i],end="|")
      else:
        print(self.d[i],end="|")
        print()
  def checkgamex(self):
    if self.d[1]==self.d[2]==self.d[3]=="X":
      return self.d[1]
    elif self.d[4]==self.d[5]==self.d[6]=="X":
      return self.d[4]
    elif self.d[7]==self.d[8]==self.d[9]=="X":
      return self.d[7] 
    elif self.d[1]==self.d[4]==self.d[7]=="X":
      return self.d[1]
    elif self.d[2]==self.d[5]==self.d[8]=="X":
      return self.d[2]
    elif self.d[3]==self.d[6]==self.d[9]=="X":
      return self.d[3]
    elif self.d[1]==self.d[5]==self.d[9]=="X":
      return self.d[1]
    elif self.d[3]==self.d[5]==self.d[7]=="X":
      return self.d[3]
    else:
      return None
  def checkgameo(self):
    if self.d[1]==self.d[2]==self.d[3]=="O":
      return self.d[1]
    elif self.d[4]==self.d[5]==self.d[6]=="O":
      return self.d[4]
    elif self.d[7]==self.d[8]==self.d[9]=="O":
      return self.d[7] 
    elif self.d[1]==self.d[4]==self.d[7]=="O":
      return self.d[1]
    elif self.d[2]==self.d[5]==self.d[8]=="O":
      return self.d[2]
    elif self.d[3]==self.d[6]==self.d[9]=="O":
      return self.d[3]
    elif self.d[1]==self.d[5]==self.d[9]=="O":
      return self.d[1]
    elif self.d[3]==self.d[5]==self.d[7]=="O":
      return self.d[3]
    else:
      return None
  def checkdraw(self):
    flag = 0
    for i in range(1,10):
      if self.d[i]==0:
        flag = 1
    if flag ==1 :
      return 1
    else:
      return 0
ob = tictactoe()
while True:
  print()
  print("Enter position for player X : ")
  n = int(input())
  ob.addx(n)
  ob.show()
  game = ob.checkgamex()
  if game!=None:
    print(game,"wins the game")
    break 

  draw = ob.checkdraw()
  if draw==0:
    print("Game draw")
    break 
  print()
  print("Enter position for player O : ")
  n= int(input())
  ob.addo(n)
  ob.show()
  game = ob.checkgameo()
  if game!=None:
    print(game,"wins the game")
    break 

  draw = ob.checkdraw()
  if draw==0:
    print("Game draw")
    break 
    
    