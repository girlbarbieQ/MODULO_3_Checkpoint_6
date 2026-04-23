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

La clase define qué es un usuario. Los objetos son usuarios concretos.

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

### ❌ ¿Cuándo NO usar clases?
No siempre son necesarias. Evitalas cuando:
- El programa es muy pequeño
- Solo necesitas funciones simples
- No hay estructuras complejas

### ⚠️ Errores comunes
#### ❌ 1. No usar self
````python
def __init__(name): #MAL

def __init__(self, name): #BIEN
````
#### ❌ 2. Confundir clases con objetos
````python
User #CLASE
User('Ana', 20) #OBJETO
````
#### ❌ 3. No entender que cada objeto es independiente
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

## 🔹 ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
El método que se ejecuta automáticamente cuando se crea una instancia (objeto) de una clase en Python es:
````plain text
__init__
````

### 🧠 ¿Qué es __init__?
El método __init__ es un método especial (también llamado método dunder) que actúa como constructor de la clase.
Se ejecuta automáticamente en el momento en que se crea un objeto a partir de esa clase.

#### 💡 Traducción simple
👉 “es el método que se encarga de preparar el objeto cuando nace”

### 🧠 ¿Para qué sirve?
El método __init__ se utiliza para:
- Inicializar los datos del objeto
- Asignar valores a los atributos
- Preparar el objeto para su uso

### 💻 Ejemplo básico
````python
class Person:
    def __init__(self, name):
        self.name = name

person1 = Person("Luccia")
````
#### 📌 Explicación
En este ejemplo, se define una clase llamada Person. Dentro de ella, el método __init__ recibe un parámetro (name) y lo asigna al objeto mediante self.name.

Cuando se crea el objeto person1 = Person("Luccia"), Python ejecuta automáticamente el método __init__, pasando el valor "Luccia" como argumento. Como resultado, el objeto queda inicializado con ese dato.

### 🧠 ¿Qué significa self aquí?
Self representa el objeto que se está creando.
````python
self.name = name
````
👉 significa:
“guarda este valor dentro de ESTE objeto”

### 🧠 ¿Qué pasa si no usas _init_?
Puedes crear una clase sin _init_, pero no podrás inicializar datos fácilmente.
````python
class Person:
    pass

p = Person()
````
Esto crea un objeto vacío, sin información.

### ⚠️ Errores comunes
#### ❌ 1. Olvidar self
````python
def __init__(name):  # MAL
def __init__(self, name):  # BIEN
````
#### ❌ 2. Pensar que hay que llamarlo manualmente
````python
person1.__init__("Luccia")  # NO se hace
````
Python lo ejecuta automáticamente

### 💻 Ejemplo más completo
````python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2020)
````
#### 📌 Explicación
Cuando se crea car1, Python ejecuta automáticamente __init__, asignando "Toyota" a brand y 2020 a year. 
Esto permite que el objeto tenga sus propios datos desde el momento en que se crea.

### 🧠 ¿Por qué es importante?
El método __init__ es fundamental porque:

- Permite crear objetos ya configurados
- Evita tener que asignar datos manualmente después
- Hace el código más limpio y organizado

## 🔹 ¿Cuáles son los tres verbos de API?
Los tres verbos principales de una API son:

👉 GET, POST y DELETE

Estos verbos forman parte del protocolo HTTP y se utilizan para indicar qué acción quieres realizar sobre los datos.

### 🧠 ¿Qué es un verbo en una API?
Un verbo HTTP es una instrucción que le dice al servidor qué quieres hacer.

👉 Es como decir:
- “quiero ver datos”
- “quiero crear algo”
- “quiero eliminar algo”

### 🧠 Los tres verbos principales
#### ✅ 1. GET --> Obtener datos
El verbo GET se utiliza para consultar información.
- No modifica nada
- Solo lee datos

##### 💻 Ejemplo
````http
GET /users
````
👉 Esto significa:

“dame todos los usuarios”

###### 📌 Uso real
- Ver una lista de productos
- Ver un perfil de usuario
- Obtener datos de una API
  
###### ⚠️ Importante
👉 GET es seguro

👉 No cambia la base de datos

#### ✅ 2. POST --> Crear datos
El verbo POST se utiliza para enviar información al servidor y crear nuevos datos.

##### 💻 Ejemplo
````http
POST /users
````
````json
{
  "name": "Luccia",
  "age": 23
}
````
👉 Esto significa:

“crea un nuevo usuario con estos datos”

###### 📌 Uso real
- Crear una cuenta
- Publicar un comentario
- Subir información

###### ⚠️ Importante
👉 POST sí modifica la base de datos

#### ✅ 3. DELETE --> Eliminar datos
El verbo DELETE se utiliza para borrar información del servidor.

##### 💻 Ejemplo
````http
DELETE /users/1
````
👉 Esto significa:

“elimina el usuario con id 1”

###### 📌 Uso real

- Eliminar una cuenta
- Borrar un producto
- Quitar un comentario

### 🧠 ¿Cómo funcionan juntos?
En una API, estos verbos permiten realizar operaciones básicas sobre los datos.

👉 Esto se conoce como operaciones CRUD:

- GET --> Read (leer)
- POST --> Create (crear)
- DELETE --> Delete (eliminar)

#### 💻 Ejemplo completo
Imagina una app de usuarios:
- GET --> ver usuarios
- POST --> crear usuario
- DELETE --> eliminar usuario

#### 💡 Nota importante
Existen más verbos como:
- PUT --> reemplazar datos
- PATCH --> modificar parcialmente

Pero GET, POST y DELETE son los más básicos y utilizados al empezar.

### ⚠️ Errores comunes
#### ❌ 1. Confundir GET con POST
-  GET es para leer
- POST es para crear

#### ❌ 2. Pensar que GET puede modificar datos
GET NUNCA debe cambiar información

#### ❌ 3. Usar DELETE sin identificar recurso
````http
DELETE /users  #MAL
DELETE /users/1  #BIEN
````
### 🧠 ¿Por qué son importantes?
Porque permiten que el cliente (frontend) y el servidor (backend) se comuniquen correctamente.

👉 Sin estos verbos, no podrías:
- ver datos
- crear información
- eliminar contenido

### 🧠 En una frase
👉 Los verbos de API (GET, POST y DELETE) indican qué acción quieres realizar sobre los datos en un servidor.
