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

## 🔹 ¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB es una base de datos:

👉 NoSQL (Not Only SQL)

Esto significa que no utiliza el modelo tradicional de bases de datos relacionales (como MySQL o PostgreSQL), sino un modelo diferente basado en documentos.

### 🧠 ¿Qué significa realmente NoSQL?
El término NoSQL no significa “sin SQL”, sino: “no solo SQL”. 
Es decir, engloba sistemas de bases de datos que no siguen la estructura clásica de tablas, filas y columnas.

### 🧠 ¿Cómo funcionan las bases de datos SQL?
Las bases de datos SQL (relacionales) organizan la información de forma muy estructurada. Usan:
- Tablas
- Filas
- Columnas
- Relaciones entre tablas

#### 💻 Ejemplo en SQL
Tabla users

| id | Name | Age |
|----|------|-----|
| 1  | Ana  | 20  |
| 2  | Luis | 30  |

Todo debe seguir esa estructura obligatoriamente.

#### ⚠️ Característica clave de SQL
Estructura rígida (schema fijo). 
Antes de guardar datos, debes definir cómo serán.

### 🟩 ¿Cómo funciona MongoDB?
MongoDB utiliza un modelo completamente diferente.

👉 En lugar de tablas, usa:
- Bases de datos
- Colecciones
- Documentos

### 🧠 Estructura en MongoDB
- Base de datos --> contenedor general
- Colección --> grupo de documentos (similar a tabla)
- Documento --> unidad de datos (similar a fila, pero más flexible)

#### 💻 Ejemplo de documento
````json
{
  "name": "Luccia",
  "age": 23,
  "skills": ["Python", "MongoDB"]
}
````
👉 Esto es un documento real en MongoDB.

### 🔥 Diferencia fundamental
- SQL --> estructura fija
- MongoDB --> estructura flexible

### 🧠 ¿Qué significa que MongoDB sea flexible?
En MongoDB, los documentos dentro de la misma colección no tienen que tener la misma estructura.

#### 💻 Ejemplo
````json
{ "name": "Ana" }
{ "name": "Luis", "age": 30 }
{ "name": "Carlos", "age": 25, "city": "Madrid" }
````
👉 Todos pueden coexistir sin problema.

##### 💥 Esto es clave
No necesitas definir previamente todas las columnas como en SQL.

### 🧠 ¿Por qué se usa MongoDB?
MongoDB se utiliza porque permite trabajar de forma más rápida y flexible, especialmente en aplicaciones modernas.

### 🔥 Ventajas principales
#### ✅ 1. Flexibilidad
Puedes cambiar la estructura de los datos sin romper la base de datos.

#### ✅ 2. Facilidad de uso
Trabaja con JSON, lo cual es muy intuitivo.

#### ✅ 3. Escalabilidad
MongoDB está diseñado para escalar horizontalmente (añadir más servidores).

#### ✅ 4. Ideal para APIs
Encaja perfectamente con aplicaciones backend modernas.

### ⚠️ Desventajas de MongoDB
#### ❌ 1. Menor control estructural
Al no tener esquema fijo, puede volverse desordenado.

#### ❌ 2. Relaciones limitadas
No es ideal para datos muy relacionados entre sí.

#### ❌ 3. Integridad de datos
En SQL es más fácil garantizar consistencia estricta.

### 🔍 Comparación directa

| Característica | SQL        | MongoDB    |
|----------------|-----------|------------|
| Estructura     | Rígida    | Flexible   |
| Datos          | Tablas    | Documentos |
| Relación       | Alta      | Baja       |
| Escalabilidad  | Vertical  | Horizontal |
| Uso            | Tradicional | Moderno  |

### ✅ ¿Cuándo usar MongoDB?
- Aplicaciones web modernas
- APIs REST
- Proyectos con datos cambiantes
- stemas que necesitan escalar rápido

### ❌ ¿Cuándo NO usar MongoDB?
- Sistemas bancarios
- Datos altamente relacionales
- Proyectos con reglas estrictas de integridad

#### 💡 Ejemplo real comparado
##### 🟦 SQL
````sql
SELECT * FROM users WHERE name = 'Ana';
````
##### 🟩 MongoDB
````javascript
db.users.find({ name: "Ana" })
````
Mongo es más cercano a cómo piensas los datos en código.

