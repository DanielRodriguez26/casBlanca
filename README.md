# Casa Blanca - Sistema de Gestión Empresarial

## 📋 Descripción

**Casa Blanca** es un sistema web de gestión empresarial desarrollado en Python con Flask, diseñado para administrar inventarios, ventas, gastos y usuarios de manera eficiente y segura.

## ✨ Características Principales

### 🔐 Sistema de Autenticación
- **Multi-rol**: Administrador Super, Administrador y Ventas
- **Sesiones seguras** con hash de contraseñas
- **Control de acceso** basado en roles

### 📦 Gestión de Inventario
- **Productos**: Crear, editar y gestionar productos
- **Stock**: Control de cantidades y valores unitarios
- **Imágenes**: Soporte para subida de imágenes de productos
- **Categorización**: Organización por tipos de productos

### 💰 Sistema de Ventas
- **Facturación**: Generación automática de facturas
- **Carrito de compras**: Gestión de productos en venta
- **Historial**: Seguimiento de todas las transacciones
- **Estados**: Control de ventas diarias, mensuales y anuales

### 💸 Control de Gastos
- **Registro de gastos**: Categorización y descripción
- **Estados**: Seguimiento diario, mensual y anual
- **Reportes**: Análisis de gastos por períodos

### 👥 Gestión de Usuarios
- **CRUD completo**: Crear, leer, actualizar y eliminar usuarios
- **Roles diferenciados**: Permisos específicos por función
- **Seguridad**: Contraseñas hasheadas y validación de sesiones

### 📊 Dashboard y Reportes
- **Resumen ejecutivo**: Gastos, ventas y ganancias
- **Métricas diarias y mensuales**: Seguimiento de KPIs
- **Historial detallado**: Consulta de transacciones específicas

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.x + Flask
- **Base de Datos**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticación**: Sistema personalizado con hash
- **Logging**: Sistema de logs para errores y acceso

## 📁 Estructura del Proyecto

```
CasaBlanca/
├── app.py                 # Aplicación principal Flask
├── modules/               # Módulos de funcionalidad
│   ├── authentication.py  # Sistema de autenticación
│   ├── globalvariables.py # Configuración global
│   ├── customhash.py      # Funciones de hash
│   └── usuarios.py        # Gestión de usuarios
├── templates/             # Plantillas HTML
│   ├── login.html         # Página de inicio de sesión
│   ├── index.html         # Dashboard principal
│   ├── usuarios.html      # Gestión de usuarios
│   ├── productos.html     # Gestión de productos
│   └── ...                # Otras plantillas
├── static/                # Archivos estáticos
│   ├── css/               # Estilos CSS
│   ├── js/                # JavaScript
│   ├── img/               # Imágenes y archivos subidos
│   └── assets/            # Recursos adicionales
└── casaBlanca_error.log   # Log de errores
```

## 🚀 Instalación

### Prerrequisitos
- Python 3.7 o superior
- MySQL 5.7 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el repositorio
```bash
git clone [URL_DEL_REPOSITORIO]
cd CasaBlanca
```

### 2. Instalar dependencias
```bash
pip install flask
pip install flask-mysqldb
pip install mysql-connector-python
pip install werkzeug
```

### 3. Configurar base de datos
1. Crear una base de datos MySQL llamada `casaBlanca`
2. Importar el esquema de base de datos (si existe)
3. Actualizar las credenciales en `modules/globalvariables.py`:
   ```python
   self.MysqlHost = "localhost"
   self.MysqlUser = "tu_usuario"
   self.MysqlPassword = "tu_contraseña"
   self.MysqlDatabase = "casaBlanca"
   ```

### 4. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:3000`

## 🔧 Configuración

### Variables de Entorno
El sistema utiliza variables globales configuradas en `modules/globalvariables.py`:

- **MysqlHost**: Host de la base de datos
- **MysqlUser**: Usuario de MySQL
- **MysqlPassword**: Contraseña de MySQL
- **MysqlDatabase**: Nombre de la base de datos

### Configuración de la Aplicación
- **Puerto**: 3000 (configurable en `app.py`)
- **Debug**: Habilitado por defecto
- **Secret Key**: Configurada en la aplicación
- **Upload Folder**: `./static/img/` para imágenes de productos

## 👤 Roles de Usuario

### 1. Administrador Super (Rol 1)
- Acceso completo a todas las funcionalidades
- Gestión de usuarios y roles
- Configuración del sistema

### 2. Administrador (Rol 2)
- Gestión de inventario y productos
- Control de gastos y ventas
- Reportes y estadísticas

### 3. Ventas (Rol 3)
- Proceso de ventas y facturación
- Consulta de productos disponibles
- Historial de transacciones

## 📱 Uso del Sistema

### 1. Inicio de Sesión
- Acceder a `http://localhost:3000`
- Ingresar credenciales de usuario
- El sistema redirigirá según el rol del usuario

### 2. Dashboard Principal
- **Administradores**: Vista completa con métricas de gastos, ventas y ganancias
- **Ventas**: Vista específica para operaciones de venta

### 3. Gestión de Productos
- **Nuevo Producto**: Agregar productos con imagen, precio y cantidad
- **Editar Cantidad**: Actualizar stock existente
- **Consulta**: Ver productos disponibles

### 4. Sistema de Ventas
- **Selección**: Elegir productos del inventario
- **Facturación**: Generar factura automáticamente
- **Historial**: Consultar transacciones realizadas

### 5. Control de Gastos
- **Registro**: Agregar nuevos gastos con descripción
- **Seguimiento**: Estados diarios, mensuales y anuales
- **Edición**: Modificar gastos existentes

## 🔒 Seguridad

- **Autenticación**: Sistema de login con validación de credenciales
- **Sesiones**: Control de sesiones activas
- **Hash**: Contraseñas encriptadas con algoritmo personalizado
- **Roles**: Control de acceso basado en permisos
- **Logs**: Registro de errores y actividades del sistema

## 📝 Logs y Monitoreo

El sistema mantiene logs detallados en `casaBlanca_error.log`:
- Errores de aplicación
- Intentos de autenticación
- Operaciones críticas del sistema

## 🚨 Solución de Problemas

### Error de Conexión a Base de Datos
1. Verificar credenciales en `modules/globalvariables.py`
2. Confirmar que MySQL esté ejecutándose
3. Verificar que la base de datos `casaBlanca` exista

### Error de Permisos
1. Verificar que el usuario tenga permisos en la base de datos
2. Confirmar que las tablas necesarias existan

### Problemas de Subida de Archivos
1. Verificar permisos en la carpeta `static/img/`
2. Confirmar que el formato de archivo sea permitido
3. Verificar el tamaño máximo del archivo (500KB)

## 🤝 Contribución

Para contribuir al proyecto:

1. Fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto es propiedad de **Casa Blanca** y fue desarrollado para uso interno de la empresa.

## 👨‍💻 Equipo de Desarrollo

**Casa Blanca** fue desarrollado por un equipo de desarrolladores dedicados a crear soluciones empresariales eficientes y seguras.

---

**Nota**: Este sistema está diseñado para uso empresarial y requiere configuración adecuada de la base de datos y servidor antes de su implementación en producción.
