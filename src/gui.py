import tkinter as tk
from tkinter import filedialog, ttk
import os
import sys
from PIL import Image, ImageTk, UnidentifiedImageError
import requests

# Configura o UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# URL da API
API_URL = "http://127.0.0.1:8000/predict/"

# Inicializa o caminho do arquivo
file_path = None

# Cria a tela do Tkinter
root = tk.Tk()
root.title("Pet Emotion Classifier")
root.geometry("600x700")
root.configure(bg="#f0f0f0")

# Custom styles
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", padding=10, font=('Helvetica', 12))
style.configure("TLabel", padding=5, font=('Helvetica', 12), background="#f0f0f0")

# Cores
PRIMARY_COLOR = "#4a90e2"
SECONDARY_COLOR = "#f39c12"
BG_COLOR = "#f0f0f0"
TEXT_COLOR = "#333333"

def upload_image():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        try:
            file_path = os.path.normpath(file_path)
            img = Image.open(file_path)
            img = img.resize((300, 300))
            img = ImageTk.PhotoImage(img)
            image_label.config(image=img)
            image_label.image = img
            result_label.config(text="")
            detect_button.config(state=tk.NORMAL)
        except UnidentifiedImageError:
            result_label.config(text="Arquivo inválido. Escolha uma imagem válida.")

def detect_emotion():
    global file_path
    if not file_path:
        result_label.config(text="Primeiro, carregue uma imagem.")
        return
    
    try:
        # Envia a imagem para a API
        with open(file_path, "rb") as image_file:
            files = {"file": image_file}
            response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result = response.json()
            emotion = result.get("class", "Desconhecido")
            confidence = result.get("confidence", 0) * 100
            result_label.config(text=f"Emoção Detectada: {emotion}\nConfiança: {confidence:.2f}%")
        else:
            result_label.config(text=f"Erro na API: {response.status_code}")
    except Exception as e:
        result_label.config(text=f"Erro ao conectar com a API: {str(e)}")

# Tela principal
main_frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Titulo
title_label = ttk.Label(main_frame, text="Classificador de Emoções de Pets", font=('Helvetica', 24, 'bold'), foreground=PRIMARY_COLOR)
title_label.grid(row=0, column=0, pady=(0, 20))

# Instrução
instruction_label = ttk.Label(main_frame, text="Escolha uma imagem do seu Pet:", font=('Helvetica', 14))
instruction_label.grid(row=1, column=0, pady=(0, 10))

# Botão de upload
upload_button = ttk.Button(main_frame, text="Carregue seu arquivo", command=upload_image, style="TButton")
upload_button.grid(row=2, column=0, pady=(0, 20))

# Imagem carregada
image_label = ttk.Label(main_frame)
image_label.grid(row=3, column=0, pady=(0, 20))

# Botão de detectar
detect_button = ttk.Button(main_frame, text="Detectar Emoção", command=detect_emotion, style="TButton")
detect_button.grid(row=4, column=0, pady=(0, 20))
detect_button.config(state=tk.DISABLED)

# Tela de resultado
result_label = ttk.Label(main_frame, text="", wraplength=400, justify="center", font=('Helvetica', 14))
result_label.grid(row=5, column=0, pady=(0, 20))

# Configure grid
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