### 🧠 Analogía simple
- SQL = Excel (todo estructurado)
- MongoDB = objetos JSON (más libre)

### 🔥 Idea clave para recordar
MongoDB es NoSQL porque no usa tablas, sino documentos flexibles que pueden adaptarse fácilmente a distintos tipos de datos.

### 🧠 En una frase
MongoDB es una base de datos NoSQL que almacena información en documentos flexibles tipo JSON, permitiendo una mayor adaptabilidad frente a los sistemas tradicionales basados en tablas.

## 🔹 ¿Qué es una API?
Una API (Application Programming Interface) es un sistema que permite que diferentes aplicaciones o programas se comuniquen entre sí de forma estructurada y controlada.

### 🧠 ¿Qué significa API?
- Application Programming Interface
- Interfaz de Programación de Aplicaciones

#### 💡 Traducción simple
Una API es un intermediario que permite que dos sistemas se entiendan.

### 🧠 ¿Cómo funciona una API?
Una API actúa como puente entre:
- 👤 Cliente (frontend, app, navegador)
- 🖥️ Servidor (backend, base de datos)

#### 🔄 Flujo básico
Cliente --> API --> Servidor --> API --> Cliente

### 💻 Ejemplo real
Cuando entras en una app y ves datos:
- Tu app hace una petición a la API
- La API consulta el servidor
- Devuelve la información

### 🔥 Ejemplo práctico
````http
GET /users
````
Esto significa: “quiero obtener la lista de usuarios”

### 📥 Respuesta de la API
````json
[
  { "name": "Ana", "age": 20 },
  { "name": "Luis", "age": 25 }
]
````
### 🧠 ¿Para qué sirve una API?
Las APIs permiten:
#### ✅ 1. Obtener datos
👉 Ejemplo:
- ver usuarios
- ver productos

#### ✅ 2. Enviar información
👉 Ejemplo:
- crear cuenta
- publicar contenido

#### ✅ 3. Conectar sistemas
👉 Ejemplo:
- app --> servidor
- web --> base de datos

### 🔍 Tipos de APIs
#### 🔻 1. APIs REST
👉 Las más comunes
👉 Usan HTTP (GET, POST, etc.)

#### 🔻 2. APIs privadas
👉 Uso interno de una empresa

#### 🔻 3. APIs públicas
👉 Disponibles para desarrolladores

### 💡 Ejemplo real
- API de Instagram
- API de Google Maps
- API de Stripe

### 🔥 ¿Por qué son importantes?
Sin APIs:

❌ No podrías:
- iniciar sesión
- ver datos en apps
- conectar frontend y backend

### 💻 Ejemplo completo
#### Paso 1: Cliente pide datos
````http
GET /books
````
#### Paso 2: API procesa
Consulta base de datos

#### Paso 3: API responde
````json
[
  { "name": "Blink" },
  { "name": "Deep Work" }
]
````
### ⚠️ Errores comunes
#### ❌ Pensar que API es una base de datos
- No lo es
- Es un intermediario

#### ❌ Pensar que API tiene interfaz
- No tiene interfaz visual
- Devuelve datos

#### ❌ Confundir API con backend
- API es parte del backend

### 🧠 Analogía simple

👉 API = camarero en un restaurante
- tú (cliente) haces pedido
- el camarero (API) lo lleva
- cocina (servidor) responde
- camarero te trae la comida

### 🔥 Ventajas
- Separación de sistemas
- Reutilización
- Escalabilidad

### 🧠 En una frase
Una API es un intermediario que permite que diferentes aplicaciones se comuniquen intercambiando datos de forma estructurada.

## 🔹 ¿Qué es Postman?
Postman es una herramienta que permite probar, construir y trabajar con APIs de forma sencilla, sin necesidad de crear una aplicación completa.

### 🧠 Definición clara
Postman es un programa que te permite enviar peticiones a una API y ver las respuestas.

#### 💡 Traducción simple
Es como un “simulador” de cliente (frontend)
Pero sin tener que programar una app.

### 🧠 ¿Para qué sirve Postman?
Postman se utiliza principalmente para:
#### ✅ 1. Probar APIs
Puedes comprobar si una API funciona correctamente.

