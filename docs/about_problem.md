Llega febrero, y el mundo se viste del color del amor. Los pájaros cantan, los bombones desaparecen de las estanterías de los supermercados, y en las radios suena *Rosas* de La Oreja de Van Gogh como si de un himno se tratase. Se acerca San Valentín, otro año más, y tú, Alex, lo volverás a pasar sin pareja. A no ser que...

Te detienes ante una valla publicitaria en tu camino a casa. Sus grandes luces de neón te deslumbran, pero el texto allí impreso te sorprende aún más:

> **:heart:4u2:heart:** ¿Quieres encontrar el amor? ¡Encontramos a tu otra mitad mediante el poder de la meta-heurística!

¿Otra aplicación de citas? Seguro que es como las otras cincuenta que ya has probado. Pero... ¿Y si esta es la buena? Sueltas un pequeño suspiro, y procedes a descargar **:heart:4u2:heart:** en tu teléfono móvil.

> ¡Bienvenid@ a **:heart:4u2:heart:**! ¡La aplicación que te permite ordenar a tus futuras medias naranjas en función de tus preferencias!

> A continuación, se te mostrará una serie de **100** posibles candidat@s especificamente seleccionad@s para ti. Sabemos que decidirse entre tantas personas a la vez puede ser complicado, por lo que tan solo te pediremos que nos digas qué opción prefieres de entre cada par de candidat@s. Fácil, ¿Verdad?

> Una vez nos hayas indicado tus preferencias para... Los **4.950** pares posibles, ejem, tan solo deberás confirmar tu solicitud y nosotros nos encargaremos de ordenar todas las opciones mediante algoritmos meta-heurísticos. Después, podrás comenzar a chatear con l@s candidat@s que hayan quedado más arriba en el ranking de tu corazón. ¿A qué esperas? :revolving_hearts: ¡Únete a la búsqueda del amor! :revolving_hearts:

Bueno, la esperanza es lo último que se pierde. Veamos que tal funciona esto de la meta-heurística...

### Descripción del problema

Tu nuevo trabajo en **:heart:4u2:heart:** comienza fuerte. ¡Un usuari@ ya ha mandado su solicitud, y tú aún no has implementado el algoritmo que le ayudará a encontrar a su futuro amor! Por suerte, la versión gratuita de la aplicación notifica los resultados con **2 horas y media** de retraso. Por lo que ese es, precisamente, el tiempo que tienes para arreglar este desaguisado.

Los datos con los que puedes trabajar están reflejados en el archivo *preferences.dat*. El formato es sencillo, se trata de una matriz de tamaño $100\times 100$ con números enteros que van del $0$ al $100$. El valor situado en la fila $i$ columna $j$ nos indicará el porcentaje de preferencia otorgado por el usuari@ al candidat@ $i$ sobre el candidat@ $j$. Por definición, la suma de la preferencia de $i$ sobre $j$ y la preferencia de $j$ sobre $i$ debe de ser $100$. Además, lo valores en la diagonal principal (fila $i$ columna $i$) serán todos $0$, y no se utilizarán durante la resolución del problema.

> **Ejemplo**
>
> $
> \begin{array}{c|ccc}
> & \text{Pablo} & \text{Juan} & \text{Maria} \\ \hline
> \text{Pablo} & 0   & 50  & 0 \\
> \text{Juan}  & 50  & 0   & 60 \\
> \text{Maria} & 100 & 40  & 0
> \end{array}
> $
>
> En el anterior ejemplo, la preferencia del usuari@ entre **Pablo** y **Juan** es 50%-50%. Es decir, puestos uno al lado del otro, al usuari@ le es complicado decidir quién podría ser un mejor candidato para una relación. Si comparamos a **Pablo** y **María**, sin embargo, la ganadora es claramente **María**, con un 100% de preferencia por parte del usuari@. Uno esperaría que al comparar a **Juan** y **María**, el resultado sería similar, pero curiosamente esto no es así: la preferencia del usuari@ en este caso es un ajustado 60%-40% a favor **Juan**. Esto es, precisamente, lo que hace difícil a este problema: la atracción no cumple la propiedad transitiva, por lo que encontrar el ranking idóneo entre todas las posibles opciones no es algo fácil.

Perfecto, ya tienes todos los datos necesarios, y estas en condiciones de ponerte a trabajar. Tu objetivo será encontrar la ordenación de los candidatos que se ajuste lo máximo posible a los gustos del usuari@. Pero... ¿Cómo puedes cuantificar como de *buena* es tu solución? Seguramente tendrás tus propias ideas y sugerencias, pero las directrices de **:heart:4u2:heart:** son claras: la calidad de una solución se mide sumando los porcentajes de las preferencias del usuario que son respetadas. En otras palabras, si en tu ordenación el candidat@ $i$ aparece sobre el candidat@ $j$, sumarás a tu función objetivo el valor asociado a la preferencia de $i$ sobre $j$ en la matriz del problema. Fácil, ¿No? Ahora solo queda repetir este proceso para todo par de candidat@s posible, y sumar los valores obtenidos. Al final de este proceso, obtendras un valor que servirá como indicador de la calidad de tu solución. Cuanto más alto sea este valor, mejor habrás hecho tu trabajo, ¡Y mayores probabilidades tendrá Alex de encontrar a su pareja ideal!

> **Ejemplo**
>
> Volviendo al ejemplo anterior, ¿Cuál sería la calidad de la ordenación $(Maria,Juan,Pablo)$? Comprobemos qué preferencias se cumplen y cuanto aporta cada una a la calidad de la solución:
> 
> $Maria>Juan\rightarrow$ La preferencia de Maria sobre Juan es del $40\%$.
>
> $Maria>Pablo\rightarrow$ La preferencia de Maria sobre Pablo es del $100\%$.
>
> $Juan>Pablo\rightarrow$ La preferencia de Juan sobre Pablo es del $50\%$.
>
> Por lo tanto, si sumamos todas las preferencias respetadas por nuestra solución, obtendremos un valor de función objetivo de $40+100+50=190$.
