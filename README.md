# ZenMasterX

**ZenMasterX** es una aplicación integral diseñada para ayudarte a equilibrar todos los aspectos clave de tu vida: salud física, finanzas personales y productividad. Con un enfoque integral y herramientas fáciles de usar, **ZenMasterX** te ofrece un control total sobre tu bienestar y objetivos.

## Características

### 1. **Módulo de Ejercicio**
   - **Seguimiento de Rutinas**: Lleva un registro de tus entrenamientos y actividades físicas.
   - **Metas Personalizadas**: Establece metas de fitness y haz un seguimiento de tu progreso.
   - **Informes de Progreso**: Visualiza estadísticas sobre tu actividad física y evolución.

### 2. **Control de Comidas y Nutrición**
   - **Base de Datos de Alimentos**: Accede a una base de datos completa de alimentos para registrar calorías, macronutrientes y más.
   - **Registro Diario**: Controla tu ingesta calórica y ajusta tu dieta para alcanzar tus objetivos.
   - **Balance Nutricional**: Mantén un equilibrio entre proteínas, carbohidratos y grasas.

### 3. **Gestión Financiera**
   - **Control de Finanzas**: Administra tus ingresos, egresos y ahorros, y lleva un control de tus deudas.
   - **Presupuestos y Metas**: Establece presupuestos mensuales y metas financieras personalizadas.
   - **Informes Financieros**: Visualiza gráficos y reportes de tu situación económica.

### 4. **Gestión de Tareas (Estilo Jira)**
   - **Organización de Proyectos**: Organiza tus proyectos y tareas personales o profesionales de manera eficiente.
   - **Seguimiento de Actividades**: Haz un seguimiento de las tareas, con fechas de vencimiento, prioridades y progreso.
   - **Notificaciones y Recordatorios**: Recibe alertas sobre tareas pendientes y objetivos por cumplir.

## Objetivo
El objetivo de **ZenMasterX** es proporcionar una plataforma completa que ayude a los usuarios a mantener un equilibrio en todas las áreas esenciales de su vida. Ya sea mejorando tu salud física, gestionando tus finanzas personales o manteniendo tus proyectos organizados, **ZenMasterX** está diseñado para guiarte en tu camino hacia una vida equilibrada y exitosa.

## Tecnologías

**ZenMasterX** está construido utilizando tecnologías modernas para asegurar una experiencia fluida y eficiente:

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Base de Datos**: PostgreSQL, SQLite (para desarrollo)
- **API**: Django REST Framework (para integraciones móviles o APIs externas)

## Instalación

### Requisitos previos

1. Tener Python 3.x instalado.
2. Tener PostgreSQL (o usar SQLite para desarrollo).

### Pasos para instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/ZenMasterX.git
   cd ZenMasterX
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura la base de datos:**
   ```bash
   python manage.py migrate
   ```

4. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

5. Abre tu navegador y ve a `http://127.0.0.1:8000/` para comenzar a usar la aplicación.

## Contribuir

Si deseas contribuir a **ZenMasterX**, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`.
3. Realiza tus cambios y haz commit: `git commit -am 'Añadir nueva funcionalidad'`.
4. Empuja tu rama: `git push origin feature/nueva-funcionalidad`.
5. Abre un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.


 kill -9 $(lsof -t -i :8000)