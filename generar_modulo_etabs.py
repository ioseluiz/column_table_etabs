# Archivo: generar_modulo_etabs.py

import comtypes.client
import os

# 1. Define la ruta al archivo .tlb de tu instalación de ETABS
#    (¡Asegúrate de que la ruta sea correcta para tu sistema!)
ruta_tlb = r"C:\Program Files\Computers and Structures\ETABS 22\NativeAPI\x64\ETABSv1.tlb"

# 2. Comprueba si el archivo existe antes de continuar
if not os.path.exists(ruta_tlb):
    print(f"Error: No se encontró el archivo en la ruta especificada:\n{ruta_tlb}")
    print("Por favor, verifica la ruta de tu instalación de ETABS.")
else:
    try:
        # 3. Llama a GetModule para que genere el paquete "traductor"
        print(f"Generando el módulo de comtypes para ETABS...")
        etabs_module = comtypes.client.GetModule(ruta_tlb)
        
        print("\n¡Módulo generado con éxito!")
        print("Ahora tienes autocompletado en tu editor y puedes empaquetar con PyInstaller.")
        
    except Exception as e:
        print(f"\nOcurrió un error durante la generación del módulo: {e}")