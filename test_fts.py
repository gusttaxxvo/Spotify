import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Função para criar a interface
def criar_interface():
    # Criando a janela principal
    root = tk.Tk()
    root.title("Tela do Spotify")

    # Definir o tamanho da janela
    root.geometry("600x200")

    # Carregar a imagem da capa (certifique-se de substituir pelo caminho correto)
    img_capa = Image.open("caminho_da_imagem.jpg")  # Substitua com o caminho da imagem
    img_capa = img_capa.resize((100, 100))  # Redimensionando a imagem para 100x100 pixels
    img_capa_tk = ImageTk.PhotoImage(img_capa)

    # Criar o label para a imagem da capa no canto esquerdo
    label_imagem = tk.Label(root, image=img_capa_tk)
    label_imagem.grid(row=0, column=0, padx=20, pady=50)

    # Nome da música (pode ser alterado dinamicamente)
    nome_musica = "Nome da Música"  # Substitua com o nome da música

    # Criar o label para o nome da música no canto direito
    label_nome = tk.Label(root, text=nome_musica, font=("Arial", 24), anchor="w")
    label_nome.grid(row=0, column=1, padx=20, pady=50, sticky="w")

    # Mantenha a janela aberta
    root.mainloop()

# Chamar a função para criar a interface
criar_interface()
