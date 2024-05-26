import os
import requests

def crear_carpeta(nombre_carpeta):
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        print(f"Carpeta '{nombre_carpeta}' creada.")
    else:
        print(f"La carpeta '{nombre_carpeta}' ya existe.")

def descargar_archivo(url, carpeta_destino, nombre_archivo=None):
    if nombre_archivo is None:
        nombre_archivo = url.split("/")[-1]
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(f"Archivo '{nombre_archivo}' descargado en '{carpeta_destino}'.")
    else:
        print(f"Error al descargar el archivo desde {url}. Código de estado: {response.status_code}")

def print_large_message():
    print(r"""
     _    _                       _____                    
    / \  | |__  _   _ _ __  ___  |_   _|__  __ _ _ __ ___  
   / _ \ | '_ \| | | | '_ \/ __|   | |/ _ \/ _` | '_ ` _ \ 
  / ___ \| |_) | |_| | | | \__ \   | |  __/ (_| | | | | | |
 /_/   \_\_.__/ \__, |_| |_|___/   |_|\___|\__,_|_| |_| |_|
                |___/                                      
  ____                                     ___           _        _ _             _   _        ___        _ 
 / ___|  ___ _ ____   _____ _ __          |_ _|_ __  ___| |_ __ _| | | ___ _ __  | | / |      / _ \      / |
 \___ \ / _ \ '__\ \ / / _ \ '__|  _____   | || '_ \/ __| __/ _` | | |/ _ \ '__| | | | |     | | | |     | |
  ___) |  __/ |   \ V /  __/ |    |_____|  | || | | \__ \ || (_| | | |  __/ |    | | | |  _  | |_| |  _  | |
 |____/ \___|_|    \_/ \___|_|            |___|_| |_|___/\__\__,_|_|_|\___|_|    | | |_| (_)  \___/  (_) |_|
                                                                                 |_|                         
Developed by Abyns Team
    """)

def print_start_message():
    print(r"""
  ___           _        _ _ _                     _             _                             _                                                     _             
 |_ _|_ __  ___| |_ __ _| | (_)_ __   __ _   _ __ | |_   _  __ _(_)_ __  ___    __ _ _ __   __| |  ___  ___ _ ____   _____ _ __  __   _____ _ __ ___(_) ___  _ __  
  | || '_ \/ __| __/ _` | | | | '_ \ / _` | | '_ \| | | | |/ _` | | '_ \/ __|  / _` | '_ \ / _` | / __|/ _ \ '__\ \ / / _ \ '__| \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
  | || | | \__ \ || (_| | | | | | | | (_| | | |_) | | |_| | (_| | | | | \__ \ | (_| | | | | (_| | \__ \  __/ |   \ V /  __/ |     \ V /  __/ |  \__ \ | (_) | | | |
 |___|_| |_|___/\__\__,_|_|_|_|_| |_|\__, | | .__/|_|\__,_|\__, |_|_| |_|___/  \__,_|_| |_|\__,_| |___/\___|_|    \_/ \___|_|      \_/ \___|_|  |___/_|\___/|_| |_|
                                     |___/  |_|            |___/                                                                                                   
    """)

def print_end_message():
    print(r"""
  _           _        _ _       _   _                                         _      _       
 (_)_ __  ___| |_ __ _| | | __ _| |_(_) ___  _ __     ___ ___  _ __ ___  _ __ | | ___| |_ ___ 
 | | '_ \/ __| __/ _` | | |/ _` | __| |/ _ \| '_ \   / __/ _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \
 | | | | \__ \ || (_| | | | (_| | |_| | (_) | | | | | (_| (_) | | | | | | |_) | |  __/ ||  __/
 |_|_| |_|___/\__\__,_|_|_|\__,_|\__|_|\___/|_| |_|  \___\___/|_| |_| |_| .__/|_|\___|\__\___|
                                                                        |_|                   
    """)

if __name__ == "__main__":
    # Imprimir mensaje ASCII
    print_large_message()
    
    print_start_message()
    nombre_carpeta = "plugins"
    urls_descarga = {
        "WorldEdit.jar": "https://dev.bukkit.org/projects/worldedit/files/922048/download",
        "Multiverse-Core.jar": "https://dev.bukkit.org/projects/multiverse-core/files/898527/download",
        "paper-1.8.8-445.jar": "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar",
        "ViaVersion.jar": "https://github.com/ViaVersion/ViaVersion/releases/download/4.10.2/ViaVersion-4.10.2.jar",
        "ProtocolLib.jar": "https://github.com/dmulloy2/ProtocolLib/releases/download/5.2.0/ProtocolLib.jar"
    }
    nombre_paper_renombrado = "server.jar"
    
    # Crear carpeta de plugins
    crear_carpeta(nombre_carpeta)
    
    # Descargar archivos
    for nombre_archivo, url in urls_descarga.items():
        descargar_archivo(url, nombre_carpeta, nombre_archivo)
    
    # Renombrar el archivo de paper
    ruta_paper_original = os.path.join(nombre_carpeta, "paper-1.8.8-445.jar")
    ruta_paper_renombrada = os.path.join(nombre_carpeta, nombre_paper_renombrado)
    
    if os.path.exists(ruta_paper_original):
        os.rename(ruta_paper_original, ruta_paper_renombrada)
        print(f"Archivo '{ruta_paper_original}' renombrado a '{ruta_paper_renombrada}'.")
        
        # Mover el archivo renombrado una carpeta hacia atrás
        ruta_destino = os.path.join(os.path.dirname(nombre_carpeta), nombre_paper_renombrado)
        os.rename(ruta_paper_renombrada, ruta_destino)
        print(f"Archivo '{ruta_paper_renombrada}' movido a '{ruta_destino}'.")
    else:
        print(f"El archivo '{ruta_paper_original}' no existe y no se pudo renombrar.")
    print_end_message()
