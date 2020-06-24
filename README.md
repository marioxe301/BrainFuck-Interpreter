# BrainFuck-Interpreter
Un interpretador del lenguaje de programación esotérico "Brainfuck" elaborado con Python

# Comandos de BrainFuck
| Operador |                                                   Descripcion                                                  |
|:--------:|:--------------------------------------------------------------------------------------------------------------:|
|     +    |                              Suma 1 unidad en el elemento donde apunta el puntero                              |
|     -    |                              Resta 1 unidad en el elemento donde apunta el puntero                             |
|     >    |                                     Mueve el puntero a la derecha 1 unidad                                     |
|     <    |                                    Mueve el puntero a la izquierda 1 unindad                                   |
|     .    |               Imprimer el caracter ASCII basado en el valor de la celda la cual apunta el puntero              |
|     ,    | Permite input de un caracter ( su valor sera guardad con su codigo ASCII ) y lo guarda donde apunta el puntero |
|     [    |                                                Comienzo del loop                                               |
|     ]    |    Final del loop ( salta a inicio del loop si y solo si el valor donde apunta el puntero es distinto de 0 )   |

# Como funciona BrainFuck
Es un lenguaje basado en un Vector de "N" tamaño ( [0,0,0,0] ) cada elemento del vector es su valor inicial es 0 y el puntero apunta al primer elemento( Nota: El maximo valor de cada celda es 255 es decir (2^8)-1 ). Si ejecutamos un **+** nuestro vector quedaria ( [1,0,0,0] ) ya que el puntero esta en el primer elemento a menos que ejecutemos **>** y luego **+** y nuestro vector quedaria ( [1,1,0,0] ) ya que movimos 1 unidad a la derecha nuestro puntero y ahora apunta al valor de la siguiente celda. Y para comentar se puede usar cualquier caracter a excepcion de los reservados para el lenguaje

# Dependecias usadas
* python 3 y pip3
* pyparsing ( Libreria )

# Ejecutar Codigo de BF
## Clonar el repo
> git clone https://github.com/marioxe301/BrainFuck-Interpreter.git
## Instalar dependencias
> pip3 install -r requirements.txt
## Ejecutar
> python3 main.py <-nombre del archivo->

# Observaciones Extras
Hay que tener cuidado al momento de manejar el puntero ( por eso es importante comentar ) ya que si se realiza un **<** estando el puntero en la primera poscicion no va pasar nada porque no se puede mover a esa direccion. Tambien al momento de usar **-** no va ocurrir nada si el valor de la celda donde apunta es 0 y viceversa usando **+** ya que el numero maximo en cada celda es (2^8)-1
