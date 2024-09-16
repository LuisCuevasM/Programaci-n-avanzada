# Preguntas teóricas

## 1. ¿Qué es un paradigma de programación?
Un **paradigma de programación** es un enfoque conceptual que guía cómo se estructuran y desarrollan soluciones a problemas usando un lenguaje de programación. Define principios y prácticas para escribir código, organizando tanto los datos como las operaciones. Algunos paradigmas comunes incluyen:

- **Programación orientada a objetos (OOP)**: Se basa en la organización de datos y comportamientos en objetos.
- **Programación funcional**: Enfatiza el uso de funciones puras y evita el estado mutable.
- **Programación procedural**: Estructura el código mediante procedimientos o funciones.
  
Cada paradigma tiene su propia filosofía y conjunto de reglas que determinan cómo resolver problemas de manera eficiente y mantenible.

## 2. ¿En qué se basa la programación orientada a objetos?
La **programación orientada a objetos (OOP)** se centra en la creación de **objetos** que representan entidades del mundo real o conceptos abstractos. Estos objetos agrupan **datos** (atributos) y **comportamientos** (métodos) dentro de una misma unidad. El concepto clave es que los objetos interactúan entre sí para lograr el comportamiento del programa.

La OOP se sustenta en cuatro pilares principales:

- **Encapsulamiento**: Agrupar datos y métodos que operan sobre esos datos dentro de un objeto, restringiendo el acceso externo.
- **Herencia**: Permite que una clase herede propiedades y métodos de otra, fomentando la reutilización de código.
- **Polimorfismo**: La capacidad de diferentes clases de responder a la misma interfaz de manera distinta.
- **Abstracción**: Esconder detalles internos de la implementación y exponer solo lo esencial.

## 3. ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación Big O?
La **recursividad** ocurre cuando una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más pequeños. La **iteración**, en cambio, utiliza bucles (como `for` o `while`) para repetir un conjunto de instrucciones hasta cumplir una condición.

Ambas técnicas se pueden comparar en términos de **complejidad algorítmica** (expresada en notación **Big O**). Aunque pueden resolver el mismo problema, la recursividad a menudo consume más memoria, ya que cada llamada recursiva se almacena en la pila de ejecución. En cambio, la iteración utiliza un espacio constante de memoria.

Por ejemplo:
- Un algoritmo recursivo que divide un problema en dos subproblemas tiene una complejidad \( O(2^n) \) si no reduce significativamente el tamaño en cada llamada.
- Un algoritmo iterativo puede tener \( O(n) \) si solo requiere recorrer todos los elementos una vez.

## 4. Explicar la diferencia de rendimiento entre \( O(1) \) y \( O(n) \)
- \( O(1) \) (constante): Indica que el tiempo de ejecución es **constante** y no depende del tamaño de la entrada. Por ejemplo, acceder a un elemento específico de un array tiene complejidad \( O(1) \), ya que siempre toma el mismo tiempo, sin importar cuántos elementos tenga el array.
  
- \( O(n) \) (lineal): Indica que el tiempo de ejecución **crece linealmente** con respecto al tamaño de la entrada. Por ejemplo, recorrer todos los elementos de una lista uno por uno tiene una complejidad \( O(n) \), porque el tiempo requerido aumenta proporcionalmente al número de elementos.

En términos de rendimiento, un algoritmo \( O(1) \) es siempre más eficiente que uno \( O(n) \), especialmente cuando trabajamos con grandes volúmenes de datos.

## 5. ¿Cómo se calcula el orden en un programa que funciona por etapas?
Cuando un programa se ejecuta en varias **etapas**, el cálculo de la **complejidad total** depende de cómo se combinan estas etapas:

- **Etapas secuenciales**: Si un programa tiene varias operaciones que se ejecutan una tras otra, se toma en cuenta la **complejidad más alta** entre ellas. Por ejemplo, si una etapa tiene una complejidad \( O(n) \) y otra \( O(n^2) \), el orden total será \( O(n^2) \).
  
- **Etapas anidadas**: Si una etapa se repite dentro de otra (como en un bucle dentro de otro bucle), las complejidades se **multiplican**. Por ejemplo, un bucle que recorre \( n \) elementos dentro de otro bucle similar tiene una complejidad de \( O(n^2) \).

Este análisis permite entender el impacto de cada parte del programa en el tiempo de ejecución total.

## 6. ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?
Para calcular la **complejidad temporal** de un algoritmo recursivo, se usa una **relación de recurrencia** que describe el tiempo de ejecución en función del tamaño del problema. Esta relación se puede resolver usando técnicas como:

- **El teorema maestro**: Proporciona una forma de resolver muchas ecuaciones de recurrencia que surgen en algoritmos recursivos.
  
- **Desenrollado de la recursión**: Se expande la recursión para encontrar un patrón y determinar la complejidad.

Por ejemplo, en un algoritmo de búsqueda binaria, la relación de recurrencia es \( T(n) = T(n/2) + O(1) \), lo que resulta en una complejidad \( O(\log n) \), ya que en cada paso el problema se reduce a la mitad.
