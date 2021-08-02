def hasAP(listOfNumber,difference):
    listOfNumber.sort()
    for i in range(len(listOfNumber)-2):
        if listOfNumber[i] == listOfNumber[i+1] - difference == listOfNumber[i+2] - difference*2:
            return True
    return False

def sameHorizontalValue(moves): 
    horizontalValueDictionary = {}
    for move in moves:
        if move[0] in horizontalValueDictionary.keys():
            horizontalValueDictionary[move[0]].append(move[1])
        else:
            horizontalValueDictionary.update({move[0]:[move[1]]})
    for value in horizontalValueDictionary.values():
        if hasAP(value,1):
            return True
    return False

def sameVerticalValue(moves):
    verticalValueDictionary = {}
    for move in moves:
        if move[1] in verticalValueDictionary.keys():
            verticalValueDictionary[move[1]].append(move[0])
        else:
            verticalValueDictionary.update({move[1]:[move[0]]})
    for value in verticalValueDictionary.values():
        if hasAP(value,1):
            return True
    return False


def sameDiagonalValue(moves):
    DiagonalValueList = []
    for move in moves:
        tong = move[0] + move[1]
        hieu = move[0] - move[1]
        DiagonalValueList.append([tong,hieu])
    sameDiagonalValueTSP = {}
    sameDiagonalValuePST = {}
    for i in DiagonalValueList:
        if i[1] in sameDiagonalValueTSP.keys():
            sameDiagonalValueTSP[i[1]].append(i[0])
        else:
            sameDiagonalValueTSP.update({i[1]:[i[0]]})
    for i in DiagonalValueList:
        if i[0] in sameDiagonalValuePST.keys():
            sameDiagonalValuePST[i[0]].append(i[1])
        else:
            sameDiagonalValuePST.update({i[0]:[i[1]]})
    for value in sameDiagonalValueTSP.values():
        if hasAP(value,2):
            return True
    for value in sameDiagonalValuePST.values():
        if hasAP(value,2):
            return True
    return False

def TaoBang(KichThuoc, ToaDoX, ToaDoO):
    print('  ',end ='')
    for x in range(KichThuoc):
        print(x,end = ' ')
    for x in range(KichThuoc):
        print(x, end = ' ')
        for y in range(KichThuoc):
            if [x,y] in ToaDoX:
                print("X", end = " ")
            elif [x,y] in ToaDoO:
                print("O", end = " ")
            else:
                print("-", end = " ")
        print()

def ToaDo():
    NuocDi = []
    ToaDo = input("Nhap nuoc di cua ban (voi cu phap x,y VD: 1,2): ")
    for i in ToaDo.split(","):
        NuocDi.append(int(i))
    return NuocDi
def isOver(movesX,movesO):
    return sameVerticalValue(movesX) or sameVerticalValue(movesO) or sameDiagonalValue(movesX) or sameDiagonalValue(movesO) or sameHorizontalValue(movesX) or sameHorizontalValue(movesO)
movesX = []
movesO = []
endGame = False
while not endGame:

  while True:
    listToaDoX = ToaDo()
    if listToaDoX in movesX or listToaDoX in movesO:
      print("Toa do da duoc di")
    else:
      break
  movesX.append(listToaDoX)
  TaoBang(7,movesX,movesO)
  
  endGame = isOver(movesX,movesO)
  
  if endGame:
    print("Tro choi ket thuc")
    
    break

  while True:
    listToaDoO = ToaDo()
    if listToaDoO in movesX or listToaDoO in movesO:
      print("Toa do nay da duoc di")
    else:
      break

  movesO.append(listToaDoO)
  TaoBang(7,movesX,movesO)
  endGame = isOver(movesX,movesO)
  if endGame:
    print("Tro choi ket thuc")
    
    break
