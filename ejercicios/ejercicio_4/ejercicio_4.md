# Ejercicio 4: "*Unrestricted File Upload*"

**Nombre**: Cristian Durán

--- 
## Introduccion
Hemos enfatizado la importancia de ser extremadamente cautelosos en el manejo de la entrada de los usuarios, incluyendo los archivos. De hecho, la vulnerabilidad [*Unrestricted File Upload*](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload), la cual corresponde a confiar plenamente en los archivos subidos por el usuario, puede tener consecuencias catastróficas.

El objetivo de este ejercicio es comprender bien las posibles **consecuencias** de un manejo de archivos "mediocre" y las formas de **prevenirlas**.

## Pregunta 1
Investigue y explique **con sus propias palabras** 3 posibles ataques que un usuario malicioso podria realizar a una aplicacion web con la vulnerabilidad *Unrestricted File Upload*". Se espera que para cada ataque se mencionen las **consecuencias** del mismo.

**Respuesta:** 
1. Ataque de denegación de servicio (DoS): Este tipo de ataque es bastante conocido y consiste en agotar los recursos del servidor, por ejemplo subiendo archivos extremadamente grandes y así afectar la disponibilidad de la aplicación web.
2. Ataque de cross-site-scripting (XSS): Consiste en subir un archivo malicioso que luego otro usuario va a descargar por error en su navegador con lo cual se pueden robar datos valiosos como las cookies, sesiones de usuario o incluso realizar acciones en nombre del usuario.
3. Ataque de inyección de código: Consiste en subir un archivo el cual inyecta código en la aplicación web permitiendo robar datos, modificar  o eliminar información, etc.

## Pregunta 2
Ahora que ya tenemos claro que descuidar el manejo de archivos es peligroso, les pedimos listar 5 metodos preventivos para esta vulnerabilidad.

**Respuesta:**
1. La verificación del tipo y contenido del archivo.
2. Encriptación de archivos.
3. La implementación de sistema de detección de malware.
4. Autenticación y autorización de usuario.
5. Validación de entrada de usuario.