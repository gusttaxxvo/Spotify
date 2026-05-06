#Diogo Alves , Gustavo Silva , isabela Araujo , Isabelly Alves, Júlia Anjos e Mateus Henrique 

from tkinter import *


# --- Cores Spotify ---
SPOTIFY_GREEN = "#1ED760"  # Verde vibrante
SPOTIFY_BLACK = "#191414"  # Preto escuro

# --- Função para criar retângulo com bordas arredondadas ---
def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# --- Função para criar botões arredondados ---
def botao_arredondado(tela, texto, comando):
    canvas = Canvas(tela, width=200, height=50, bg=SPOTIFY_BLACK, highlightthickness=0)
    canvas.pack(pady=10)
    button = create_rounded_rect(canvas, 5, 5, 195, 45, radius=20,
                                 fill=SPOTIFY_GREEN, outline="#1ED760", width=2)
    label = canvas.create_text(100, 25, text=texto, font=("Outfit-Bold", 16), fill="black")
    canvas.tag_bind(button, "<Button-1>", lambda e: comando())
    canvas.tag_bind(label, "<Button-1>", lambda e: comando())

# --- Função para criar cards (texto + imagem opcional) ---
def criar_card(parent, texto, imagem=None):
    card = Canvas(parent, width=160, height=60, bg=SPOTIFY_BLACK, highlightthickness=0)
    create_rounded_rect(card, 2, 2, 158, 58, radius=15, fill="#282828")

    if imagem:
        card.create_image(30, 30, image=imagem)  # imagem à esquerda
        card.image = imagem  # evita descarte pelo garbage collector
        card.create_text(70, 30, text=texto, font=("Outfit-Bold", 14), fill="white", anchor="w")
    else:
        card.create_text(80, 30, text=texto, font=("Outfit-Bold", 14), fill="white")

    card.pack(side=LEFT, padx=5, pady=5)
    return card

# --- Telas ---
def abrir_tela_cadastro():
    principal.destroy()

    tela_cadastro = Tk()
    tela_cadastro.title("Cadastro")
    tela_cadastro.geometry("360x600")
    tela_cadastro.configure(bg=SPOTIFY_BLACK)

    Label(tela_cadastro, text="Spotify", font=("Outfit-Bold", 20),
          fg="white", bg=SPOTIFY_BLACK).pack(pady=10)

    try:
        logo = PhotoImage(file="logo.png")
        logo_menor = logo.subsample(2, 2)
        Label(tela_cadastro, image=logo_menor, bg=SPOTIFY_BLACK).pack(pady=30)
        tela_cadastro.logo = logo_menor
    except:
        pass

    Label(tela_cadastro, text="Cadastro de clientes", font=("Outfit-Bold", 20),
          fg="white", bg=SPOTIFY_BLACK).pack(pady=10)

    Label(tela_cadastro, text="Nome:", font=("Outfit-Bold", 14),
          fg="white", bg=SPOTIFY_BLACK).pack()
    Entry(tela_cadastro).pack(pady=5)

    Label(tela_cadastro, text="Email:", font=("Outfit-Bold", 14),
          fg="white", bg=SPOTIFY_BLACK).pack()
    Entry(tela_cadastro).pack(pady=5)

    botao_arredondado(tela_cadastro, "Enviar", lambda: abrir_tela_principal(tela_cadastro))

    tela_cadastro.mainloop()


