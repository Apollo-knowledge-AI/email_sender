# email_templates.py
from datetime import datetime

class EmailTemplateGenerator:
    def __init__(self):
        # SVG do logo Apollo
        self.logo_image = 'image/logomarca.png'
        
        # SVG do ícone para assinatura
        self.icon_image = 'image/icon.png'

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

    def get_template_1_content(self, nome_remetente, nome_escola, metodo_ensino):
        """Template 1: Um detalhe que pode transformar ainda mais o dia a dia"""
        return f'''
        <div class="greeting">Olá, equipe da {nome_escola}!</div>
        
        <p>O <strong>{metodo_ensino}</strong> entrega uma base sólida de conteúdo, mas o que realmente transforma a sala de aula é o que acontece entre as linhas — no vínculo com o aluno.</p>
        
        <div class="highlight">
            <h2 style="margin: 0 0 15px 0;">💝 Presença Afetiva no Ensino</h2>
            <p style="margin: 0;">Temos observado um movimento bonito em escolas que estão resgatando essa presença afetiva no ensino.</p>
        </div>
        
        <p>Nosso trabalho nasce justamente desse sonho: <strong>fortalecer essa ponte entre professor e aluno</strong>.</p>
        
        <div class="cta">
            <p style="margin: 0 0 15px 0;">Será que essa conversa também faz sentido por aí?</p>
        </div>
        
        <div class="quote">
            "A educação não é preparação para a vida; a educação é a própria vida."<br><strong>— John Dewey</strong>
        </div>
        '''

    def get_template_2_content(self, nome_remetente, nome_escola, metodologia):
        """Template 2: E se o engajamento dos alunos pudesse ir ainda além?"""
        return f'''
        <div class="greeting">Oi, pessoal!</div>
        
        <p>Sabemos como a <strong>{nome_escola}</strong> se dedica à excelência — o <strong>{metodologia}</strong> já é um passo firme nessa direção.</p>
        
        <div class="highlight">
            <h2 style="margin: 0 0 15px 0;">🚀 Próximo Salto da Educação</h2>
            <p style="margin: 0;">Mas e se os professores conseguissem atingir os alunos de forma ainda mais direta, emocional e transformadora?</p>
        </div>
        
        <p>A gente acredita que o próximo salto da educação está na <strong>conexão, não só na instrução</strong>.</p>
        
        <div class="cta">
            <p style="margin: 0 0 15px 0;">Estamos aqui pra caminhar junto nessa visão.</p>
        </div>
        
        <div class="quote">
            "O professor medíocre conta. O bom professor explica. O professor superior demonstra. O grande professor inspira."<br><strong>— William Arthur Ward</strong>
        </div>
        '''

    def get_template_3_content(self, nome_remetente, nome_escola):
        """Template 3: O que diferencia as escolas que marcam gerações?"""
        return f'''
        <div class="greeting">Olá, tudo bem por aí?</div>
        
        <p>Algumas escolas seguem o currículo à risca, mas outras deixam marcas que os alunos levam pra vida inteira.</p>
        
        <div class="highlight">
            <h2 style="margin: 0 0 15px 0;">⭐ Escolas que Marcam Gerações</h2>
            <p style="margin: 0;">A <strong>{nome_escola}</strong> já é uma referência — e talvez esteja na hora de fortalecer ainda mais esse diferencial.</p>
        </div>
        
        <p>Hoje, quem se destaca não é só quem ensina mais, mas quem cria <strong>relações mais fortes</strong>.</p>
        
        <div class="cta">
            <p style="margin: 0 0 15px 0;">Será que conseguimos sonhar esse próximo passo juntos?</p>
        </div>
        
        <div class="quote">
            "A educação é o passaporte para o futuro, pois o amanhã pertence àqueles que se preparam para ele hoje."<br><strong>— Malcolm X</strong>
        </div>
        '''

    def get_template_4_content(self, nome_remetente, nome_escola, metodologia):
        """Template 4: Quando a relação esfria, nem o melhor conteúdo segura o aluno"""
        return f'''
        <div class="greeting">Oi, pessoal da {nome_escola}!</div>
        
        <p>Mesmo com um sistema robusto como o <strong>{metodologia}</strong>, a gente sabe que às vezes o aluno se desconecta — e o professor sente isso.</p>
        
        <div class="highlight">
            <h2 style="margin: 0 0 15px 0;">🛡️ Protegendo o Vínculo Essencial</h2>
            <p style="margin: 0;">Essa distância silenciosa, quando cresce, cobra um preço alto no engajamento e nos resultados.</p>
        </div>
        
        <p>A gente acredita que dá pra evitar esse afastamento com <strong>gestos pequenos, mas consistentes</strong>.</p>
        
        <div class="cta">
            <p style="margin: 0 0 15px 0;">Talvez possamos conversar sobre como proteger esse vínculo tão essencial.</p>
        </div>
        
        <div class="quote">
            "O relacionamento é a base de todo aprendizado significativo."<br><strong>— Rita Pierson</strong>
        </div>
        '''

    def gerar_email_html(self, tipo_template, nome_remetente, nome_escola, email_remetente, metodo_ensino="", metodologia=""):
        """Gera o email HTML completo"""
        if tipo_template == "template1":
            conteudo = self.get_template_1_content(nome_remetente, nome_escola, metodo_ensino)
            titulo = f"Um detalhe que pode transformar ainda mais o dia a dia da {nome_escola}"
        elif tipo_template == "template2":
            conteudo = self.get_template_2_content(nome_remetente, nome_escola, metodologia)
            titulo = f"E se o engajamento dos alunos da {nome_escola} pudesse ir ainda além?"
        elif tipo_template == "template3":
            conteudo = self.get_template_3_content(nome_remetente, nome_escola)
            titulo = "O que diferencia as escolas que marcam gerações?"
        elif tipo_template == "template4":
            conteudo = self.get_template_4_content(nome_remetente, nome_escola, metodologia)
            titulo = "Quando a relação esfria, nem o melhor conteúdo segura o aluno"
        else:
            # Fallback para template1
            conteudo = self.get_template_1_content(nome_remetente, nome_escola, metodo_ensino)
            titulo = f"Um detalhe que pode transformar ainda mais o dia a dia da {nome_escola}"
        
        return self.get_base_template().format(
            logo_image=self.logo_image,
            icon_image=self.icon_image,
            titulo=titulo,
            conteudo=conteudo,
            nome_remetente=nome_remetente,
            email_remetente=email_remetente,
            ano=datetime.now().year
        )