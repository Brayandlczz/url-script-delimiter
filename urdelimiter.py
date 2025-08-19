import re
import tkinter as tk
from tkinter import messagebox

def procesar_urls():
    entrada = text_area.get("1.0", tk.END).strip().splitlines()
    ids_validos = []
    ids_invalidos = []

    for url in entrada:
        match = re.search(r'/d/([^/]+)/', url)
        if match:
            candidate = match.group(1)
            if len(candidate) in (33, 34):  
                ids_validos.append(candidate)
            else:
                ids_invalidos.append(candidate)
        elif re.fullmatch(r"[A-Za-z0-9_-]{33,34}", url):
            ids_validos.append(url)
        else:
            if url:  
                ids_invalidos.append(url)

    salida_text.delete("1.0", tk.END)

    total_urls = len([u for u in entrada if u.strip()]) 
    total_validos = len(ids_validos)
    total_invalidos = len(ids_invalidos)

    salida_text.insert(tk.END, f"Total ingresados: {total_urls}\n")
    salida_text.insert(tk.END, f"Válidos: {total_validos}\n")
    salida_text.insert(tk.END, f"Inválidos: {total_invalidos}\n\n")

    if ids_validos:
        longitudes = {len(i) for i in ids_validos}
        if len(longitudes) == 1:
            salida_text.insert(tk.END, f"Todos los IDs válidos tienen {longitudes.pop()} caracteres\n\n")
        else:
            salida_text.insert(tk.END, "Los IDs válidos tienen distintas longitudes:\n")
            for i in ids_validos:
                salida_text.insert(tk.END, f"- {i} → {len(i)} caracteres\n")

        salida_text.insert(tk.END, "\nIDs válidos:\n")
        for i in ids_validos:
            salida_text.insert(tk.END, f"{i}\n")
    else:
        salida_text.insert(tk.END, "No se encontraron IDs válidos.\n")

    if ids_invalidos:
        salida_text.insert(tk.END, "\nIDs/URLs inválidos:\n")
        for i in ids_invalidos:
            salida_text.insert(tk.END, f"{i}\n")

def limpiar_campos():
    text_area.delete("1.0", tk.END)   
    salida_text.delete("1.0", tk.END) 

ventana = tk.Tk()
ventana.title("Extractor de IDs de Google Drive")
ventana.geometry("600x500")

tk.Label(ventana, text="Adjunta las URL's o ID's aquí:").pack()
text_area = tk.Text(ventana, height=10, width=70)
text_area.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Extraer ID's", command=procesar_urls, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar_campos, width=15).pack(side=tk.LEFT, padx=5)

tk.Label(ventana, text="Fragmento ID:").pack()
salida_text = tk.Text(ventana, height=15, width=70)
salida_text.pack(pady=10)

ventana.mainloop()
