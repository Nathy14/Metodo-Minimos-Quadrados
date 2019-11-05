def metodo_minimos(x,y,tam):
  totalx = 0
  totaly = 0
  x_quadrado = 0
  xy = 0
  for i in range (0, tam):                                                   #somatória xi
    totalx += x[i]
  for j in range(0, tam):                                                    #somatória yi
    totaly += y[j]
  for k in range (0, tam):                                                   #somatória x^2
    x_quadrado += x[k]**2
  for l in range(1, tam):                                                    #somaória x*y
    xy += x[l]*y[l]
  a0 = ((x_quadrado*totaly)-(xy*totalx))/((tam*x_quadrado)-(totalx**2))      #cálculo a0
  a1 = ((tam*xy)-(totalx*totaly))/((tam*x_quadrado)-(totalx**2))             #cálculo a1
  print("A reta aproximadora de pontos é {}*x+({})".format(a1,a0))  


def main():
  tam = int(input("Digite a quantidade de pontos: \n"))
  c= [tam]
  v=[tam]
  for j in range(0,tam):
    c.append(j)
    c[j] = float(input("Digite o valor de x: "))
  for i in range(0,tam):
    v.append(i)
    v[i]=float(input("\nDigite o valor de y: "))
  metodo_minimos(c,v,tam)

main()
