# Trabajo Práctico Integrador 2020 - Devops - UTN FRRe

## Como empezar

- Formar grupo de 3 personas como máximo
- Todos los integrantes deben aceptar la [invitación](https://classroom.github.com/g/Sd5rqpwM) a la actividad
- Formar el equipo o unirse al grupo correspondientes a través de la invitación

## Actividad

- Desarrollar una aplicación web que realice consultas a una base de datos

## Consideraciones

- La aplicación debe estar containerizada y administrada por un orquestador de containers
- El aprovisionamiento de la aplicación y de la base de datos debe hacerse de forma automática a partir de un Pipeline CI/CD
- La carga de datos en la base se puede hacer de forma manual o por algun otro medio no automático
- Se debe preveer la existencia de por lo menos dos entornos (desarrollo, produccion por ej)
- Se debe preveer la capacidad del despliegue de nuevas versiones en los distintos entornos de forma automática a partir de un Pipeline CI/CD
- Se debe preveer la capacidad de despliegue de cambios de esquemas en las bases de datos de forma automática a partir de un Pipeline CI/CD, los mismos deben ser manejado por el mismo pipeline que implementa los cambios de aplicación
- No se prevee que la aplicación tenga interfaz gráfica (HTML+CSS), con solo responder requests HTTP es suficiente
- Usar las siguientes tecnologías
	- **Lenguaje:** A elección
	- **Container runtime:** A elección
	- **Repositorio de artefactos:** A elección
	- **Servidor CI/CD:** A elección
	- **Motor de Base de Datos:** A elección
	- **Herramienta de migración de base de datos:** A elección
	- **Sistemas de Control de Versiones:** Github
	- **Orquestador de containers:** Kubernetes
- Se debe preveer para Kubernetes
	- Un `ingress` para acceder externamente a la aplicaciones
	- Un `configmap` para configurar la URL de la base de datos
	- Un `secret` para configurar las credenciales de acceso a las base de datos
	- Tanto la URL como las credenciales se deben consumir desde el código como variables de entorno
- Tanto el código de la aplicación, los scripts de base de datos, manifiestos de los containers, de los recursos de Kubernetes, definición de Pipelines y diapositivas para la presentación tienen que guardarse en este mismo repositorio

## Entregables

- El repositorio forkeado que incluya
	- Código
	- Manifiestos (Containers, Kubernetes)
	- Pipelines
	- Diapositivas
	- Scripts de base de datos
- No se tendrán en cuenta commits hechos fuera de termino
- Zippear el repositorio y subirlo al campus virtual [en la actividad correspondiente](https://frre.cvg.utn.edu.ar/mod/assign/view.php?id=52802)
- Se van a permitir entregas hasta el domingo 29 de noviembre.

## Presentación

Durante la exposición deberán tener preparado:

- Este repositorio con todo el código, manifiesto, pipelines completo 
- Diapositivas donde se explique brevemente:
	- Qué es lo que hace el aplicativo web
	- Arquitectura de servicios
	- Tecnologias utilizadas
	- Pipeline CI/CD
- Una demo en donde:
	- Se realice el despliegue de la aplicación y su base en sus distintos entornos
	- A traves de un request HTTP se haga una consulta a la base de datos
	- Se realice un cambio en el código observable con un cambio de esquema de base de datos asociado
	- Se ejecute el pipeline que aplique estos cambios
	- Promover estos cambios de un entorno a otro
	- Realizar una nueva request donde se pueda observar tanto el cambio de código como del esquema de base de datos

Consideraciones:

- La exposición no deberá durar mas de 45 minutos
- La exposición se realizará el lunes 30 de noviembre, a cada grupo se le asignara un horario determinado

## Criterios de Evaluación

- La calificación es individual
- Repositorio completo
- Funcionamiento de cada uno de los puntos solicitados para la demo
- Contribución (commits) de cada uno de los integrantes del grupo en el repositorio
- Exposición oral de cada integrante
- Funcionalidad, no complejidad de la aplicación y base de datos
- Puntualidad en la entrega, y a la exposición.
- Se valorará el uso de tecnologías no utilizadas en la cátedra

## Consultas

- Las clases del 16 y 20 de noviembre serán exclusivas de consultas sobre el TPI
- Se podrán hacer consultas en el canal ["TPI"](https://teams.microsoft.com/l/channel/19%3aff5e6516c6ca4f459988c651eea53393%40thread.tacv2/TPI?groupId=b2d18768-fa95-4db9-b8a2-477dfa7c332d&tenantId=35e9cd03-43d0-4947-b582-a6965c4cb674) en el equipo "Devops" en Microsoft Teams