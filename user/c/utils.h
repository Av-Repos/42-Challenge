#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1024

typedef struct {
    int size;
    int ** mat;
} Instance;

/***
Función que lee la instancia en el fichero indicado.
Input:
    - path: Ruta al fichero con la instancia del problema.
Output:
    Estructura que alberga la instancia. Contiene los siguientes datos:
        - size: Tamaño del problema.
        - mat: Matriz de preferencias del problema.
***/
Instance readInstance(const char* path){
    int i, j;
    Instance ins = {.size = -1, .mat = NULL};
    FILE *fp = fopen(path, "r");
    
    // Abre el fichero con la instancia
    if (!fp) {
        perror("fopen");
        return ins;
    }

    char line[MAX_LINE];

    // Guarda el tamaño del problema
    fgets(line, sizeof(line), fp);
    ins.size = atoi(line);

    // Inicializa la matriz de preferencias
    ins.mat = (int **) malloc(ins.size*sizeof(int *));
    for(i = 0; i < ins.size; i++){
        ins.mat[i] = (int *) malloc(ins.size*sizeof(int));
    }


    // Lee la instancia, fila por fila
    i = 0;
    while (fgets(line, sizeof(line), fp)) {
        char *start = line;
        char *comma;

        // Guarda los valores correspondientes a la fila actual
        j = 0;
        while ((comma = strchr(start, ',')) != NULL) {
            *comma = '\0';
            ins.mat[i][j] = atoi(start);
            start = comma + 1;
            j++;
        }

        ins.mat[i][j] = atoi(start);
        i++;
    }

    fclose(fp);
    return ins;
}

/***
Función que genera una solución aleatoria al problema.
Input: 
    - size: Tamaño del problema.
Output:
    Ordenación aleatoria de size números del 0 a size-1, sin duplicados.
***/
int * randomSolution(int size){
    int i, j, temp;
    int * solution = (int *) malloc(size*sizeof(int));

    // Inicializa la solución
    for(i = 0; i < size; i++) solution[i] = i;
    
    // Reordena aleatoriamente la solución utilizando el algoritmo Fisher-Yates
    for(i = size-1; i >= 1; i--){
        j = rand() % (i+1);
        temp = solution[i];
        solution[i] = solution[j];
        solution[j] = temp;
    }

    return(solution);
}

/***
Función que comprueba si la solución indicada es una solución válida para el problema.
Input:
    - solution: Solución a validar.
    - size: Tamaño del problema.
Output:
    1 si se trata de una solución válida, y 0 en caso contrario.
***/
int checkSolution(int * solution, int size){
    int i;
    int *seen;

    // Inicializa la lista de visitados
    seen = (int *) malloc(size*sizeof(int));
    for(i = 0; i < size; i++) seen[i] = 0;

    // Comprueba que no haya valores no válidos o duplicados en la solución
    for(i = 0; i < size; i++){
        if(solution[i] >= size || solution[i] < 0){
            fprintf(stderr,"La solución debe contener los números del 0 al %d, sin duplicados.", size-1);
            return(0);
        }
        seen[solution[i]]++;
        if(seen[solution[i]]>1){
            fprintf(stderr,"La solución debe contener los números del 0 al %d, sin duplicados.", size-1);
            return(0);
        }
    }

    return(1);
}

#endif