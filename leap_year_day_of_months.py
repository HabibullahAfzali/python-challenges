#------- Is leap year ? -----------

def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")



# -----------  Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LABORATORIO 4.1.3.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función; este truco acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.     --------------------

def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    # Lista con días por mes (no considera el valor del año, solo el mes)
    days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año es bisiesto y ajustar los días de febrero si es necesario
    if is_year_leap(year):
        days_by_month[1] = 29  # Febrero tiene 29 días en años bisiestos

    # Verificar la validez de los argumentos
    if month < 1 or month > 12:
        return None  # Mes fuera del rango válido

    # Devolver el número de días correspondiente al mes dado
    return days_by_month[month - 1]  # Restamos 1 porque los índices de la lista empiezan en 0

# Código de prueba
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
 
 

#  Escenario
# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
 
def is_year_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        days_by_month[1] = 29

    if month < 1 or month > 12:
        return None

    return days_by_month[month - 1]

def day_of_year(year, month, day):
    # Verificar la validez de los argumentos
    if type(year) != int or year <= 0:
        return None
    if type(month) != int or month < 1 or month > 12:
        return None
    if type(day) != int or day < 1 or day > days_in_month(year, month):
        return None

    # Calcular el día del año
    day_of_year = day
    for m in range(1, month):
        days_in_current_month = days_in_month(year, m)
        if days_in_current_month is None:
            return None
        day_of_year += days_in_current_month

    return day_of_year

# Ejemplo de prueba
print(day_of_year(2000, 12, 31))  # Salida esperada: 366 (porque 2000 es bisiesto)

