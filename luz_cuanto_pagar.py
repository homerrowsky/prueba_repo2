import math

def luz(medicion):
    '''(int) -> int
    Calcula la cantidad a pagar de acuerdo al consumo de energia (kilowatts)
    '''
    #Precio kilowattshora de acuerdo al consumo
    costo_kw = {'basico':.751, 'intermedio': .915, 'excedente': 2.673}
    
    #Define cantidad de kilowattshoras usados para cada rango de consumo
    consumo = [0 ,0 , 0]
    if medicion > 280:
            consumo = [150, 130, medicion - 280]
    elif medicion > 150 <= 280:
            consumo = [150, medicion - 130, 0]
    else :
            consumo = [medicion, 0, 0]

    #Calculo a pagar
    costo_energia = consumo[0] * costo_kw['basico'] \
               + consumo[1] * costo_kw['intermedio'] \
               + consumo[2] * costo_kw['excedente']

    iva = costo_energia * .16
    subtotal = costo_energia + iva
    #Imprime el costo base de la energia
    print 'Costo energia:', costo_energia
    print 'IVA:', iva
    #print(iva)
    print 'SubTotal:', subtotal
    #Calucula e imprime el impuesto de alumbrado publico
    der_alum_publ = costo_energia * .1
    print 'DerechoAlumbradoPublico:', der_alum_publ
    #Calcular el total
    total = subtotal + der_alum_publ
    print 'Total:', total

    return math.ceil(total)
