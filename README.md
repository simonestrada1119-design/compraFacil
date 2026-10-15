# CompraFácil — Django

Proyecto desarrollado hasta el punto 6 de la guía: validaciones en Django incluidas.

## 1. Requisitos
- Python 3.10 o superior
- Visual Studio Code (opcional)

## 2. Abrir la carpeta
Descomprime el ZIP y abre la carpeta `CompraFacil` en VS Code.

## 3. Crear y activar entorno virtual (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Si PowerShell bloquea la activación, puedes usar CMD:
```cmd
.venv\Scripts\activate.bat
```

## 4. Instalar Django
```powershell
python -m pip install -r requirements.txt
```

## 5. Crear base de datos local y administrador
```powershell
python manage.py makemigrations compras
python manage.py migrate
python manage.py createsuperuser
```
Escribe el nombre de usuario, correo (opcional) y contraseña del administrador.

## 6. Ejecutar
```powershell
python manage.py runserver
```
Abre http://127.0.0.1:8000/ y entra con el usuario creado.

## Funciones incluidas
- Inicio y cierre de sesión con autenticación de Django.
- CRUD de proveedores, con NIT único.
- CRUD de compras, con número de compra único, proveedor existente y usuario autenticado.
- Búsqueda de proveedores por razón social o NIT.
- Filtro de compras por proveedor y estado.
- Validaciones de navegador mediante JavaScript y validaciones de servidor mediante formularios/modelos Django.
- Confirmación antes de eliminar registros.

## Nota
Para que puedas ejecutar el proyecto de inmediato, la configuración inicial usa SQLite local. La guía original solicita PostgreSQL en Neon y despliegue en Render, pero esos pasos están fuera del alcance pedido (hasta el punto 6 de validaciones).


## Inicio de sesión sencillo
El login usa el formulario estándar de Django (`{{ form.as_p }}`), sin diseño ni validaciones personalizadas adicionales. Aun así, la autenticación sigue activa para proteger las páginas administrativas.
