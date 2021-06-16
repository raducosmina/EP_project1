import numpy as np
import math

def median(persoane):
    persoane_sortate = np.sort(np.unique(persoane))
    persone_sort = np.sort(persoane)
    print(persoane_sortate)

    size_p = persone_sort.shape
    size = persoane_sortate.shape
    if size[0] % 2 == 0:
        medianul = (persoane_sortate[int((size[0] / 2) - 1)] + persoane_sortate[int(size[0] / 2)]) / 2
    else:
        medianul = persoane_sortate[int((size[0] - 1) / 2)]
    print('Medianul:' + str(medianul))
    return medianul

def media_aritmetica(persoane):
    persoane_sortate = np.sort(np.unique(persoane))
    persone_sort = np.sort(persoane)
    print(persoane_sortate)

    size_p = persone_sort.shape
    size = persoane_sortate.shape
    # media aritmetica
    suma = 0
    for persoana in persone_sort:
        suma = suma + persoana
    media_artimetica = suma / size_p[0]
    print('Media aritmetica:' + str(media_artimetica))
    return media_artimetica

def domeniu_dispersie(persoane):
    # domeniul de dispersie
    domeniu_dispersie = max(persoane) - min(persoane)
    print('Domeniu dispersie:' + str(domeniu_dispersie))


def deviatia(persoane):
    #deviatia standard
    persoane_sortate = np.sort(np.unique(persoane))
    persone_sort = np.sort(persoane)
    media_ar = media_aritmetica(persoane)
    size_p = persone_sort.shape
    # variantia
    suma_variatie = 0
    for persoana in persoane:
        suma_variatie = suma_variatie + pow(persoana - media_ar, 2)
    variantia = suma_variatie / size_p[0]
    deviatia_standard = math.sqrt(variantia)
    print('Deviatia standard:'+str(deviatia_standard))
    return deviatia_standard

def coef_variatie (persoane):
    dev = deviatia(persoane)
    m_a = media_aritmetica(persoane)
    #coeficientul de variație
    coeficientul_variație = dev/m_a
    print('Coeficientul de variatie:'+str(coeficientul_variație))
    return coeficientul_variație
persoane = [40, 43, 34, 44, 52, 51, 63,36, 54, 43, 67, 45, 55, 57, 48, 45, 71, 51, 54, 47, 39, 50, 26, 62,33, 40, 42, 55,29, 45]

medianul = median(persoane)
med_ar = media_aritmetica(persoane)
dom_disp = domeniu_dispersie(persoane)



