# Motor de Validación para Banco Digital

## Descripción General

Este proyecto implementa un motor de validación de transacciones basado en reglas de negocio para un entorno de banca digital.

La solución incluye:

- Motor de validación de reglas de negocio
- Procesamiento batch de transacciones
- Análisis exploratorio de datos (EDA)
- Queries SQL para reporting
- Suite de pruebas unitarias

---

## Decisiones de Arquitectura

- El motor de validación sigue el patrón Chain of Responsibility para permitir una evaluación modular y extensible de reglas.
- Cada regla de negocio fue implementada como una clase independiente para mejorar mantenibilidad y testabilidad.
- Los valores de configuración como límites, monedas permitidas y países de alto riesgo fueron externalizados en un módulo centralizado de configuración.
- Se seleccionó Pandas para el procesamiento batch debido a su simplicidad y fuerte soporte para transformaciones tabulares.

---

## Trade-offs Considerados

- Se prefirió procesamiento secuencial sobre multiprocessing para priorizar legibilidad y facilidad de debugging.
- La solución prioriza mantenibilidad y claridad sobre optimización prematura.
- La evaluación de reglas realiza cortocircuito únicamente en violaciones CRÍTICAS, siguiendo los requerimientos del negocio.

---

## Estructura del Proyecto

```text
config/        -> Configuración externa
rules/         -> Reglas de validación de negocio
validator/     -> Motor principal de validación
tests/         -> Pruebas unitarias
data/          -> Datasets de entrada y salida
analysis.ipynb -> Notebook de análisis exploratorio
queries.sql    -> Queries SQL de reporting
```

---

## Instalación

```bash
pip install -r requirements.txt
```

---

## Ejecutar Motor de Validación

```bash
python main.py
```

---

## Ejecutar Procesamiento Batch

```bash
python batch_processor.py
```

---

## Ejecutar Pruebas Unitarias

```bash
pytest
```

---

## Abrir Notebook de Análisis Exploratorio

```bash
jupyter notebook
```

Luego abrir:

```text
analysis.ipynb
```

---

## Dataset

El dataset original `transactions.csv` se encuentra en:

```text
data/transactions.csv
```

El resultado generado por el batch processor se exporta en:

```text
data/validation_results.csv
```

---

## Tecnologías Utilizadas

- Python
- Pandas
- Pytest
- Jupyter Notebook
- SQL
- Matplotlib / Seaborn