👉 Ejemplo:
- ver si devuelve datos
- comprobar errores
- validar respuestas

#### ✅ 2. Enviar peticiones HTTP
Puedes hacer:
- GET --> obtener datos
- POST --> crear datos
- PUT/PATCH --> actualizar
- DELETE --> eliminar

#### ✅ 3. Ver respuestas del servidor
Postman te muestra:
- JSON
- status code (200, 404, etc.)
- headers
- tiempo de respuesta

#### ✅ 4. Debuggear (detectar errores)
Si algo falla en tu API:

👉 Postman te ayuda a ver exactamente qué está pasando

### 🔄 ¿Cómo funciona Postman?
Flujo básico:

1. Tú configuras una petición
2. La envías
3. El servidor responde
4. Ves el resultado

#### 💻 Ejemplo práctico
##### Petición
````http
GET https://api.ejemplo.com/users
````
##### Respuesta
````json
[
  { "name": "Ana" },
  { "name": "Luis" }
]
````
👉 Todo esto lo ves directamente en Postman.

### 🧠 Partes de Postman
#### 🔻 1. URL
👉 A dónde haces la petición

#### 🔻 2. Método HTTP
👉 GET, POST, PUT, DELETE

#### 🔻 3. Headers
👉 Información adicional (ej: autenticación)

#### 🔻 4. Body
👉 Datos que envías (en POST o PUT)

#### 🔻 5. Response
👉 Lo que devuelve el servidor

### 💻 Ejemplo completo en Postman
#### Crear un usuario
````http
POST https://api.ejemplo.com/users
````
#### Body (JSON)
````json
{
  "name": "Luccia",
  "age": 23
}
````
#### Respuesta
````json
{
  "id": 1,
  "name": "Luccia",
  "age": 23
}
````
### 🔥 ¿Por qué es tan importante Postman?
Porque te permite:
- trabajar sin frontend
- probar APIs rápidamente
- detectar errores
- entender cómo funciona un backend

### ⚠️ Errores comunes
#### Pensar que Postman crea APIs
- No crea APIs
- Solo las prueba

#### Pensar que es obligatorio en producción
Es una herramienta de desarrollo

#### No usar bien los métodos HTTP
GET ≠ POST

### 🧠 Analogía simple
👉 Postman = control remoto de una API
- eliges acción
- envías comando
- ves resultado

### 🔥 Ventajas
- Fácil de usar
- Visual
- Rápido
- No necesitas frontend

### ⚠️ Desventajas
- No reemplaza una app real
- No es backend
- Solo sirve para pruebas

### ✅ ¿Cuándo usar Postman?
- Cuando estás desarrollando una API
- Cuando quieres probar endpoints
- Cuando necesitas debuggear

### ❌ ¿Cuándo NO usarlo?
- Para usuarios finales
- Para construir interfaces

### 🧠 En una frase
👉 Postman es una herramienta que permite enviar peticiones a una API y visualizar sus respuestas para probar y depurar su funcionamiento.

## 🔹 ¿Qué es el polimorfismo?
El polimorfismo es un concepto de la programación orientada a objetos (POO) que permite que diferentes objetos respondan de manera distinta al mismo método.

### 🧠 Definición clara
El polimorfismo permite usar el mismo nombre de método en diferentes clases, pero con comportamientos distintos.

#### 💡 Traducción simple
“Una misma acción, diferentes comportamientos”

### 🧠 ¿Por qué es importante?
El polimorfismo permite:
- escribir código más flexible
- reutilizar lógica
- trabajar con diferentes objetos de forma uniforme

### 🔥 Idea clave
Puedes llamar al mismo método en distintos objetos y cada uno hace algo diferente

### 💻 Ejemplo básico
````python
class Dog:
    def speak(self):
        return "Guau"

class Cat:
    def speak(self):
        return "Miau"

dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
````
#### 📌 ¿Qué está pasando aquí?
- Ambos tienen el método .speak()
- Pero cada uno devuelve algo distinto

#### 📤 Resultado
````plain text
Guau
Miau
````
### 🧠 ¿Dónde está el polimorfismo?
En que usamos el mismo método (speak) pero cada objeto responde diferente

### 🔥 Ejemplo más potente
````python
def make_sound(animal):
    print(animal.speak())

