# Manual de Usuario: Sistema de Parqueadero Otherworld Park

## Descripción del Sistema

Sistema de parqueadero diseñado con temática espacial para interacción más amigable con los usuarios que lo emplean. Este sistema fue creado con el propósito de que el usuario tenga un espacio manejado por consola donde pueda registrar su vehículo y se gestione tanto la entrada como la salida, al igual que la cantidad de horas que este permanezca dentro del sistema.

---

## Reglas del Sistema de Parqueadero Otherworld Park

- Una nave solo puede estar acoplada una vez.
- Solo se aceptan placas en el formato correcto: tres letras y tres números (ej: ABC123).
- El cobro mínimo por uso del hangar es una hora: $7,000.
- Cada 15 minutos adicionales cuesta $1,500.

---

## Instrucciones del Sistema para el Usuario

### Registrar Tripulante

- Recordatorio: solo se permite un formato de placa con 6 caracteres (3 letras y 3 números).
- Selecciona la opción **1** en el menú principal.
- Ingresa: nombre, apellido, documento de identidad y placa de la nave.
- Si todo es válido, se despliega un mensaje de **registro exitoso**.

### Ingresar Nave

- Selecciona la opción **2** del menú.
- Ingresa la placa de tu nave.
- Solo puedes ingresar si estás registrado y hay espacio en el hangar.

### Retirar Nave

- Selecciona la opción **3** del menú.
- Ingresa la placa de tu nave.
- Se mostrará un recibo detallado:
  - Tiempo de permanencia.
  - Tarifa por hora.
  - Cuartos de hora adicionales.
  - Total a pagar.

### Salir

- Selecciona la opción **5** del menú para salir del sistema.

---

## Instrucciones del Sistema para Administrador

> Función solo permitida para usuarios autorizados

**Usuarios permitidos:**
- admin
- comandante
- supervisor

**Contraseñas válidas:**
- admin123
- space2025
- hangar456

### Funciones Disponibles

- Ver total de naves registradas.
- Ver historial de naves retiradas.
- Ver naves actualmente en el hangar.
- Ver total recaudado por cobros.
- Consultar tiempo promedio de estancia de las naves.
- Exporta historial de naves retiradas, la información de los que están en el hangar y los usuarios registrados en dos archivos llamados `usuarios.csv` y `historial_retiradas.csv`
  - El archivo se guarda en la misma carpeta donde se ejecuta el sistema.

---

## Errores Comunes

- Ingresar una placa con formato incorrecto.
- Intentar ingresar una nave que ya está dentro.
- Retirar una nave no registrada.
- Ingresar datos con números en nombre o apellido.

