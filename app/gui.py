# gui.py
import tkinter as tk
from tkinter import ttk, scrolledtext

from .base_email import EmailTemplateGenerator
from .templates import EmailSenderLogic

class EmailSenderGUI:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        
    def setup_window(self):
        """Configura a janela principal"""
        self.root.title("Sistema de Envio de Emails - Nerd-o AI")
        self.root.configure(bg='#f0f0f0')
        
        # Configurar tamanho da janela
        self.root.geometry("800x700")
        self.root.minsize(700, 600)
        
        # Centralizar a janela
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def setup_variables(self):
        """Configura as variáveis da interface"""
        # Inicializar gerador de templates
        self.template_generator = EmailTemplateGenerator()
        
        # Inicializar lógica de negócio
        self.logic = EmailSenderLogic(self)
        
        # Variáveis
        self.template_var = tk.StringVar(value="template1")
        self.metodo_ensino_var = tk.StringVar(value="")
        self.metodologia_var = tk.StringVar(value="")
        
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        self.create_title_section()
        self.create_scrollable_area()
        self.create_sender_section()
        self.create_school_section()
        self.create_method_section()
        self.create_template_section()
        self.create_preview_section()
        self.create_button_section()
        
        # Preview inicial e carregar credenciais
        self.logic.update_preview()
        self.logic.load_credentials()
    
    def create_title_section(self):
        """Cria a seção do título"""
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="📧 Nerd-o - Sistema de Emails", 
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Envio de propostas educacionais com templates profissionais", 
                                 font=('Arial', 10), bg='#f0f0f0', fg='#6c757d')
        subtitle_label.pack()
    
    def create_scrollable_area(self):
        """Cria a área com scrollbar"""
        # Criar canvas com scrollbar
        self.canvas = tk.Canvas(self.root, bg='#f0f0f0', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#f0f0f0')
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Frame principal dentro do canvas
        self.main_frame = tk.Frame(self.scrollable_frame, bg='#f0f0f0', padx=30, pady=20)
        self.main_frame.pack(expand=True, fill='both')
        
        # Configurar scroll com mouse
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Empacotar canvas e scrollbar
        self.canvas.pack(side="left", fill="both", expand=True, padx=(0, 5))
        self.scrollbar.pack(side="right", fill="y")
        
        # Configurar canvas para redimensionar
        def configure_scroll_region(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        self.scrollable_frame.bind("<Configure>", configure_scroll_region)
    
    def create_sender_section(self):
        """Cria a seção de dados do remetente"""
        sender_frame = tk.LabelFrame(self.main_frame, text="📤 Dados do Remetente", 
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        sender_frame.pack(fill='x', pady=(0, 15))
        
        # Nome
        tk.Label(sender_frame, text="Seu Nome:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=0, column=0, sticky='w', padx=10, pady=8)
        self.sender_name_entry = tk.Entry(sender_frame, font=('Arial', 10), width=45)
        self.sender_name_entry.grid(row=0, column=1, padx=10, pady=8)
        
        # Email
        tk.Label(sender_frame, text="Seu Email:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=1, column=0, sticky='w', padx=10, pady=8)
        self.sender_email_entry = tk.Entry(sender_frame, font=('Arial', 10), width=45)
        self.sender_email_entry.grid(row=1, column=1, padx=10, pady=8)
        
        # Senha
        tk.Label(sender_frame, text="Senha do Email:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=2, column=0, sticky='w', padx=10, pady=8)
        self.sender_password_entry = tk.Entry(sender_frame, font=('Arial', 10), width=45, show='*')
        self.sender_password_entry.grid(row=2, column=1, padx=10, pady=8)
        
        # Botão para salvar credenciais
        save_credentials_btn = tk.Button(sender_frame, text="💾 Salvar Credenciais", 
                                       command=self.logic.save_credentials, font=('Arial', 9),
                                       bg='#17a2b8', fg='white', cursor='hand2', relief='flat',
                                       padx=10, pady=5)
        save_credentials_btn.grid(row=2, column=2, padx=(10, 0), pady=8)
        
        # Botão para carregar credenciais
        load_credentials_btn = tk.Button(sender_frame, text="📂 Carregar Credenciais", 
                                       command=self.logic.load_credentials_manual, font=('Arial', 9),
                                       bg='#28a745', fg='white', cursor='hand2', relief='flat',
                                       padx=10, pady=5)
        load_credentials_btn.grid(row=3, column=2, padx=(10, 0), pady=8)
    
    def create_school_section(self):
        """Cria a seção da escola destinatária"""
        school_frame = tk.LabelFrame(self.main_frame, text="🏫 Escola Destinatária", 
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        school_frame.pack(fill='x', pady=(0, 15))
        
        # Nome da escola
        tk.Label(school_frame, text="Nome da Escola:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=0, column=0, sticky='w', padx=10, pady=8)
        self.school_name_entry = tk.Entry(school_frame, font=('Arial', 10), width=45)
        self.school_name_entry.grid(row=0, column=1, padx=10, pady=8)
        
        # Email da escola
        tk.Label(school_frame, text="Email da Escola:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=1, column=0, sticky='w', padx=10, pady=8)
        self.school_email_entry = tk.Entry(school_frame, font=('Arial', 10), width=45)
        self.school_email_entry.grid(row=1, column=1, padx=10, pady=8)
    
    def create_method_section(self):
        """Cria a seção de método/metodologia"""
        method_frame = tk.LabelFrame(self.main_frame, text="📚 Método/Metodologia da Escola", 
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        method_frame.pack(fill='x', pady=(0, 15))
        
        # Método de ensino
        tk.Label(method_frame, text="Método de Ensino:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=0, column=0, sticky='w', padx=10, pady=8)
        self.metodo_ensino_entry = tk.Entry(method_frame, font=('Arial', 10), width=45)
        self.metodo_ensino_entry.grid(row=0, column=1, padx=10, pady=8)
        
        # Metodologia
        tk.Label(method_frame, text="Metodologia:", font=('Arial', 10), 
                bg='#f0f0f0').grid(row=1, column=0, sticky='w', padx=10, pady=8)
        self.metodologia_entry = tk.Entry(method_frame, font=('Arial', 10), width=45)
        self.metodologia_entry.grid(row=1, column=1, padx=10, pady=8)
    
    def create_template_section(self):
        """Cria a seção de seleção de template"""
        template_frame = tk.LabelFrame(self.main_frame, text="🎨 Selecionar Template", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        template_frame.pack(fill='x', pady=(0, 15))
        
        template_info_frame = tk.Frame(template_frame, bg='#f0f0f0')
        template_info_frame.pack(fill='x', padx=10, pady=10)
        
        # Templates
        template1_radio = tk.Radiobutton(template_info_frame, 
                                       text="💝 Template 1 - Presença Afetiva", 
                                       variable=self.template_var, value="template1",
                                       font=('Arial', 11), bg='#f0f0f0', 
                                       command=self.logic.update_preview)
        template1_radio.pack(anchor='w', pady=3)
        
        tk.Label(template_info_frame, text="     → Foco no vínculo entre professor e aluno", 
                font=('Arial', 9), bg='#f0f0f0', fg='#6c757d').pack(anchor='w')
        
        template2_radio = tk.Radiobutton(template_info_frame, 
                                       text="🚀 Template 2 - Engajamento Avançado", 
                                       variable=self.template_var, value="template2",
                                       font=('Arial', 11), bg='#f0f0f0',
                                       command=self.logic.update_preview)
        template2_radio.pack(anchor='w', pady=(10, 3))
        
        tk.Label(template_info_frame, text="     → Conexão emocional e transformadora", 
                font=('Arial', 9), bg='#f0f0f0', fg='#6c757d').pack(anchor='w')
        
        template3_radio = tk.Radiobutton(template_info_frame, 
                                       text="⭐ Template 3 - Escolas que Marcam", 
                                       variable=self.template_var, value="template3",
                                       font=('Arial', 11), bg='#f0f0f0',
                                       command=self.logic.update_preview)
        template3_radio.pack(anchor='w', pady=(10, 3))
        
        tk.Label(template_info_frame, text="     → Diferencial e legado educacional", 
                font=('Arial', 9), bg='#f0f0f0', fg='#6c757d').pack(anchor='w')
        
        template4_radio = tk.Radiobutton(template_info_frame, 
                                       text="🛡️ Template 4 - Protegendo Vínculos", 
                                       variable=self.template_var, value="template4",
                                       font=('Arial', 11), bg='#f0f0f0',
                                       command=self.logic.update_preview)
        template4_radio.pack(anchor='w', pady=(10, 3))
        
        tk.Label(template_info_frame, text="     → Evitando desconexão dos alunos", 
                font=('Arial', 9), bg='#f0f0f0', fg='#6c757d').pack(anchor='w')
    
    def create_preview_section(self):
        """Cria a seção de preview"""
        preview_frame = tk.LabelFrame(self.main_frame, text="👁️ Preview do Email", 
                                    font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        preview_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        self.preview_text = scrolledtext.ScrolledText(preview_frame, height=8, 
                                                    font=('Arial', 9), state='disabled',
                                                    wrap=tk.WORD)
        self.preview_text.pack(fill='both', expand=True, padx=10, pady=10)
    
    def create_button_section(self):
        """Cria a seção de botões"""
        button_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x')
        
        preview_btn = tk.Button(button_frame, text="🔄 Atualizar Preview", 
                              command=self.logic.update_preview, font=('Arial', 10),
                              bg='#3498db', fg='white', cursor='hand2', relief='flat',
                              padx=15, pady=8)
        preview_btn.pack(side='left', padx=(0, 10))
        
        browser_btn = tk.Button(button_frame, text="🌐 Ver no Navegador", 
                              command=self.logic.preview_in_browser, font=('Arial', 10),
                              bg='#9b59b6', fg='white', cursor='hand2', relief='flat',
                              padx=15, pady=8)
        browser_btn.pack(side='left', padx=(0, 10))
        
        send_btn = tk.Button(button_frame, text="📤 Enviar Email", 
                           command=self.logic.send_email, font=('Arial', 11, 'bold'),
                           bg='#27ae60', fg='white', cursor='hand2', relief='flat',
                           padx=20, pady=8)
        send_btn.pack(side='right')
