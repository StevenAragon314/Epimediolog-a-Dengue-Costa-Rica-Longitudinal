# Sistema de Vigilancia Epidemiológica del Dengue: Desarrollo de Indicadores (2020-2026) en Costa Rica

Este repositorio contiene la arquitectura de datos, el pipeline de procesamiento y el marco metodológico para el cálculo, monitoreo y evaluación de indicadores epidemiológicos y operacionales de Dengue a nivel cantonal y semanal. 

A diferencia de los enfoques predictivos tradicionales, este proyecto se centra en el **desarrollo de indicadores estandarizados** y en la asignación automatizada de **clases de análisis** para optimizar la toma de decisiones en salud pública y evaluar el impacto de las intervenciones a partir de los registros asignados.

Proyecto desarrollado para la Escuela de Estadística, de la Universidad de Costa Rica 🌻.

---

Aclaratoria: Los datos utilizados para este análisis no están de uso libre, en caso de requerir dicha información, se recomienda contactar a: 

 + MARIANNE ALESANDRA PEÑA WUST
 + Contacto: marianne.pena@ucr.ac.cr

---

## 📋 Marco Metodológico y Clasificación de Indicadores

Para articular el análisis de manera estructurada, cada indicador propuesto ha sido asignado a una **Clase** específica (de las 5 clases que componen el ciclo de gestión y análisis epidemiológico). A continuación, se detallan los indicadores, su clasificación y la ecuación matemática para su cálculo formal:

### 1. Tasa de Incidencia (Clase: Efecto)
Mide la velocidad de propagación de la enfermedad en una población y periodo específicos, expresada por cada $100,000$ habitantes.
* **Ecuación:**
  $$\text{Tasa de Incidencia} = \left( \frac{\text{Casos Nuevos de Dengue en la Semana } w}{\text{Población Total en el Cantón } c} \right) \times 100,000$$

### 2. Cambio Porcentual y Número de Casos por Cantón (Clase: Proceso)
Monitorea la dinámica y tendencia de la transmisión de una semana epidemiológica a otra para clasificar el ritmo de aceleración o desaceleración del brote.

* **Ecuación:**
  
$$\Delta\% = \left( \frac{\text{Casos en la Semana } w - \text{Casos en la Semana } w-1}{\text{Casos en la Semana } w-1} \right) \times 100$$

### 3. Tasa de Efectividad de las Campañas a Largo Plazo (Clase: Impacto)
Evalúa de manera retrospectiva el comportamiento de la curva epidemiológica post-intervención, analizando el periodo específico desde **Enero 2024 hasta Diciembre 2025**.
* **Ecuación:**

  $$\text{Efectividad } (\%) = \left( \frac{\text{Casos Medios Pre-Campaña} - \text{Casos Medios Post-Campaña}}{\text{Casos Medios Pre-Campaña}} \right) \times 100$$

### 4. Tasa de Ataque Acumulado (Clase: Efecto)
Establece la proporción de la población que ha sido afectada por el Dengue acumulativamente a lo largo del periodo longitudinal completo (2020-2026).
* **Ecuación:**
  $$\text{Tasa de Ataque Acumulado} = \left( \frac{\sum_{t=2020}^{2026} \text{Total de Casos Confirmados en Cantón } c}{\text{Población Expuesta en Cantón } c} \right) \times 100$$

### 5. Distribución de Campañas por Cantón (Clase: Producto)
Cuantifica la cobertura espacial y la frecuencia de los esfuerzos logísticos y de prevención desplegados por los equipos de salud.
* **Ecuación:**
  $$\text{Distribución de Campañas} = \left( \frac{\text{Número de Campañas Ejecutadas en Cantón } c}{\text{Total de Campañas Ejecutadas a Nivel Nacional}} \right) \times 100$$

### 6. Número de Viviendas Inspeccionadas en las Campañas (Clase: Producto)
Indicador directo de rendimiento operacional que mide el alcance físico del control vectorial (fumigación y eliminación de criaderos) dentro de las zonas de riesgo.
* **Ecuación:**
  $$\text{Cobertura de Inspección} = \left( \frac{\text{Viviendas Inspeccionadas/Fumigadas en Cantón } c}{\text{Total de Viviendas Registradas en Cartografía}} \right) \times 100$$

---

## 📂 Estructura del Repositorio

El repositorio se organiza bajo el estándar de proyectos de ciencia de datos, enfocado en el procesamiento de registros asignados y tracking de indicadores:

```text
├── .gitignore               # Exclusión de entornos, cachés y datos locales
├── README.md                # Descripción general y marco metodológico (este archivo)
├── data/                    # Almacenamiento local de datos (No trackeado en Git)
│   ├── raw/                 # Registros asignados de casos y reportes de campañas en bruto
│   └── processed/           # Dataframes consolidados con los indicadores calculados
├── src/                     # Código fuente modular
│   ├── __init__.py
│   ├── indicators.py        # Scripts con las funciones matemáticas y lógica de cálculo
|   ├── constants.py         # Variabes constanstes utilizadas en el procesamiento de datos
│   └── class_assigner.py    # Módulo de asignación automatizada de las 5 clases
└── notebooks/               # Jupyter Notebooks para análisis exploratorio y validación
```
