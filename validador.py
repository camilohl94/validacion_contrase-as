# se importa string para validar caracteres especiales 
import string

# se define la funcion que valida la contraseña y que recibe como argumento la contarseña del usuario
def validar_contraseña(contraseña):
     #validar que la contarseña tenga mas de 8 caracteres
     if len(contraseña) <= 8:
        print('La contraseña debe tener más de 8 caracteres.')
        return False
     # validar si se encuentra alguna mayuscula en la contraseña
     contiene_mayúsculas = any(caracter.isupper() for caracter in contraseña)
     # validar si se encuentra alguna minuscula en la contraseña
     contiene_minusculas =any(caracter.islower() for caracter in contraseña)
     #validar si se encuentra algun caracter especial en la contraseña
     contiene_especiales = any(caracter in string.punctuation for caracter in contraseña)
     #validar si se encuentra algun numero en la contraseña
     contiene_digitos = any(caracter.isdigit() for caracter in contraseña)
                 
       # verificar si se cumple con todos los requisitos de la contraseña  con un if y si no se cumple se retorna un false 
     if contiene_mayúsculas and contiene_minusculas and contiene_especiales and contiene_digitos:
        print('agregada correctamente')
        return True
     else:
        print('la contaseña no cumple con algunos de estos  requisitos : caracter especial, mayuscula,numeros, minusculas ')
        return False
# almacenar el valor de una contraseña
contraseña = input('por favor ingrese una contraseña:')

# imprimir el resultado del ingreso de la contraseña 
print(validar_contraseña(contraseña))
