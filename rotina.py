import webbrowser
import subprocess

def abrir_spotify():
    # Verifica se o Spotify está em execução
    output = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq Spotify.exe'], capture_output=True, text=True)
    if 'Spotify.exe' in output.stdout:
        # O Spotify está em execução, abre o aplicativo
        webbrowser.open("spotify:")
    else:
        print("O Spotify não está em execução no seu computador.")

def abrir_canal_noticias():
    # Insira a URL do canal de notícias que você deseja abrir
    url = "https://g1.globo.com/sp/campinas-regiao/"
    webbrowser.open(url)

# Chamada das funções ao ligar o computador
abrir_spotify()
abrir_canal_noticias()