def abrir_tela_principal(janela_atual=None):
    if janela_atual:
        janela_atual.destroy()

    tela_principal = Tk()
    tela_principal.title("Tela Principal")
    tela_principal.geometry("360x640")
    tela_principal.configure(bg=SPOTIFY_BLACK)

    # Cabeçalho
    Label(tela_principal, text="@usuario", font=("Outfit-Bold", 24),
          fg="white", bg=SPOTIFY_BLACK).pack(anchor="w", padx=15, pady=(15, 10))

    # Área dos cards
    frame_cards = Frame(tela_principal, bg=SPOTIFY_BLACK)
    frame_cards.pack(padx=15)

    # Linha 1 de cards
    linha1 = Frame(frame_cards, bg=SPOTIFY_BLACK)
    linha1.pack()

    try:
        batles_img = PhotoImage(file="the-beatles-ar-logo-png-transparent.png")
        batles_min=batles_img.subsample(40, 29)
        criar_card(linha1,"BEATLES", imagem=batles_min)
        linha1.batles_min = batles_min
    except:
        criar_card(linha1,"batles")

    criar_card(linha1, "Kamaitachi")

    # Linha 2 de cards
    linha2 = Frame(frame_cards, bg=SPOTIFY_BLACK)
    linha2.pack()

    try:
        Kamaitachi_img = PhotoImage(file="kamaitachi.jpg")
        Kamaitachi_min=Kamaitachi_img.subsample(20, 10)
        criar_card(linha2,"Kamaitachi", imagem=Kamaitachi_min)
        linha2.Kamaitachi_min = Kamaitachi_min
    except:
        
         criar_card(linha2, "Daily Mix 1")
    criar_card(linha2, "Daily Mix 2")

    # Seção "Picked for you"
    Label(tela_principal, text="Picked for you", font=("Outfit-Bold", 20),
          fg="white", bg=SPOTIFY_BLACK).pack(anchor="w", padx=15, pady=(20, 5))

    frame_picked = Frame(tela_principal, bg="#282828", width=330, height=90)
    frame_picked.pack(padx=15, pady=5)
    frame_picked.pack_propagate(False)

    Label(frame_picked, text="Hangovers: What Really Helps?",
          font=("Outfit-Bold", 16), fg="white", bg="#282828").pack(anchor="w", padx=10, pady=(8, 0))
    Label(frame_picked,
          text="What the science says about how to bounce back when we’ve had a few too many",
          font=("Outfit-Bold", 10), fg="#BBBBBB", bg="#282828",
          wraplength=310, justify=LEFT).pack(anchor="w", padx=10)

    # Seção "Jump back in"
    Label(tela_principal, text="Jump back in", font=("Outfit-Bold", 20),
          fg="white", bg=SPOTIFY_BLACK).pack(anchor="w", padx=15, pady=(20, 10))

    frame_jump = Frame(tela_principal, bg=SPOTIFY_BLACK)
    frame_jump.pack(padx=15)

    for i in range(3):
        c = Canvas(frame_jump, width=100, height=100, bg=SPOTIFY_BLACK, highlightthickness=0)
        create_rounded_rect(c, 2, 2, 98, 98, radius=15, fill="#282828")
        c.create_text(50, 50, text=f"Mix {i+1}", font=("Outfit-Bold", 14), fill="white")
        c.pack(side=LEFT, padx=5)

    # Barra inferior de navegação
    bottom_frame = Frame(tela_principal, bg=SPOTIFY_BLACK, height=60)
    bottom_frame.pack(side=BOTTOM, fill=X, pady=10)

    def criar_botao_nav(texto, ativo=False):
        cor = SPOTIFY_GREEN if ativo else "white"
        return Label(bottom_frame, text=texto, fg=cor, bg=SPOTIFY_BLACK, font=("Outfit-Bold", 12))

    criar_botao_nav("Home", ativo=True).pack(side=LEFT, expand=True)
    criar_botao_nav("Search").pack(side=LEFT, expand=True)
    criar_botao_nav("Your Library").pack(side=LEFT, expand=True)
    criar_botao_nav("Premium").pack(side=LEFT, expand=True)

    tela_principal.mainloop()


def abrir_tela_rede_social(janela_atual=None):
    if janela_atual:
        janela_atual.destroy()

    tela_rede = Tk()
    tela_rede.title("Rede Social")
    tela_rede.geometry("360x600")
    tela_rede.configure(bg=SPOTIFY_BLACK)

    Label(tela_rede, text="Spotify", font=("Outfit-Bold", 20),
          fg="white", bg=SPOTIFY_BLACK).pack(pady=10)

    try:
        logo = PhotoImage(file="logo.png")
        logo_menor = logo.subsample(2, 2)
        Label(tela_rede, image=logo_menor, bg=SPOTIFY_BLACK).pack(pady=30)
        tela_rede.logo = logo_menor
    except:
        pass

    Label(tela_rede, text="Bem-vindo à Rede Social", font=("Outfit-Bold", 18),
          fg="white", bg=SPOTIFY_BLACK).pack(pady=10)

    botao_arredondado(tela_rede, "Voltar", lambda: abrir_tela_principal(tela_rede))

    tela_rede.mainloop()


# --- Tela Inicial ---
principal = Tk()
principal.geometry("360x600")
principal.title("Home")
principal.configure(bg=SPOTIFY_BLACK)

Label(principal, text="Spotify", font=("Outfit-Bold", 20),
      fg="white", bg=SPOTIFY_BLACK).pack(pady=10)

try:
    logo = PhotoImage(file="logo.png")
    logo_menor = logo.subsample(2, 2)
    Label(principal, image=logo_menor, bg=SPOTIFY_BLACK).pack(pady=30)
    principal.logo = logo_menor
except:
    pass 

botao_arredondado(principal, "Cadastrar", abrir_tela_cadastro)
botao_arredondado(principal, "Login", lambda: abrir_tela_principal(principal))

principal.mainloop()