make_sound(Dog())
make_sound(Cat())
````
#### 📌 ¿Qué está pasando aquí?
- La función no sabe si es perro o gato
- Solo sabe que tiene .speak()

#### 💥 Esto es CLAVE
- No importa el tipo
- Importa el comportamiento

### 🧠 Tipos de polimorfismo
#### 🔻 1. Polimorfismo por herencia
Cuando varias clases heredan de una clase base y redefinen métodos.
##### 💻 Ejemplo
````python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Guau"
````
#### 🔻 2. Polimorfismo por duck typing
“Si camina como pato y suena como pato… es un pato”
##### 💻 Ejemplo
````python
class Car:
    def move(self):
        return "Driving"

class Person:
    def move(self):
        return "Walking"
````
Ambos tienen .move() → polimorfismo

### 🧠 ¿Para qué se usa?
#### ✅ 1. Reutilizar código
Puedes usar una misma función para diferentes objetos.

#### ✅ 2. Simplificar lógica
No necesitas hacer:
````python
if type == "dog":
````
#### ✅ 3. Crear sistemas más escalables
Puedes añadir nuevas clases sin cambiar el código existente.

### ⚠️ Errores comunes
#### ❌ Pensar que es solo herencia
No, también puede existir sin herencia

#### ❌ Confundirlo con sobrecarga de funciones
Python no tiene sobrecarga clásica como otros lenguajes

### 🧠 Analogía simple
👉 Un botón de “play”
- en Spotify → reproduce música
- en Netflix → reproduce vídeo

👉 mismo botón, distinto comportamiento

### 🔥 Ventajas
- código más limpio
- más flexible
- fácil de extender

⚠️ Desventajas
- puede ser más difícil de entender al inicio
- requiere buena organización

### 🧠 En una frase
👉 El polimorfismo es la capacidad de diferentes objetos de responder de forma distinta al mismo método.


## 🔹 ¿Qué es un método dunder en Python?
Un método dunder (también llamado método mágico) es un método especial en Python que empieza y termina con doble guion bajo.

👉 Ejemplo:
````phyton
__init__
__str__
__len__
````
### 🧠 ¿Qué significa “dunder”?
“dunder” = double underscore (doble guion bajo)

### 🧠 Definición clara
Son métodos especiales que Python usa automáticamente para definir comportamientos de los objetos.

#### 💡 Traducción simple
👉 Son funciones “internas” que le dicen a Python cómo debe comportarse un objeto.

### 🔥 Idea clave
- No los llamas tú directamente (normalmente)
- Python los ejecuta por ti automáticamente

### 💻 Ejemplo básico
````python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Luccia")
````
#### 📌 ¿Qué pasa aquí?
- Cuando haces Person("Luccia")
- Python ejecuta automáticamente:
````python
__init__
````

### 🧠 ¿Para qué sirven los dunder methods?
Sirven para:
#### ✅ 1. Inicializar objetos
````python
__init__
````
👉 Se ejecuta al crear un objeto

#### ✅ 2. Representar objetos como texto
````python
__str__
````
👉 Define qué se muestra al hacer print(objeto)

#### ✅ 3. Representación técnica
````python
__repr__
````
👉 Para debugging

#### ✅ 4. Operadores
````python
__add__
__sub__
````
👉 Permiten usar +, -, etc. con objetos

### 💻 Ejemplo importante (str)
````python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Usuario: {self.name}"

u = User("Luccia")
print(u)
````
📤 Resultado
````plain text
Usuario: Luccia
````
### 🧠 Sin str
Saldría algo feo tipo:
```` plain text
<__main__.User object at 0x...>
````
### 💻 Ejemplo (len)
````python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

lista = MyList([1, 2, 3])
print(len(lista))
````
#### 📌 ¿Qué pasa aquí?
len(lista) llama automáticamente a:
````python
__len__()
````
### 🔥 Ejemplo (add)
````python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(5)
n2 = Number(3)

print(n1 + n2)
````
#### 📌 ¿Qué está pasando?
👉 n1 + n2 llama a:
````python
__add__(n1, n2)
````
### 🧠 ¿Por qué son tan importantes?
Porque permiten que tus clases:
- se comporten como tipos nativos
- sean más intuitivas
- integren con Python de forma natural

