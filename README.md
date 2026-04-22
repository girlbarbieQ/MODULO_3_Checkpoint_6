# DOCUMENTACION

## 🔹 ¿Para qué usamos Clases en Python?
Las clases en Python se utilizan para organizar el código, representar objetos del mundo real y
construir programas más estructurados, reutilizables y escalables.
Son uno de los conceptos fundamentales de la Programación Orientada a Objetos (POO)

### 🧠 ¿Qué es una clase?
Una clase es una plantilla o molde que define cómo serán ciertos objetos dentro de un programa.

👉 No es un objeto en sí, sino la "idea" del objeto.

#### 💡 Ejemplo mental
- Clase --> "Usuario"
- Objeto --> "Barbara", "Luccia", "Ana"

👉 La clase define qué es un usuario

👉 Los objetos son usuarios concretos

### 🧠 ¿Qué contiene una clase?
Una clase está compuesta principalmente de lo siguiente:

#### 🔻 Atributos (datos)
Son las carecteristicas del objeto:
- Nombre
- Edad
- Email

#### 🔻 Métodos (funciones)
Son las acciones que el objeto puede realizar:
- Saludar
- Iniciar sesión
- Comprar

##### 💻 Ejemplo completo
python´´´´
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hola, soy {self.name} y tengo {self.age} años"
´´´´
