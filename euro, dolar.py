tasa_usd = 16.80  
tasa_euro = 18.64
entrada = 0 

while True:
    entrada = input("Cantidad de pesos mexicanos a convertir: ")

    try:
        pesos = float(entrada) 
    except ValueError:
        print("numero invalido")
        continue 

    dolares = pesos / tasa_usd
    euros = pesos / tasa_euro

    print(f"{pesos} MXN son {dolares:.2f} USD y {euros:.2f} EUR")
