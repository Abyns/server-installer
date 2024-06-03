# Información General

Para descargar los complementos que normalmente se utilizan en un servidor de Minecraft, deberá instalar PowerShell y Python desde la Microsoft Store en su computadora. Una vez instalados, abra PowerShell y ejecute el siguiente comando para verificar si Python se ha instalado correctamente:

```sh
python --version

Si Python está instalado correctamente, verá la versión de Python en la salida del comando. A continuación, instale la dependencia necesaria ejecutando el siguiente comando:
pip install requests

Después de instalar las dependencias, puede utilizar el instalador automático que se le ha proporcionado, llamado "Plugin installer and version server". Ejecute este comando en su terminal de PowerShell:
python '.\Plugin installer and version server.py'

Con esto, tendrá el servidor completamente configurado. Para iniciar el servidor, utilice el siguiente comando en PowerShell:
.\start.bat

Información sobre start.bat
El contenido predeterminado de start.bat es el siguiente:
java -Xms2G -Xmx4G -jar server.jar run
PAUSE

Para que el mundo "Spawn (default)" esté vacío, configure el archivo server.properties de la siguiente manera:
generator-settings=2;0x0;
Si no desea esta configuración, cambie los siguientes valores:
level-type=FLAT
generator-settings=2;0x0;
Por:
level-type=
generator-settings=

Mensajes en Español
Configuraciones de mensajes en archivos específicos:

bukkit.yml:
settings:
  shutdown-message: §fReiniciando el servidor
spigot.yml:
messages:
  whitelist: '&fEstamos realizando &6Mantenimiento&f. ¡Por favor, vuelve en unas horas!'
  unknown-command: '&c&lUps&7, ese comando no es reconocido. Intenta usar &a/ayuda&7 para asistencia'
  server-full: '&f¡Los servidores están llenos! Obtén un rango &dVIP&f para &aentrar&f sin esperar!'
  outdated-client: '&fPor favor, actualiza tu cliente a &b{0}&f para acceder al servidor!'
  outdated-server: '&fNuestro servidor está desactualizado. Por favor, usa &b{0}&f para conectarte!'
  restart: '&fEstamos &ereiniciando&f el servidor. ¡Por favor espera 1 minuto!'


