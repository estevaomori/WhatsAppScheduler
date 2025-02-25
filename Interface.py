import tkinter as tk
from tkinter import messagebox

class WhatsAppSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 Agendador de Mensagens - WhatsApp")
        self.root.geometry("420x400")
        self.root.resizable(False, False)
        
        # Estilos para a janela
        self.root.config(bg="#F0F0F0")
        self.create_widgets()

    def create_widgets(self):
        # Título estilizado
        title_label = tk.Label(self.root, text="📩 Agende sua mensagem", font=("Arial", 14, "bold"), bg="#F0F0F0")
        title_label.pack(pady=10)

        # Contato
        self.contato_label = tk.Label(self.root, text="Contato:", font=("Arial", 10), bg="#F0F0F0")
        self.contato_label.pack(pady=5)
        self.contato_entry = tk.Entry(self.root, font=("Arial", 10), width=40, bd=2, relief="solid")
        self.contato_entry.pack(pady=5)

        # Mensagem
        self.mensagem_label = tk.Label(self.root, text="Mensagem:", font=("Arial", 10), bg="#F0F0F0")
        self.mensagem_label.pack(pady=5)
        self.mensagem_entry = tk.Entry(self.root, font=("Arial", 10), width=40, bd=2, relief="solid")
        self.mensagem_entry.pack(pady=5)

        # Data e Hora
        self.data_hora_label = tk.Label(self.root, text="Data e Hora (YYYY-MM-DD HH:MM):", font=("Arial", 10), bg="#F0F0F0")
        self.data_hora_label.pack(pady=5)
        self.data_hora_entry = tk.Entry(self.root, font=("Arial", 10), width=40, bd=2, relief="solid")
        self.data_hora_entry.pack(pady=5)

        # Botão estilizado
        self.agendar_button = tk.Button(self.root, text="📆 Agendar", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.agendar_mensagem)
        self.agendar_button.pack(pady=15, ipadx=20, ipady=10)

    def agendar_mensagem(self):
        contato = self.contato_entry.get()
        mensagem = self.mensagem_entry.get()
        data_hora = self.data_hora_entry.get()

        if not contato or not mensagem or not data_hora:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        else:
            # Chama a função agendar_envio do arquivo scheduler.py
            from Scheduler import agendar_envio
            agendar_envio(contato, mensagem, data_hora)
            self.root.withdraw()  # Oculta a janela suavemente
