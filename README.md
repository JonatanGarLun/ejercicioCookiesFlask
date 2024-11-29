# Ejercicio sobre las Cookies en Flask

## Preguntas 

### ¿En qué casos específicos no es obligatorio informar o pedir consentimiento previo para el uso de cookies según el RGPD?

**Cookies técnicas o funcionales estrictamente necesarias, como las que permiten**:

- Navegar por el sitio web y utilizar funciones esenciales, como el inicio de sesión o la gestión de carritos de compra

- Cookies de personalización elegidas por el usuario, como aquellas que recuerdan el idioma seleccionado o preferencias de visualización, siempre que no se utilicen con fines adicionales como marketing o análisis.

- Cookies necesarias para ejecutar servicios solicitados explícitamente por el usuario, como las que gestionan formularios o procesan pagos.

### Si un sitio web utiliza cookies analíticas de terceros, ¿qué pasos debe seguir para cumplir con el RGPD?

1. **Obtener el consentimiento previo e informado del usuario**  
   Antes de instalar cualquier cookie analítica, es obligatorio solicitar el consentimiento explícito del usuario mediante un banner o gestor de cookies. Este consentimiento debe ser libre, específico, informado y revocable.

2. **Proporcionar información clara y detallada**  
   El sitio debe incluir una política de cookies donde se explique qué datos recopilan las cookies, quién es el tercero responsable (por ejemplo, Google Analytics) y los fines específicos de las cookies y cómo se utilizan.

3. **Permitir la gestión de preferencias de cookies**  
   Implementar un sistema que permita a los usuarios:
   - Aceptar, rechazar o personalizar el uso de cookies analíticas.
   - Modificar o revocar su consentimiento en cualquier momento.

4. **Evitar instalar cookies antes del consentimiento**  
   Las cookies analíticas de terceros no deben activarse hasta que el usuario haya dado su consentimiento explícito.

5. **Asegurarse de que el proveedor cumple con el RGPD**  
   Si se utilizan servicios de terceros, como Google Analytics, se debe:
   - Establecer un contrato que garantice que el proveedor actúa como encargado del tratamiento de datos.
   - Verificar que cumple con las normativas de protección de datos.
