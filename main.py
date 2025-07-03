# main.py
import tkinter as tk
from app.gui import EmailSenderGUI

def main():
    """Função principal"""
    root = tk.Tk()
    app = EmailSenderGUI(root)
    
    # Configurar ícone da janela (opcional)
    try:
        root.iconphoto(False, tk.PhotoImage(data=''))  # Pode adicionar ícone aqui
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()