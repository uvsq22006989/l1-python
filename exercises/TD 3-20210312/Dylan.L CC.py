def rotation():
    """La fonction permet de tourner a 180 degree mais je n'ai pas reussi à la modifier à temps pour 90"""
    mat =loading(nomImgCourante) 
    matRot=[[(0,0,0,0)]*nbrCol(mat) for k in range(nbrLig(mat))]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            matRot[nbrCol(mat)-i][nbrLig(mat)-j]=mat[i][j]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=matRot[i][j]
    modify(nomImgCourante)


#def rotation():
 #   """La fonction permet de tourner a 90 degree l'image"""
  #  mat =loading(nomImgCourante) 
   # matRot=[[(0,0,0,0)]*nbrCol(mat) for k in range(nbrLig(mat))]
    #for i in range(nbrLig(mat)):
     #   for j in range(nbrCol(mat)):
      #      matRot[nbrCol(mat)][nbrLig(mat)-j]=mat[i][j] horizontale??
      #      matRot[nbrCol(mat)-i][nbrLig(mat)]=mat[i][j] verticale ??
    #for i in range(nbrLig(mat)):
     #   for j in range(nbrCol(mat)):
      #      mat[i][j]=matRot[i][j]
    #modify(nomImgCourante)

