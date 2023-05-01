import phonenumbers
from phonenumbers import geocoder, carrier

phoneNumber= phonenumbers.parse("+numero de telefone")
Carrier= carrier.name_for_number(phoneNumber, "pt-BR")
region= geocoder.description_for_number(phoneNumber,"pt-BR")

print("A operadora é: ", Carrier)
print("O estado é:", region)
