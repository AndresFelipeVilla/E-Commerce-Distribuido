# Imagen con Maven y JDK 17
FROM maven:3.9.4-eclipse-temurin-17

# Directorio de trabajo
WORKDIR /app

# Copiamos todo el proyecto (ideal para desarrollo)
COPY . .

# Exponemos el puerto de la app (ajústalo si es distinto)
EXPOSE 8085

# Comando para correr la app directamente desde Maven (modo desarrollo)
CMD ["mvn", "spring-boot:run"]