Crear un Entorno de python:
	python -m venv .venv
	
Activar un entorno en python:
	.venv\Scripts\activate
	
Desactivar un entorno en python:
	.venv\Scripts\deactivate	
	
Ver lista de packages instalados directamenete y los instalados debido a dependencias:
	pip list
	
Ver lista de packages primarios instaldos, sin los paquetes instalados por dependencias:
	pip list --not-required

VEr los detalles de un package instalado:
	pip show <package>

Desinstalar un package:
	pip uninstall <package>
	
Instalar una versión concreta:
	pip install requests==2.0
	
Actualizar una version instalada:
	pip install -U requests
	
Ver las dependencias de un proyecto y guardarlas en un fichero:
	pip freeze > requiremets.txt
	
Desinstalar todos los paquetes utilizados:
	pip uninstall -y -r requirements.txt
	
Instalar todos los paquetes necesarios:
	pip install -r requirements.txt