import os
from tkinter.filedialog import askdirectory

diretorio = askdirectory(title="Selecione uma pasta")

lista_de_arquivos = os.listdir(diretorio)

locais={
    "imagens":[".png", ".jpeg", ".jpg", ".jfif", ".gif", ".bmp", ".webp"],
    "documentos":[".docx",".doc"],
    "powerpoint":["."],
    "arquivos html":[".html"],
    "audios":[".mp3"],
    "videos":[".mp4", ".wmv"],
    "planilhas":[".xlsx", ".xlsm"],
    "arquivos rar":[".rar",".zip"],
    "pdfs":[".pdf"],
    "atalhos":[".exe", ".bat"],
}

for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(f"{diretorio}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{diretorio}/{pasta}"):
                os.mkdir(f"{diretorio}/{pasta}")
            os.rename(f"{diretorio}/{arquivo}",f"{diretorio}/{pasta}/{arquivo}")

