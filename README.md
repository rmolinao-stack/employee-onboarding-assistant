# employee-onboarding-assistant
Employee Onboarding Assistant es un copiloto que acompaña a empleados nuevos en sus primeros días — responde dudas con documentación interna, genera checklists y sabe cuándo derivar a "People" o "IT".

## Estructura de proyecto
```text
employee-onboarding-assistant/
├── data/                           # Fichero JSON con los datos.
├── model/                          # Carpeta donde se encuentran los procesos relacionados con la carga de datos.
│   ├── data_model.py               # Carga el modelo de datos, sea el que sea.
|   ├── dataclasses/                # Carpeta donde guardamos los dataclasses del proyecto necesarios.
│   │   └── benchmark_dataclasses.py# Dataclasses para el benchmark.
│   └── objects/                    # Carpeta donde guardamos los objetos del modelo de datos.
│       ├── docs.py                 # Objeto que contiene data\onboarding_docs.json.
│       ├── empleados.py            # Objeto que contiene data\empleados_demo.json.
│       ├── empresa.py              # Objeto que contiene data\empresa.json.
│       └── faqs.py                 # Objeto que contiene data\faq_onboarding.json.
├── llm/                            # Carpeta donde se encuentran los procesos particulares de llamadas a LLMA.
│   └── gemini/ 
│       ├── gemini_auth.py          # Carga de API key de gemini
│       └── gemini_client.py        # Llamadas al LLM de gemini
├── core/                           # Carpeta donde guardamos los ficheros de la capa de negocio
│   ├── orchestrator.py             # Orquestación (turnos, checklist, modos)
│   ├── context_delimiter.py        # Selección de docs/FAQ relevantes para delimitar el contexto.
│   ├── prompt_builder.py           # Construcción dinámica de prompts.
│   ├── user_history.py             # Objeto para mantener el perfil del empleado y su historial.
│   └── validators.py               # Validación, robustez y dominio acotado
├── common/                         # Carpeta de componentes generales
│   ├── config.py                   # Se definen los valores de losp parametros que depende el comportamiento del sistema.
│   └── utils.py                    # Funciones genéricas auxiliares y reutilizables
├── benchmark/                      # Carpeta de reports/benchmark
│   └── reports  .py                # CSV + report.md
├── entregables/                    # Conclusiones finales
│   ├── matriz_decision_1.md  
│   ├── recomendacion_1.md  
│   └── rubrica_benchmark.md  
├── output/                         # Resultados de benchmark
├── lauch.sh                        # Se debe ejecutar en terminal bash. Lanza todos los casos demo menos el 61 y 99
├── main.py                         # Punto de entrada de la aplicación
├── .gitignore                      # Ignora .venv/ y cosas del sistema
├── README.md                       # Documentación principal
└── requirements.txt                # Librerías de Python
```

## Precondiciones

* Se requiere identificador de empleado para poder interactuar con el chat. Si no eres empleado no tiene sentido interactuar con dicho chat. Además se valida que el empleado sea válido.

## Modos de ejecución

Al iniciar la aplicación con main.py se solicita un código de 2 cifras para saber que demo ejecutar. Para un chat libre (límitado a los turnos configurados) teclear 99.

- 11: Demo de asistente que simula conversación de 1 turno (empleado dev junior) para el día de onboarding {DIA_ONBOARDING}.
- 12: Demo de asistente que simula conversación masiva de varios turnos (empleado dev junior) para el día de onboarding {DIA_ONBOARDING}.
- 21: Demo de asistente que simula checklist JSON, para el día de onboarding {DIA_ONBOARDING}.
- 22: Demo de asistente que simula checklist JSON, para los cinco primeros días.
- 31: Demo de asistente que simula mismo mensaje con empleado comercial vs remoto UE, para el día de onboarding {DIA_ONBOARDING}.
- 41: Demo de seguridad con un caso trampa.
- 42: Demo de seguridad con todos los casos trampa de casos_trampa.json.
- 51: Demo de seguridad con un casos trampa comparando modelo seguro vs vulnerable.
- 61: Para ejecutar el Benchmark para el día de onboarding {DIA_ONBOARDING}. El empleado y mensaje están en preguntas.json
- 99: Conversación libre con el chat vía input para el día de onboarding {DIA_ONBOARDING}. Se acaba a los {TURNOS} turnos.

## Modelo y temperatura utilizados

### Modelo y temperatura utilizados para asistente conversacional:

- Modelo utilizado: 
  - GEMINI - gemini-3.1-flash-lite-preview
  - **Justificación**: Se utiliza este modelo porque es el que más uso permite por día y ha permitido ejecutar todos los casos de uso/demo de una vez. Otros modelos se bloqueaban por exceso de uso diario.
- Temperatura: 0.2

### Modelo y temperatura utilizados para benchmark:
- GEMINI - gemini-3.5-flash & GEMINI - gemini-3.1-flash-lite
- **Justificación**: Se han usado estos ya que a priori parecían dos modelos robustos pero suficientemente distintos para obtener resultados relevantes.
- **Peculiaridades**:
  - 2 de los 10 casos ha dado problemas por limitaciones de uso de google. Aún así se ha decidido dejarlos como ejemplo de lo que podría pasar si usamos estos modelos con capa gratuita.
  - Únicamente me he apoyado en la I.A (gemini) para la redacción de de matriz_decision_1.md y recomendacion_1.md. 

## Entregables

- Además de los ficheros .md solicitados en el apartado de benchmark, se incluyen un .txt con una salida ejecutada de cada una de las demos implementadas, a excepción de la 61 (demos de benchmark en cuyo caso hay que mirar los .md y conclusiones del benchmark) y el 99 que es un chat libre.
