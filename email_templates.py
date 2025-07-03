# email_templates.py
from datetime import datetime

class EmailTemplateGenerator:
    def __init__(self):
        # SVG do logo Apollo
        self.logo_image = '''placeholder'''
        
        # SVG do ícone para assinatura
        self.icon_image = '''placeholder'''

    def get_base_template(self):
        """Template HTML base responsivo"""
        return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; }}
        .container {{ max-width: 600px; margin: 0 auto; background: white; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; }}
        .header h1 {{ color: white; margin: 15px 0 0 0; font-size: 24px; font-weight: 300; }}
        .content {{ padding: 40px 35px; line-height: 1.7; color: #333; }}
        .greeting {{ font-size: 18px; font-weight: 600; color: #2c3e50; margin-bottom: 25px; }}
        .highlight {{ background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 25px; border-radius: 12px; margin: 30px 0; text-align: center; }}
        .features {{ background: #f8f9fa; border-left: 4px solid #FDAB3D; padding: 25px; margin: 25px 0; border-radius: 0 8px 8px 0; }}
        .cta {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; margin: 30px 0; border-radius: 12px; }}
        .quote {{ font-style: italic; text-align: center; color: #6c757d; padding: 20px; margin: 25px 0; border-top: 2px solid #e9ecef; }}
        .signature {{ border-top: 3px solid #FDAB3D; padding: 30px 35px; background: #f8f9fa; display: flex; align-items: center; gap: 20px; }}
        .sig-name {{ font-size: 18px; font-weight: 600; color: #2c3e50; }}
        .sig-contact {{ font-size: 13px; color: #495057; line-height: 1.5; }}
        .footer {{ background: #2c3e50; color: white; text-align: center; padding: 20px; font-size: 12px; }}
        @media (max-width: 600px) {{ .content, .signature {{ padding: 25px 20px !important; }} .signature {{ flex-direction: column; text-align: center; }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            {logo_image}
            <h1>{titulo}</h1>
        </div>
        <div class="content">{conteudo}</div>
        <div class="signature">
            <div>{icon_image}</div>
            <div>
                <div class="sig-name">{nome_remetente}</div>
                <div style="font-size: 14px; color: #6c757d; margin: 5px 0;">Consultor de Inteligência Artificial</div>
                <div class="sig-contact">
                    📧 {email_remetente}<br>
                    📱 (11) 96168-5315<br>
                    🌐 www.apolloai.com.br
                </div>
            </div>
        </div>
        <div class="footer">© {ano} Apollo AI - Transformando Educação</div>
    </div>
</body>
</html>'''

    def get_construtivista_content(self, nome_remetente, nome_escola):
        """Conteúdo para escola construtivista"""
        return f'''
        <div class="greeting">Prezados Educadores da {nome_escola},</div>
        <p>Espero que esta mensagem os encontre bem!</p>
        <p>Meu nome é <strong>{nome_remetente}</strong> e escrevo para compartilhar uma oportunidade educacional alinhada com os princípios construtivistas praticados em sua instituição.</p>
        
        <div class="highlight">
            <h2 style="margin: 0 0 15px 0;">🏗️ Educação Construtivista</h2>
            <p style="margin: 0;">Valorizamos a construção ativa do conhecimento pelo estudante</p>
        </div>
        
        <div class="features">
            <strong>Nossa abordagem construtivista:</strong>
            <ul style="margin: 15px 0 0 20px;">
                <li>Construção ativa do conhecimento pelo próprio estudante</li>
                <li>Aprendizagem colaborativa e significativa</li>
                <li>Desenvolvimento do pensamento crítico e reflexivo</li>
                <li>Contextualização dos conteúdos com a realidade</li>
            </ul>
        </div>
        
        <p>Gostaria de apresentar <strong>[SUA PROPOSTA/PROJETO/SERVIÇO]</strong>, desenvolvido para apoiar metodologias que colocam o aluno como protagonista.</p>
        
        <div class="cta">
            <p style="margin: 0 0 15px 0;">Estou à disposição para uma conversa sobre como enriquecer ainda mais o ambiente de aprendizagem!</p>
        </div>
        
        <div class="quote">
            "O conhecimento não é uma cópia da realidade, mas uma construção do ser humano."<br><strong>— Jean Piaget</strong>
        </div>
        '''

    def get_humanista_content(self, nome_remetente, nome_escola):
        """Conteúdo para escola humanista"""
        return f'''
        <div class="greeting">Caros Educadores da {nome_escola},</div>
        <p>Saudações cordiais!</p>
        <p>É com grande alegria que me dirijo a vocês, <strong>{nome_remetente}</strong>, admirador da filosofia educacional humanista de sua instituição.</p>
        
        <div class="highlight">
            <h2 style="margin: 0 0 15px 0;">🎨 Educação Humanista</h2>
            <p style="margin: 0;">Formando cidadãos éticos, conscientes e sensíveis</p>
        </div>
        
        <div class="features">
            <strong>Valores humanistas que compartilhamos:</strong>
            <ul style="margin: 15px 0 0 20px;">
                <li>Respeito à individualidade e dignidade de cada estudante</li>
                <li>Formação de cidadãos éticos e conscientes</li>
                <li>Desenvolvimento da sensibilidade e criatividade</li>
                <li>Cultivo de valores humanos universais</li>
                <li>Educação para a paz e solidariedade</li>
            </ul>
        </div>
        
        <p>Apresento <strong>[SUA PROPOSTA/PROJETO/SERVIÇO]</strong>, uma iniciativa que dialoga com os princípios humanistas de educação.</p>
        
        <div class="cta">
            <p style="margin: 0 0 15px 0;">Seria uma honra conversar sobre como formar jovens mais humanos e conscientes!</p>
        </div>
        
        <div class="quote">
            "A educação é a arma mais poderosa que você pode usar para mudar o mundo."<br><strong>— Nelson Mandela</strong>
        </div>
        '''

    def gerar_email_html(self, tipo_template, nome_remetente, nome_escola, email_remetente):
        """Gera o email HTML completo"""
        if tipo_template == "construtivista":
            conteudo = self.get_construtivista_content(nome_remetente, nome_escola)
            titulo = "Proposta Educacional Construtivista"
        else:
            conteudo = self.get_humanista_content(nome_remetente, nome_escola)
            titulo = "Parceria Educacional Humanista"
        
        return self.get_base_template().format(
            logo_image=self.logo_image,
            icon_image=self.icon_image,
            titulo=titulo,
            conteudo=conteudo,
            nome_remetente=nome_remetente,
            email_remetente=email_remetente,
            ano=datetime.now().year
        )