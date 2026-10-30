#Faren to cel
def ftoc(farenheit):
    celci= (farenheit-32)*5/9
    return celci

#celci to faren
def ctof(celci):
    farenheit= (celci*9/5)+ 32
    return farenheit

#celci to reamur
def ctor(celci):
    reamur= celci*4/5
    return reamur

#reamur to celci
def rtoc(reamur):
    celci= reamur*5/4
    return celci

#celci to kelvin
def ctok(celci):
    kelvin= celci+273.15
    return kelvin

#kelvin to celci
def ktoc(kelvin):
    celci= kelvin-273.15
    return celci

def main():
    print(__name__)
    celci= 100
    print(f"Celcius: {celci} °C")
    print(f"Reamur: {ctor(celci)} °R")

if __name__ == "__main__":
    main()