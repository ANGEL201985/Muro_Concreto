import matplotlib.pyplot as plt 
import matplotlib.patches as patches 

fig, ax = plt.subplots(figsize =(10,6))

#Definimos nuestro datos
ancho_muro = 4.9 
altura_total_muro = 6.5
altura_muro = 5.6
distancia_corona_drenaje_1 = 4.4
distancia_corona_drenaje_2 = 2.6
distancia_drenaje_corona = 2.3
distancia_entre_drenajes = 1.8
peralte_zapata = 0.9
Ap = 0.7
ancho_inferior_muro = 0.81
At = 3.39
ancho_superior_muro = 0.25
punto_inicia_drenaje_x = 1.51
punto_inicia_drenaje_1_y = 2.1
punto_inicia_drenaje_2_y =3.9
x1 = (distancia_corona_drenaje_1)*(ancho_inferior_muro- ancho_superior_muro)/(altura_muro)
x2 = (distancia_corona_drenaje_2)*(ancho_inferior_muro- ancho_superior_muro)/(altura_muro)
altura_corona = 0.3



#Definimos nuestro puntos coordenados
coordenadas_muro = [(0,0),(ancho_muro,0),(ancho_muro, peralte_zapata),(Ap + ancho_inferior_muro, peralte_zapata),(Ap + ancho_inferior_muro, altura_total_muro), (Ap + ancho_inferior_muro-ancho_superior_muro, altura_total_muro),(Ap, peralte_zapata), (0, peralte_zapata), (0,0)]

# Graficando nuestro muro usando las coordenadas que definimos
muro = patches.Polygon(coordenadas_muro, closed = True, facecolor = 'grey', edgecolor = 'black')
ax.add_patch(muro)

#Dibujando nuestro tubos de drenaje
ax.plot([punto_inicia_drenaje_x - ancho_superior_muro-x1, punto_inicia_drenaje_x], [punto_inicia_drenaje_1_y, punto_inicia_drenaje_1_y], color = 'deepskyblue', linewidth = 4)
ax.text(punto_inicia_drenaje_x + 0.2, punto_inicia_drenaje_1_y, 'PVC 2"\n Tubo de Drenaje', fontsize = 10, va = 'center')

ax.plot([punto_inicia_drenaje_x - ancho_superior_muro-x2, punto_inicia_drenaje_x], [punto_inicia_drenaje_2_y, punto_inicia_drenaje_2_y], color = 'deepskyblue', linewidth = 4)
ax.text(punto_inicia_drenaje_x + 0.2, punto_inicia_drenaje_2_y, 'PVC 2"\n Tubo de Drenaje', fontsize = 10, va = 'center')

# Graficaremos las flechas de las cotas usando la funccion annotate
ax.annotate(text = '', xy =(-0.6, peralte_zapata), xytext = (-0.6, altura_total_muro), arrowprops=dict(arrowstyle='<->'))
ax.text(-0.5, altura_total_muro/2, altura_muro, va ='center')

# Agregamos la cota de la zapata
ax.annotate(text = '', xy =(-0.6, 0), xytext = (-0.6, peralte_zapata), arrowprops=dict(arrowstyle='<->'))
ax.text(-0.5, peralte_zapata/2, peralte_zapata, va ='center')

# Agregamos la cota altura total del muro
ax.annotate(text = '', xy =(-0.7, 0), xytext = (-0.7, altura_total_muro), arrowprops=dict(arrowstyle='<->'))
ax.text(-1.2, altura_total_muro/2, altura_total_muro, va ='center')

# Agregamos la cota de la altura de la corona

ax.annotate(text = '', xy =(Ap, altura_total_muro-altura_corona), xytext = (Ap, altura_total_muro), arrowprops=dict(arrowstyle='<->'))
ax.text(Ap-0.4, altura_total_muro-altura_corona/2, altura_corona, va ='center')

# Agregamos la cota de la altura de drenaje 2

ax.annotate(text = '', xy =(Ap, altura_total_muro-distancia_corona_drenaje_2), xytext = (Ap, altura_total_muro-altura_corona), arrowprops=dict(arrowstyle='<->'))
ax.text(Ap-0.4, altura_total_muro-distancia_corona_drenaje_2/2, distancia_drenaje_corona, va ='center')

ax.annotate(text = '', xy =(Ap, altura_total_muro-distancia_corona_drenaje_1), xytext = (Ap, altura_total_muro-distancia_corona_drenaje_2), arrowprops=dict(arrowstyle='<->'))
ax.text(Ap-0.4, altura_total_muro-(distancia_corona_drenaje_1 + distancia_corona_drenaje_2)/2, distancia_entre_drenajes , va ='center')



# Agergamos el texto del ancho de la parte superior del muro
ax.text(punto_inicia_drenaje_x - ancho_superior_muro/2 -0.2, altura_total_muro + 0.2 ,ancho_superior_muro, va ='center')

# Graficamos la flecha Ap
ax.annotate(text = '', xy =(0, -0.4), xytext = (Ap, -0.4), arrowprops=dict(arrowstyle='<->'))
ax.text(Ap/4, -0.3, Ap , va ='center')

# Graficamos la flecha ancho inferior muro
ax.annotate(text = '', xy =(Ap, -0.4), xytext = (Ap + ancho_inferior_muro , -0.4), arrowprops=dict(arrowstyle='<->'))
ax.text(Ap + ancho_inferior_muro/4, -0.3, ancho_inferior_muro , va ='center', ha= 'center')

# Graficamos la flecha At
ax.annotate(text = '', xy =(Ap + ancho_inferior_muro, -0.4), xytext = (ancho_muro , -0.4), arrowprops=dict(arrowstyle='<->'))
ax.text(Ap + ancho_inferior_muro + At/4, -0.3, At , va ='center', ha= 'center')

# Graficamos la flecha At
ax.annotate(text = '', xy =(0, -0.6), xytext = (ancho_muro , -0.6), arrowprops=dict(arrowstyle='<->'))
ax.text(ancho_muro/2, -0.8, ancho_muro , va ='center', ha= 'center')

# Agrego el texto MCA 6.5
ax.text(ancho_muro/2, -1.2, f'MCA{altura_total_muro}' , va ='center', fontsize = 12, fontweight = 'bold', ha= 'center', color ='blue')

ax.set_title("MURO DE CONCRETO ARMADO", fontsize = 14)
ax.set_xlim(-2, 6)
ax.set_ylim(-2, 7)
plt.tight_layout()
ax.set_aspect('equal')
plt.show()