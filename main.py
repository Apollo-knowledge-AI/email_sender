# email_sender.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import webbrowser
import tempfile
import os

# Importar o módulo de templates
from email_templates import EmailTemplateGenerator

class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Envio de Emails - Apollo AI")
        self.root.configure(bg='#f0f0f0')
        
        # Inicializar gerador de templates
        self.template_generator = EmailTemplateGenerator()
        
        # Variáveis
        self.template_var = tk.StringVar(value="construtivista")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Título principal
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="📧 Apollo AI - Sistema de Emails", 
                              font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Envio de propostas educacionais com templates profissionais", 
                                 font=('Arial', 10), bg='#f0f0f0', fg='#6c757d')
        subtitle_label.pack()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=30, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Seção dados do remetente
        sender_frame = tk.LabelFrame(main_frame, text="📤 Dados do Remetente", 
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
        
        # Seção escola destinatária
        school_frame = tk.LabelFrame(main_frame, text="🏫 Escola Destinatária", 
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
        
        # Seção template
        template_frame = tk.LabelFrame(main_frame, text="🎨 Selecionar Template", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        template_frame.pack(fill='x', pady=(0, 15))
        
        template_info_frame = tk.Frame(template_frame, bg='#f0f0f0')
        template_info_frame.pack(fill='x', padx=10, pady=10)
        
        # Templates
        construtivista_radio = tk.Radiobutton(template_info_frame, 
                                            text="🏗️ Escola Construtivista", 
                                            variable=self.template_var, value="construtivista",
                                            font=('Arial', 11), bg='#f0f0f0', 
                                            command=self.update_preview)
        construtivista_radio.pack(anchor='w', pady=3)
        
        tk.Label(template_info_frame, text="     → Foco na construção ativa do conhecimento e protagonismo estudantil", 
                font=('Arial', 9), bg='#f0f0f0', fg='#6c757d').pack(anchor='w')
        
        humanista_radio = tk.Radiobutton(template_info_frame, 
                                       text="🎨 Escola Humanista", 
                                       variable=self.template_var, value="humanista",
                                       font=('Arial', 11), bg='#f0f0f0',
                                       command=self.update_preview)
        humanista_radio.pack(anchor='w', pady=(10, 3))
        
        tk.Label(template_info_frame, text="     → Ênfase em valores humanos, ética e desenvolvimento integral", 
                font=('Arial', 9), bg='#f0f0f0', fg='#6c757d').pack(anchor='w')
        
        # Preview
        preview_frame = tk.LabelFrame(main_frame, text="👁️ Preview do Email", 
                                    font=('Arial', 12, 'bold'), bg='#f0f0f0', fg='#34495e')
        preview_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        self.preview_text = scrolledtext.ScrolledText(preview_frame, height=8, 
                                                    font=('Arial', 9), state='disabled',
                                                    wrap=tk.WORD)
        self.preview_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Botões
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x')
        
        preview_btn = tk.Button(button_frame, text="🔄 Atualizar Preview", 
                              command=self.update_preview, font=('Arial', 10),
                              bg='#3498db', fg='white', cursor='hand2', relief='flat',
                              padx=15, pady=8)
        preview_btn.pack(side='left', padx=(0, 10))
        
        browser_btn = tk.Button(button_frame, text="🌐 Ver no Navegador", 
                              command=self.preview_in_browser, font=('Arial', 10),
                              bg='#9b59b6', fg='white', cursor='hand2', relief='flat',
                              padx=15, pady=8)
        browser_btn.pack(side='left', padx=(0, 10))
        
        send_btn = tk.Button(button_frame, text="📤 Enviar Email", 
                           command=self.send_email, font=('Arial', 11, 'bold'),
                           bg='#27ae60', fg='white', cursor='hand2', relief='flat',
                           padx=20, pady=8)
        send_btn.pack(side='right')
        
        # Preview inicial
        self.update_preview()
    
    def get_preview_text(self, sender_name, school_name):
        """Gera texto de preview simplificado"""
        if self.template_var.get() == "construtivista":
            return f"""
ASSUNTO: Proposta Educacional Construtivista para {school_name}

Prezados Educadores da {school_name},

Meu nome é {sender_name} e escrevo para compartilhar uma oportunidade 
educacional alinhada com os princípios construtivistas.

🏗️ EDUCAÇÃO CONSTRUTIVISTA
• Construção ativa do conhecimento pelo estudante
• Aprendizagem colaborativa e significativa  
• Desenvolvimento do pensamento crítico
• Contextualização com a realidade

Gostaria de apresentar [SUA PROPOSTA], desenvolvida para apoiar 
metodologias que colocam o aluno como protagonista.

"O conhecimento não é uma cópia da realidade, mas uma 
construção do ser humano." — Jean Piaget

Atenciosamente,
{sender_name}
Consultor Educacional - Apollo Educacional
            """
        else:
            return f"""
ASSUNTO: Parceria Educacional Humanista para {school_name}

Caros Educadores da {school_name},

É com alegria que me dirijo a vocês, {sender_name}, admirador da 
filosofia educacional humanista de sua instituição.

🎨 EDUCAÇÃO HUMANISTA
• Respeito à individualidade e dignidade
• Formação de cidadãos éticos e conscientes
• Desenvolvimento da sensibilidade e criatividade
• Cultivo de valores humanos universais

Apresento [SUA PROPOSTA], uma iniciativa que dialoga com os 
princípios humanistas de educação.

"A educação é a arma mais poderosa que você pode usar 
para mudar o mundo." — Nelson Mandela

Com admiração,
{sender_name}
Consultor Educacional - Apollo Educacional
            """
    
    def update_preview(self):
        """Atualiza o preview do email"""
        sender_name = self.sender_name_entry.get().strip() or "[Seu Nome]"
        school_name = self.school_name_entry.get().strip() or "[Nome da Escola]"
        
        preview_content = self.get_preview_text(sender_name, school_name)
        
        self.preview_text.config(state='normal')
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(1.0, preview_content)
        self.preview_text.config(state='disabled')
    
    def preview_in_browser(self):
        """Abre preview completo no navegador"""
        sender_name = self.sender_name_entry.get().strip() or "Consultor Apollo"
        school_name = self.school_name_entry.get().strip() or "Escola Exemplo"
        sender_email = self.sender_email_entry.get().strip() or "consultor@apolloeducacional.com"
        
        try:
            # Gerar HTML completo
            html_content = self.template_generator.gerar_email_html(
                self.template_var.get(), sender_name, school_name, sender_email
            )
            
            # Salvar em arquivo temporário
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
                f.write(html_content)
                temp_file = f.name
            
            # Abrir no navegador
            webbrowser.open('file://' + temp_file)
            
            messagebox.showinfo("Preview", "Email aberto no navegador para visualização completa!")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar preview: {str(e)}")
    
    def validate_email(self, email):
        """Valida formato do email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def send_email(self):
        """Envia o email com template HTML"""
        # Validar campos
        sender_name = self.sender_name_entry.get().strip()
        sender_email = self.sender_email_entry.get().strip()
        sender_password = self.sender_password_entry.get().strip()
        school_name = self.school_name_entry.get().strip()
        school_email = self.school_email_entry.get().strip()
        
        if not all([sender_name, sender_email, sender_password, school_name, school_email]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
        
        if not self.validate_email(sender_email):
            messagebox.showerror("Erro", "Email do remetente inválido!")
            return
        
        if not self.validate_email(school_email):
            messagebox.showerror("Erro", "Email da escola inválido!")
            return
        
        try:
            # Gerar HTML do email
            html_body = self.template_generator.gerar_email_html(
                self.template_var.get(), sender_name, school_name, sender_email
            )
            
            # Criar mensagem
            msg = MIMEMultipart('alternative')
            msg['From'] = sender_email
            msg['To'] = school_email
            
            if self.template_var.get() == "construtivista":
                msg['Subject'] = f"Proposta Educacional Construtivista para {school_name}"
            else:
                msg['Subject'] = f"Parceria Educacional Humanista para {school_name}"
            
            # Anexar HTML
            html_part = MIMEText(html_body, 'html', 'utf-8')
            msg.attach(html_part)
            
            # Configurar SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            
            # Enviar
            server.sendmail(sender_email, school_email, msg.as_string())
            server.quit()
            
            messagebox.showinfo("✅ Sucesso!", 
                               f"Email enviado com sucesso para {school_name}!\n\n"
                               f"Template: {self.template_var.get().title()}\n"
                               f"Destinatário: {school_email}")
            
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("❌ Erro de Autenticação", 
                               "Falha na autenticação do email.\n\n"
                               "💡 Dica para Gmail:\n"
                               "• Use uma 'Senha de App' em vez da senha normal\n"
                               "• Ative a autenticação de 2 fatores\n"
                               "• Acesse: Conta Google > Segurança > Senhas de app")
        except smtplib.SMTPException as e:
            messagebox.showerror("❌ Erro SMTP", f"Erro ao enviar email:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro inesperado:\n{str(e)}")

def main():
    """Função principal"""
    root = tk.Tk()
    app = EmailSenderApp(root)
    
    # Configurar ícone da janela (opcional)
    try:
        root.iconphoto(False, tk.PhotoImage(data=''))  # Pode adicionar ícone aqui
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()