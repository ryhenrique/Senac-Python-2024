
def converter(celsius):
    return (celsius * 9 / 5 + 32)

celsius = float(input("Digite sua temperatura em Celsius: "))
resultado = converter(celsius)
print(f"A temperatura de {celsius}°C é equivalente a {resultado}°F")