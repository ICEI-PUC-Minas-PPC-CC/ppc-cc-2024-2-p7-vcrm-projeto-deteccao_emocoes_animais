from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Cria a instância da API
app = FastAPI(title="API de Classificação de Emoções", description="API para classificar emoções em imagens", version="1.0")

# Carrega o modelo de Machine Learning
MODEL_PATH = "pets_detection.keras"
model = load_model(MODEL_PATH)

# Mapeia as classes do modelo
CLASS_NAMES = ["Happy", "Sad", "Angry"]

@app.get("/")
def root():
    #print("Teste")
    return {"message": "Bem-vindo à API de Classificação de Emoções!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Recebe uma imagem e retorna a previsão da classe.
    """
    try:
        # Log da requisição recebida
        print(f"Recebendo request: {file.filename}, content_type: {file.content_type}")

        # Salva a imagem temporariamente
        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as f:
            f.write(await file.read())

        # Carrega e pré-processa a imagem
        image = load_img(temp_file, target_size=(224, 224))  # Redimensiona para 224x224
        image_array = img_to_array(image) / 255.0           # Normaliza os pixels
        image_array = np.expand_dims(image_array, axis=0)   # Adiciona dimensão para batch

        # Faz a previsão
        predictions = model.predict(image_array)
        predicted_class = CLASS_NAMES[np.argmax(predictions)]
        confidence = float(np.max(predictions))

        # Remove o arquivo temporário
        os.remove(temp_file)

        # Retorna a previsão
        response = {"class": predicted_class, "confidence": confidence}
        print(f"Resposta gerada: {response}")  # Log da resposta
        return JSONResponse(content=response)

    except Exception as e:
        error_message = {"error": str(e)}
        print(f"Erro ao processar a requisição: {error_message}")  # Log do erro
        return JSONResponse(content=error_message, status_code=500)
