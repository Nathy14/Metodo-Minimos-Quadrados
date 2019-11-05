def metodo_minimos(x,y,tam):
  for i in range (0, tam):                                          #somatória de xi
    totalx += x[i]
  for j in range(0, tam):                                           #somatória de y1
    totaly += y[j]
  for k in range (0, tam):                                          #somatória de xi^2
    x_quadrado += x[k]**2
  for l in range(1, tam):                                           #somatória de xi*yi
    xy += x[l]*y[l]
  a0 = (x_quadrado*totaly)-(xy*totalx)/(tam*x_quadrado)-(totalx**2) #calculo do a0
  a1 = (tam*xy)-(totalx*totaly)/(tam*x_quadrado)-(totalx**2)        #calculo do a1
  print("A reta aproximadora de pontos é {}*x+({})".format(a1,a0))


def main():                                                         #função principal
  tam = int(input("Digite a quantidade de pontos: \n"))
  x= [tam]
  y=[tam]
  for j in range(0,tam):
    x.append(j)
    x[j] = float(input("Digite o valor de x: "))
  for i in range(0,tam):
    y.append(i)
    y[i]=float(input("\nDigite o valor de y: "))
  metodo_minimos(x,y,tam)

main()
