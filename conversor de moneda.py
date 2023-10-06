tasa_usd = 16.80  
tasa_euro = 23.52  

while True:
    entrada = input("Cantidad de pesos mexicanos a convertir: ")

    if entrada.lower() == 'Exit':
        break  

    try:
        pesos = float(entrada) 
    except ValueError:
        print("numero invalido")
        continue 

    dolares = pesos / tasa_usd
    euros = pesos / tasa_euro

    print(f"{pesos} MXN son {dolares:.2f} USD y {euros:.2f} EUR")
