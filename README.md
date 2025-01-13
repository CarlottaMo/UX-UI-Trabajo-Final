# UX-UI-Trabajo-Final


# MyFirstAddon

## Descripción
**MyFirstAddon** es un Addon para Blender que contiene una colección de operadores útiles para artistas 3D. Con este complemento, los usuarios pueden realizar varias operaciones, como mover el origen de un objeto al origen mundial, rotar y escalar objetos, calcular distancias y copiar objetos.

### Funciones:
- **Mover origen al origen mundial**: Establece el origen del objeto activo en el origen mundial (0,0,0). (mesh.move_origin_to_world)
- **Calcular distancia**: Calcula la distancia entre el cursor 3D y el origen mundial. Mover el cursor a algun lado en el espacio y presiona calcular distancia (object.calcular_distancia)
- **Rotar objetos**: Permite rotar un objeto en un ángulo especificado. Selecciona un objeto y introducce el angulo. Presiona Ángulo de Rotación (object.rotar_objeto)
- **Escalar objetos**: Cambia la escala de un objeto con un factor especificado. Seleciona un objeto y introducce el factor de escala. Presiona Ajustar Escala (object.ajustar_escala_uniformemente)
- **Copiar y distribuir objetos**: Crea varias copias de un objeto y las distribuye a una distancia determinada. Seleciona un objeto y introducce el número de copias y la distancia al objeto original. Presiona Copiar y Distribuir (object.copiar_y_distribuir)
- **Aplicar material**: Aplica un material personalizado a los objetos seleccionados. Selecciona un objeto, asígnale un material y ajusta sus propiedades. Da un nombre al material. Luego, selecciona otro(s) objeto(s) e introduce el nombre del material. Presiona Aplicar Material Predeterminado (object.aplicar_material_predeterminado)

## Instalación
1. Descarga el complemento y guarda el archivo en tu computadora.
2. Abre Blender y ve a `Editar > Preferencias > Addons > Instalar`.
3. Selecciona el archivo descargado y haz clic en `Instalar complemento`.
4. Activa el complemento marcando la casilla junto al nombre del complemento.

## Uso
- Una vez activado el Addon, encontrarás una nueva pestaña en la vista 3D llamada "Herramientas Artista 3D".
- Puedes acceder a los diferentes operadores desde el panel o el menú radial (Pie Menú).

## Atajos de teclado
- **Ctrl + Shift + Q**: Abre el pie menu de herramientas.

## Objetivos de los operadores:
SMART - Specific, Measurable, Achievable, Relevant, Time-bound
- **Mover origen al origen mundial**: 
Podría ser útil para proyectos de interiorismo. Es útil para alinear objetos con el espacio central de la escena, o para realizar transformaciones de manera precisa antes de hacer ajustes en la geometría.
- **Calcular distancia**: Podría ser útil para planes de arquitectura/para ingenieros civiles o también en videojuegos, para medir la distancia entre un personaje y un objeto u otra persona.
- **Rotar objetos:** Este operador es necesario en escenas de animación o videoclips, donde los objetos deben rotar o estar orientados de una forma específica según el storyboard o la dirección artística de la escena, p. ej. para un storyboard digital de una película.
- **Escalar objetos**: Se usa cuando las proporciones del objeto deben mantenerse constantes. Por ejemplo, para un collage o un póster, tiene muchos casos de uso.
- **Copiar y distribuir objetos**: En general, para crear objetos que ocurren varias veces, como crear los peones en un juego de ajedrez o árboles para el escenario de un videojuego.
- **Aplicar material**: Es ideal para asignar un material inicial a varios objetos rápidamente, sin tener que hacerlo manualmente para cada uno, se puede usar en muchos campos de trabajo, como interiorismo, videojuegos, en general proyectos 3D.
- **SMART**
- **Specific**: Los objetivos de los operadores en los proyectos son específicos.
- **Measurable**: Se puede medir fácilmente.
- **Achievable**: Se puede lograr fácilmente, además se pueden usar las explicaciones en este Readme.
- **Relevant**: Cada una de las operaciones puede ser muy relevante para un proyecto específico.
- **Time-Bound**: Depende del contexto específico del proyecto concreto, si se pone un límite de tiempo, pero la operación en sí no necesita mucho tiempo.


## Decisiones de diseño
- He seleccionado el orden de los operadores en función de la frecuencia probable, empezando por el más frecuente.
- He seleccionado un Icon para cada uno, que me parecía el más adecuado.
- Siempre he dejado espacios del mismo tamaño entre los operadores diferentes y proimidad entre los campos de entrada de un operador, para que sea fácilmente visible cuál campo de entrada pertenece a cuál acción.
- He usado el mismo formato para todos, para que haya consistencia y simmetria en el diseño.
- Primero viene el título (en mayúsculas), después, si existe, el campo de entrada y al final siempre el botón/campo de acción con el icono adecuado.
- He usado texto en combinación con iconos, para que se aumente la usabilidad.
- He usado suficiente texto para que se entienda, pero no demasiado, para que no sea una sobrecarga de información y para que los operadores se puedan encontrar fácilmente y de forma rápida.

## Autor
**Carlotta Monath**

## Versión
0.0.1

## Versión de Blender
4.2.1
