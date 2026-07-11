# employee-onboarding-assistant
Employee Onboarding Assistant es un copiloto que acompaña a empleados nuevos en sus primeros días — responde dudas con documentación interna, genera checklists y sabe cuándo derivar a "People" o "IT".

# Estructura de proyecto propuesta
```text
employee-onboarding-assistant/
├── data/                          # Fichero JSON con los datos.
├── model/                         # Carpeta donde se encuentran los procesos relacionados con la carga de datos.
│   ├── data_model.py              # Carga el modelo de datos, sea el que sea.
│   └── objects/                   # Carpeta donde guardamos los objetos del modelo de datos.
│       ├── docs.py                # Objeto que contiene data\onboarding_docs.json.
│       ├── empleados.py           # Objeto que contiene data\empleados_demo.json.
│       ├── empresa.py             # Objeto que contiene data\empresa.json.
│       └── faqs.py                # Objeto que contiene data\faq_onboarding.json.
├── llm/                           # Carpeta donde se encuentran los procesos relacionados con LLM.
│   ├── context_delimiter.py       # Selección de docs/FAQ relevantes para delimitar el contexto.
│   ├── prompt_builder.py          # Construcción dinámica de prompts.
│   ├── user_history.py            # Perfil empleado + historial.
│   ├── llm_orchestrator.py        # Intermediario: Se encarga de configurar API si hace falta y llamar al LLM de turno.
│   ├── gemini/
│   │   ├── gemini_auth.py         # Carga de API key de gemini
│   │   ├── gemini_client.py       # Llamadas al LLM de gemini
├── core/                          # Carpeta donde guardamos los ficheros de la capa de negocio
│   ├── orchestrator.py            # Orquestación (turnos, checklist, modos)
│   └── validators.py              # Validación y dominio acotado
├── common/                        # Carpeta de componentes generales
│   ├── config.py                   # Se definen los valores de losp parametros que depende el comportamiento del sistema.
│   └── utils.py                   # Funciones genéricas auxiliares y reutilizables
├── benchmark/                     # Carpeta de reports/benchmark
│   └── benchmark.py               # Parte 4 — ejecución del benchmark y export a output/
├── entregables/                   # Conclusiones finales
│   ├── matriz_decision.md
│   ├── recomendacion.md
│   └── rubrica_benchmark.md
├── output/                        # Resultados de benchmark
├── main.py                        # Punto de entrada de la aplicación
├── .gitignore                     # Ignora .venv/ y cosas del sistema
├── README.md                      # Documentación principal
└── requirements.txt               # Librerías de Python
```
