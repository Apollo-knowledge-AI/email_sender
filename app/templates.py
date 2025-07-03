# templates.py
import tkinter as tk
from tkinter import messagebox
import webbrowser
import tempfile
import os
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenderLogic:
    def __init__(self, gui):
        self.gui = gui
    
    def get_preview_text(self, sender_name, school_name, metodo_ensino, metodologia):
        """Gera texto de preview simplificado"""
        template = self.gui.template_var.get()
        
        if template == "template1":
            return f"""
ASSUNTO: Um detalhe que pode transformar ainda mais o dia a dia da {school_name}

Olá, equipe da {school_name}!

O {metodo_ensino} entrega uma base sólida de conteúdo, mas o que realmente 
transforma a sala de aula é o que acontece entre as linhas — no vínculo com o aluno.

💝 PRESENÇA AFETIVA NO ENSINO
Temos observado um movimento bonito em escolas que estão resgatando 
essa presença afetiva no ensino.

Nosso trabalho nasce justamente desse sonho: fortalecer essa ponte 
entre professor e aluno.

Será que essa conversa também faz sentido por aí?

{sender_name}
Consultor Educacional - Apollo AI
            """
        elif template == "template2":
            return f"""
ASSUNTO: E se o engajamento dos alunos da {school_name} pudesse ir ainda além?

Oi, pessoal!

Sabemos como a {school_name} se dedica à excelência — o {metodologia} já é 
um passo firme nessa direção.

🚀 PRÓXIMO SALTO DA EDUCAÇÃO
Mas e se os professores conseguissem atingir os alunos de forma ainda 
mais direta, emocional e transformadora?

A gente acredita que o próximo salto da educação está na conexão, 
não só na instrução.

Estamos aqui pra caminhar junto nessa visão.

{sender_name}
Consultor Educacional - Apollo AI
            """
        elif template == "template3":
            return f"""
ASSUNTO: O que diferencia as escolas que marcam gerações?

Olá, tudo bem por aí?

Algumas escolas seguem o currículo à risca, mas outras deixam marcas 
que os alunos levam pra vida inteira.

⭐ ESCOLAS QUE MARCAM GERAÇÕES
A {school_name} já é uma referência — e talvez esteja na hora de 
fortalecer ainda mais esse diferencial.

Hoje, quem se destaca não é só quem ensina mais, mas quem cria 
relações mais fortes.

Será que conseguimos sonhar esse próximo passo juntos?

{sender_name}
Consultor Educacional - Apollo AI
            """
        else:  # template4
            return f"""
ASSUNTO: Quando a relação esfria, nem o melhor conteúdo segura o aluno

Oi, pessoal da {school_name}!

Mesmo com um sistema robusto como o {metodologia}, a gente sabe que às 
vezes o aluno se desconecta — e o professor sente isso.

🛡️ PROTEGENDO O VÍNCULO ESSENCIAL
Essa distância silenciosa, quando cresce, cobra um preço alto no 
engajamento e nos resultados.

A gente acredita que dá pra evitar esse afastamento com gestos 
pequenos, mas consistentes.

Talvez possamos conversar sobre como proteger esse vínculo tão essencial.

{sender_name}
Consultor Educacional - Apollo AI
            """
    
    def update_preview(self):
        """Atualiza o preview do email"""
        sender_name = self.gui.sender_name_entry.get().strip() or "[Seu Nome]"
        school_name = self.gui.school_name_entry.get().strip() or "[Nome da Escola]"
        metodo_ensino = self.gui.metodo_ensino_entry.get().strip() or "[Método de Ensino]"
        metodologia = self.gui.metodologia_entry.get().strip() or "[Metodologia]"
        
        preview_content = self.get_preview_text(sender_name, school_name, metodo_ensino, metodologia)
        
        self.gui.preview_text.config(state='normal')
        self.gui.preview_text.delete(1.0, tk.END)
        self.gui.preview_text.insert(1.0, preview_content)
        self.gui.preview_text.config(state='disabled')
    
    def preview_in_browser(self):
        """Abre preview completo no navegador"""
        sender_name = self.gui.sender_name_entry.get().strip() or "Consultor Apollo"
        school_name = self.gui.school_name_entry.get().strip() or "Escola Exemplo"
        sender_email = self.gui.sender_email_entry.get().strip() or "consultor@apolloeducacional.com"
        metodo_ensino = self.gui.metodo_ensino_entry.get().strip() or "Método Tradicional"
        metodologia = self.gui.metodologia_entry.get().strip() or "Metodologia Ativa"
        
        try:
            # Gerar HTML completo
            html_content = self.gui.template_generator.gerar_email_html(
                self.gui.template_var.get(), sender_name, school_name, sender_email, metodo_ensino, metodologia
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
        sender_name = self.gui.sender_name_entry.get().strip()
        sender_email = self.gui.sender_email_entry.get().strip()
        sender_password = self.gui.sender_password_entry.get().strip()
        school_name = self.gui.school_name_entry.get().strip()
        school_email = self.gui.school_email_entry.get().strip()
        
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
            # Obter método e metodologia
            metodo_ensino = self.gui.metodo_ensino_entry.get().strip() or "Método Tradicional"
            metodologia = self.gui.metodologia_entry.get().strip() or "Metodologia Ativa"
            
            # Gerar HTML do email
            html_body = self.gui.template_generator.gerar_email_html(
                self.gui.template_var.get(), sender_name, school_name, sender_email, metodo_ensino, metodologia
            )
            
            # Criar mensagem
            msg = MIMEMultipart('alternative')
            msg['From'] = sender_email
            msg['To'] = school_email
            
            # Definir assunto baseado no template
            template = self.gui.template_var.get()
            if template == "template1":
                msg['Subject'] = f"Um detalhe que pode transformar ainda mais o dia a dia da {school_name}"
            elif template == "template2":
                msg['Subject'] = f"E se o engajamento dos alunos da {school_name} pudesse ir ainda além?"
            elif template == "template3":
                msg['Subject'] = "O que diferencia as escolas que marcam gerações?"
            elif template == "template4":
                msg['Subject'] = "Quando a relação esfria, nem o melhor conteúdo segura o aluno"
            else:
                msg['Subject'] = f"Proposta Educacional para {school_name}"
            
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
            
            # Mapear nomes dos templates para exibição
            template_names = {
                "template1": "Template 1 - Presença Afetiva",
                "template2": "Template 2 - Engajamento Avançado", 
                "template3": "Template 3 - Escolas que Marcam",
                "template4": "Template 4 - Protegendo Vínculos"
            }
            
            template_display = template_names.get(self.gui.template_var.get(), "Template Personalizado")
            
            messagebox.showinfo("✅ Sucesso!", 
                               f"Email enviado com sucesso para {school_name}!\n\n"
                               f"Template: {template_display}\n"
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
    
    def save_credentials(self):
        """Salva as credenciais em arquivo .env"""
        name = self.gui.sender_name_entry.get().strip()
        email = self.gui.sender_email_entry.get().strip()
        password = self.gui.sender_password_entry.get().strip()
        
        if not name or not email or not password:
            messagebox.showwarning("⚠️ Aviso", "Por favor, preencha nome, email e senha antes de salvar!")
            return
        
        try:
            # Criar conteúdo do arquivo .env
            env_content = f"""# Credenciais do Apollo AI Email Sender
# Arquivo gerado automaticamente - Não compartilhe este arquivo!

NAME={name}
EMAIL={email}
PASSWORD={password}

# Configurações adicionais
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
"""
            
            # Salvar arquivo .env
            with open('.env', 'w', encoding='utf-8') as f:
                f.write(env_content)
            
            messagebox.showinfo("✅ Sucesso!", 
                               f"Credenciais salvas com sucesso!\n\n"
                               f"Nome: {name}\n"
                               f"Email: {email}\n"
                               f"Arquivo: .env\n\n"
                               f"⚠️ Importante: Mantenha este arquivo seguro e não o compartilhe!")
            
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro ao salvar credenciais:\n{str(e)}")
    
    def load_credentials(self):
        """Carrega credenciais do arquivo .env se existir"""
        try:
            if os.path.exists('.env'):
                with open('.env', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                name = ""
                email = ""
                password = ""
                
                for line in lines:
                    line = line.strip()
                    if line.startswith('NAME=') and not line.startswith('#'):
                        name = line.split('=', 1)[1]
                    elif line.startswith('EMAIL=') and not line.startswith('#'):
                        email = line.split('=', 1)[1]
                    elif line.startswith('PASSWORD=') and not line.startswith('#'):
                        password = line.split('=', 1)[1]
                
                if name and email and password:
                    self.gui.sender_name_entry.delete(0, tk.END)
                    self.gui.sender_name_entry.insert(0, name)
                    
                    self.gui.sender_email_entry.delete(0, tk.END)
                    self.gui.sender_email_entry.insert(0, email)
                    
                    self.gui.sender_password_entry.delete(0, tk.END)
                    self.gui.sender_password_entry.insert(0, password)
                    
                    print("✅ Credenciais carregadas do arquivo .env")
                    
        except Exception as e:
            print(f"⚠️ Erro ao carregar credenciais: {str(e)}")
    
    def load_credentials_manual(self):
        """Carrega credenciais manualmente do arquivo .env"""
        try:
            if not os.path.exists('.env'):
                messagebox.showinfo("ℹ️ Informação", 
                                   "Arquivo .env não encontrado!\n\n"
                                   "Para criar um arquivo .env:\n"
                                   "1. Preencha nome, email e senha\n"
                                   "2. Clique em 'Salvar Credenciais'\n"
                                   "3. Ou copie o arquivo env_example.txt para .env")
                return
            
            with open('.env', 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            name = ""
            email = ""
            password = ""
            
            for line in lines:
                line = line.strip()
                if line.startswith('NAME=') and not line.startswith('#'):
                    name = line.split('=', 1)[1]
                elif line.startswith('EMAIL=') and not line.startswith('#'):
                    email = line.split('=', 1)[1]
                elif line.startswith('PASSWORD=') and not line.startswith('#'):
                    password = line.split('=', 1)[1]
            
            if name and email and password:
                self.gui.sender_name_entry.delete(0, tk.END)
                self.gui.sender_name_entry.insert(0, name)
                
                self.gui.sender_email_entry.delete(0, tk.END)
                self.gui.sender_email_entry.insert(0, email)
                
                self.gui.sender_password_entry.delete(0, tk.END)
                self.gui.sender_password_entry.insert(0, password)
                
                messagebox.showinfo("✅ Sucesso!", 
                                   f"Credenciais carregadas com sucesso!\n\n"
                                   f"Nome: {name}\n"
                                   f"Email: {email}\n"
                                   f"Senha: {'*' * len(password)}")
            else:
                messagebox.showwarning("⚠️ Aviso", 
                                      "Credenciais não encontradas no arquivo .env!\n\n"
                                      "Verifique se o arquivo contém:\n"
                                      "NAME=seu_nome\n"
                                      "EMAIL=seu_email\n"
                                      "PASSWORD=sua_senha")
                
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro ao carregar credenciais:\n{str(e)}")
