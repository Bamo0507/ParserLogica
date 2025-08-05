# Proyecto 1 - Logica Matematica

## Descripción

Este proyecto implementa un lexer y parser para fórmulas de lógica proposicional simples utilizando PLY (Python Lex-Yacc) y genera visualizaciones gráficas de su árbol sintáctico con Graphviz. A partir de un archivo de texto con fórmulas, el programa reconoce tokens, construye la representación interna y produce un PNG por cada AST.

## Características

- Tokenización de variables (p–z), constantes (0,1) y operadores lógicos (~, ^, o, =>, <=>).
- Soporte para paréntesis y orden de precedencia.
- Visualización automática del árbol sintáctico.
- Procesamiento de distintas expresiones que se encuentran en `Pruebas.txt`.

## Requisitos e Instalación

Para instalar las dependencias necesarias:
```bash
pip install ply graphviz
```

## Contenido de `Pruebas.txt`

```
p
~~~q
(p^q)
(0=>(ros))
~(p^q)
(p<=>~p)
((p=>q)^p)
(~(p^(qor))os)
```

## Uso

Ejecuta el script principal para analizar las fórmulas y generar los árboles sintácticos:

```bash
python main.py
```

Los archivos resultantes `arbol_0.png`, `arbol_1.png`, … se guardarán en el directorio actual, es decir, en el que se ejecute el programa.