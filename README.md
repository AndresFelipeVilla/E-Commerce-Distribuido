# 🛒 E-Commerce Distribuido - Proyecto de Microservicios

Este proyecto consiste en el desarrollo de una aplicación de comercio electrónico construida bajo **arquitectura de microservicios**, con servicios independientes implementados en **Java (Spring Boot)** y **Python (Django REST Framework)**, comunicándose a través de **REST APIs** y orquestados con **Docker Compose**.

---

## 🎯 Objetivo General

Desarrollar una solución distribuida para un sistema de e-commerce que permita gestionar clientes, productos, inventario y órdenes, utilizando múltiples tecnologías y fomentando el desarrollo colaborativo.

---

## 📦 Microservicios

| Microservicio        | Lenguaje         | Descripción |
|----------------------|------------------|-------------|
| `cliente-service`    | Java + Spring Boot | Gestión de usuarios/clientes |
| `orden-service`      | Java + Spring Boot | Registro de órdenes y sus detalles |
| `producto-service`   | Python + Django    | Administración de productos |
| `inventario-service` | Python + Django    | Control de stock de productos |

---

## 🔧 Tecnologías Utilizadas

### 🛠️ Lenguajes y Frameworks

- **Java 17**
- **Spring Boot 3**
- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**

### 🗃️ Bases de Datos

- **PostgreSQL** (instancia por microservicio)

### 🔗 Comunicación

- **REST API**
- **OpenAPI / Swagger** para documentación de endpoints

### 🐳 DevOps / Infraestructura

- **Docker**
- **Docker Compose**
- **Nginx** (opcional, para gateway / balanceo de carga)
- **Git + GitHub**
- **Postman** (pruebas manuales)

---

## 📁 Estructura del Proyecto

```bash
proyecto-ecommerce/
│
├── cliente-service/            # Microservicio Java
├── orden-service/              # Microservicio Java
├── producto-service/           # Microservicio Python
├── inventario-service/         # Microservicio Python
│
├── docker-compose.yml          # Orquestación de contenedores
├── nginx/                      # Configuración opcional de gateway
└── README.md                   # Este archivo
```

---

## 📌 Funcionalidades por Microservicio

### 🧍 cliente-service (Java + Spring Boot)
- Crear, actualizar, eliminar y listar clientes
- Consultar cliente por ID o email
- Relación 1:N con órdenes

### 📦 producto-service (Python + Django)
- Crear, editar, eliminar y listar productos
- Filtrado por nombre, categoría, precio
- Endpoint de consulta para otros servicios

### 🏬 inventario-service (Python + Django)
- Control de stock (entradas y salidas)
- Verificación de stock disponible
- Actualización de stock tras una venta

### 🧾 orden-service (Java + Spring Boot)
- Crear órdenes para un cliente
- Incluir múltiples productos por orden
- Consultar historial de órdenes por cliente

---

## 🚀 Roadmap de Desarrollo

1. Diseño de modelos y relaciones (UML o ERD)
2. Crear repositorios individuales para cada microservicio
3. Configurar PostgreSQL en cada servicio
4. Implementar funcionalidades CRUD básicas
5. Exponer endpoints REST y documentarlos con Swagger/OpenAPI
6. Probar endpoints con Postman
7. Configurar Dockerfiles y `docker-compose.yml`
8. Implementar comunicación entre servicios
9. Validar integración entre servicios
10. Agregar pruebas automatizadas

---

## 🧪 Pruebas

- **Pruebas Manuales:** con Postman

---

## 🌐 Comunicación entre Microservicios

- `orden-service` consulta a:
  - `cliente-service` para validar cliente existente
  - `producto-service` para obtener datos del producto
  - `inventario-service` para verificar stock antes de registrar la orden

> Todas las llamadas se realizan a través de **REST APIs** documentadas con Swagger.

---

## 🤝 Colaboración

Este proyecto está pensado para el trabajo en equipo entre desarrolladores de Java y Python. Cada microservicio puede desarrollarse, probarse y desplegarse de forma independiente.

---

## 📬 Contacto

Andres Felipe Villa Pardo: 
Email: andresfelipevillapardo7@gmail.com
Linkedin: https://www.linkedin.com/in/andres-felipe-villa-pardo

Santiago Villa Ramos
Email: 
Linkedin: https://www.linkedin.com/in/santiago-villa-6784412a8
