
def es_as_privado(asn):
    return 64512 <= asn <= 65534 or 4200000000 <= asn <= 4294967294

asn = int(input("Ingrese el número de Sistema Autónomo (AS): "))
if es_as_privado(asn):
    print(f"El AS {asn} es PRIVADO.")
else:
    print(f"El AS {asn} es PÚBLICO.")
