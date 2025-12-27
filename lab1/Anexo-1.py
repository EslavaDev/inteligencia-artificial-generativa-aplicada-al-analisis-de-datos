#Datos de entrada 
reseñas = [
    "Producto llegó dañado y el empaque estaba abierto.",
    "No cumple con las expectativas, material de mala calidad.",
    "Demasiado pequeño, la descripción no coincidía con el tamaño real.",
    "Entrega muy lenta. No volveré a comprar.",
    "El color no es como en la imagen, parece usado.",
    "El servicio al cliente no respondió ante mi reclamación.",
    "Las instrucciones eran confusas y venían en otro idioma.",
    "Faltaban piezas importantes dentro del paquete.",
    "El producto dejó de funcionar a los pocos días.",
    "Precio elevado para la calidad ofrecida.",
    "Se desliza demasiado, no es seguro como se anunciaba.",
    "La batería dura muy poco, nada que ver con lo prometido.",
    "Vino con manchas y olores extraños, parecía de segunda mano.",
    "Muy complicado de configurar, requiere asistencia técnica.",
    "Tuve que pagar gastos adicionales que no estaban informados."
]

#Diseño del Prompt 
prompt_sistema = """
Eres un Analista de Datos experto en Experiencia de Cliente (CX).
Tu objetivo es analizar un listado de reseñas negativas.
Genera un informe con la siguiente estructura:
1. Resumen Ejecutivo (máx 3 líneas para dirección).
2. Puntos Fuertes (si existen).
3. Puntos Débiles (agrupados por categorías: Logística, Producto, Servicio).
4. Dos acciones de mejora concretas y accionables.
"""

prompt_usuario = f"Aquí tienes las reseñas para analizar: {reseñas}"

#Función simulada de llamada al LLM
def analizar_reseñas(sistema, usuario):
    #Simulación de: client.chat.completions.create(...)
    print("--- 1. Enviando Prompt al LLM ---")
    print(f"[Sistema]: {sistema}")
    print(f"[Usuario]: {usuario[:100]}... (truncado por longitud)\n")
    
    print("--- 2. Respuesta Generada (Simulada para el Informe) ---")
    
    #"respuesta esperada"
    respuesta_simulada = """
INFORME DE ANÁLISIS DE RESEÑAS

1. Resumen Ejecutivo:
Se detecta una insatisfacción crítica generalizada, afectando tanto a la calidad física del producto (daños, uso previo, materiales) como a la logística. La reputación de la marca está en riesgo alto debido a la percepción de "producto usado" y falta de soporte.

2. Puntos Fuertes:
- No se han identificado puntos fuertes en este lote de reseñas negativas.

3. Puntos Débiles (Categorizados):
- Producto: Mala calidad de materiales, producto dañado/usado, discrepancia con la descripción (tamaño/color), faltan piezas, batería deficiente.
- Logística: Entregas lentas, empaques abiertos, cobros adicionales no informados.
- Servicio: Soporte al cliente ausente, instrucciones en otro idioma.

4. Acciones de Mejora:
- Acción A (Control de Calidad): Implementar una auditoría de salida obligatoria para verificar que el producto no tenga manchas/olores y que el kit de piezas esté completo antes del envío.
- Acción B (Transparencia): Revisar la ficha del producto en la web para asegurar que las fotos y descripciones de tamaño sean 100% fieles a la realidad y evitar devoluciones por falsas expectativas.
    """
    print(respuesta_simulada)

#Ejecución del flujo
if __name__ == "__main__":
    analizar_reseñas(prompt_sistema, prompt_usuario)