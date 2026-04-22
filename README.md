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

### 💻 Ejemplo completo
```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hola, soy {self.name} y tengo {self.age} años"

user1 = User("Luccia", 23)
user2 = User("Ana", 30)

print(user1.greet())
print(user2.greet())
```
#### 📌 Explicación
En este código se define una clase llamada User, que actúa como una plantilla para crear objetos que representan usuarios.

El método _init_ es el constructor de la clase y se ejecuta automáticamente cada vez que se crea un nuevo objeto. Recibe dos parámetros (name y age) y los asigna al objeto mediante self, lo que permite que cada usuario tenga sus propios datos independientes.

Después, se define el método greet, que utiliza los atributos del objeto (self.name y self.age) para construir y devolver un mensaje personalizado. Este método muestra cómo un objeto no solo almacena información, sino que también puede utilizarla.

A continuación, se crean dos objetos (user1 y user2) a partir de la clase User, cada uno con valores distintos. Aunque ambos provienen de la misma clase, mantienen sus propios datos.

Finalmente, al ejecutar print(user1.greet()) y print(user2.greet()), se llama al método greet de cada objeto, generando mensajes diferentes según la información almacenada en cada uno. Esto demuestra cómo múltiples instancias de una misma clase pueden comportarse de forma similar pero con datos distintos.

### 🧠 ¿Para que sirven las clases?
Las clases tiene varios objetivos clave en programación:

#### ✅ 1. Organizar el código
Sin clases el código se vuelve desordenado 

##### 💻 Ejemplo sin clases
````python
user_name = 'Ana'
user_age = 23
````
##### 💻 Ejemplo con clases
````python
User('Ana', 23)
````
- Más limpio con clases
- Más claro con clases

#### ✅ 2. Reutilizar código
Puedes usar la misma clase para crear muchos objetos.

👉 No necesitas repetir código constantemente

#### ✅ 3. Representar la realidad
Las clases permiten modelar cosas reales:
- Usuarios
- Productos
- Coches
- Libros

#### ✅ 4. Escalar proyectos
Cuando un proyecto crece, las clases hacen que el código sea:
- Más facil de mantener
- Más facil de entender
- Más facil de ampliar

### 🧠 ¿Cuándo usar clases?
Usa clases cuando:
- Trabajas con entidades (usuarios, objetos, precios, etc.)
- Necesitas agrupar datos + funciones
- Tu código empieza a crecer
- Quieres reutilizar lógica

### ¿❌ Cuándo NO usar clases?
No siempre son necesarias. Evitalas cuando:
- El programa es muy pequeño
- Solo necesitas funciones simples
- No hay estructuras complejas

### ⚠️ Errores comunes
#### 1. No usar self
````python
def __init__(name): #MAL

def __init__(self, name): #BIEN
````
#### 2. Confundir clases con objetos
````python
User #CLASE
User('Ana', 20) #OBJETO
````
#### 3. No entender que cada objeto es independiente
````python
user1 = User('Ana', 20)
user2 = User('Luis', 25)
````
👉 Son objetos distintos, con datos distintos

### 🧠 Conceptos clave para recordar 
- Clase --> plantilla
- Objeto --> instancia de la clase
- Atributo --> dato
- Método --> acción
- self --> el objeto actual