### ⚠️ Errores comunes
#### ❌ Pensar que son opcionales sin importancia
Son clave para hacer código profesional

#### ❌ Intentar llamarlos directamente
No se usan así:
````python
obj.__str__()
````
👉 Se usan a través de Python:
````python
print(obj)
````
#### ❌ No entender cuándo se ejecutan
Se ejecutan automáticamente en momentos específicos

### 🧠 Analogía simple
Son como “reglas ocultas” que definen cómo funciona un objeto

### 🔥 Ejemplo mental

👉 + en números --> suma

👉 + en tus clases --> tú decides qué hace

### 🧠 En una frase
Los métodos dunder son métodos especiales que Python usa automáticamente para definir el comportamiento de los objetos.

## 🔹 ¿Qué es un decorador de Python?
Un decorador en Python es una herramienta que permite modificar o extender el comportamiento de una función o método sin cambiar su código original.

### 🧠 Definición clara
Un decorador es una función que envuelve otra función para añadirle funcionalidad extra.
#### 💡 Traducción simple
Es como “ponerle algo encima” a una función para que haga más cosas.

### 🔥 Idea clave
- No cambias la función
- La “envuelves” y le añades comportamiento

### 🧠 ¿Por qué se usan?
Los decoradores permiten:
- reutilizar código
- evitar repetir lógica
- mantener el código limpio
- añadir funcionalidades sin modificar lo original

### 💻 Ejemplo básico
````python
def my_decorator(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper
````
#### 📌 ¿Qué hace esto?
- my_decorator recibe una función
- crea una nueva función (wrapper)
- ejecuta cosas antes y después

### 💻 Aplicando el decorador
````python
@my_decorator
def say_hello():
    print("Hola")

say_hello()
````
📤 Resultado
````plain text
Antes de ejecutar la función
Hola
Después de ejecutar la función
```` 
#### 📌 ¿Qué pasó aquí realmente?
👉 @my_decorator es equivalente a:
````python
say_hello = my_decorator(say_hello)
````
#### 💥 CLAVE
El decorador reemplaza la función original por una versión modificada

### 🧠 Estructura de un decorador
````python
def decorador(func):
    def wrapper():
        # código antes
        func()
        # código después
    return wrapper
````
### 🔥 Decoradores con argumentos
````python
def decorator(func):
    def wrapper(name):
        print("Hola antes")
        func(name)
        print("Adiós después")
    return wrapper

@decorator
def greet(name):
    print(f"Hola {name}")

greet("Luccia")
````
### 🧠 Decoradores reales en Python
#### 🔻 @property
👉 Convierte un método en atribut
````python
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
````
#### 🔻 @staticmethod
👉 Método sin acceso a self

#### 🔻 @classmethod
👉 Trabaja con la clase en lugar de la instancia

### 🧠 ¿Para qué se usan en la vida real?
#### ✅ Logging
Registrar acciones

#### ✅ Autenticación
Verificar usuarios

#### ✅ Validación
Comprobar datos

#### ✅ Control de acceso
Permisos

### 💻 Ejemplo real (login)
````python
def require_login(func):
    def wrapper():
        print("Verificando usuario...")
        func()
    return wrapper

@require_login
def dashboard():
    print("Bienvenido al panel")

dashboard()
````
### 🧠 ¿Por qué son tan importantes?
Porque permiten:
- código limpio
- separación de responsabilidades
- reutilización avanzada

### ⚠️ Errores comunes
#### ❌ Pensar que modifican la función directamente
- No la modifican
- La envuelven

#### ❌ No entender el wrapper
El wrapper es la clave del decorador

#### ❌ Olvidar devolver la función
Sin return wrapper no funciona

### 🧠 Analogía simple
👉 Decorador = filtro de Instagram 📸

- la foto es la función
- el filtro añade efectos
- la foto sigue siendo la misma

### 🔥 Ventajas
- reutilización
- limpieza de código
- modularidad
- flexibilidad

### ⚠️ Desventajas
- puede ser difícil al principio
- puede complicar la lectura si se abusa

### 🧠 En una frase
Un decorador es una función que envuelve otra función para añadirle comportamiento sin modificar su código original.
