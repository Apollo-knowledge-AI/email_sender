# email_templates.py
from datetime import datetime
import base64
import os

class EmailTemplateGenerator:
    def __init__(self):
        # Tags HTML das imagens com URLs diretas do GitHub
        self.logo_image = '<img src="https://github.com/Apollo-knowledge-AI/icons/blob/main/logomarca_nerd-o_branco.png?raw=true" alt="Apollo AI Logo" style="max-width: 250px; height: auto; border-radius: 8px;">'
        self.icon_image = '<img src="https://github.com/Apollo-knowledge-AI/icons/blob/main/logo_nerd-o.png?raw=true" alt="Apollo AI Icon" style="width: 50px; height: 50px; border-radius: 8px; object-fit: contain;">'

    def get_base_template(self):
        """Template HTML base responsivo"""
        return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ 
            font-family: 'Figtree', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
            color: #333333;
        }}
        
        .container {{ 
            max-width: 600px; 
            margin: 0 auto; 
            background: linear-gradient(135deg, #ffffff 0%, #fefefe 100%);
            box-shadow: 0 8px 32px rgba(0,0,0,0.08);
            border-radius: 16px;
            overflow: hidden;
        }}
        
        .header {{ 
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            padding: 40px 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .header::before {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #F9A826 0%, #EC9A21 50%, #D98C1E 100%);
        }}
        

        
        .header h1 {{ 
            color: white; 
            margin: 15px 0 0 0; 
            font-size: 28px; 
            font-weight: 600;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: relative;
            z-index: 1;
        }}
        
        .content {{ 
            padding: 40px 35px; 
            line-height: 1.7; 
            color: #333333;
            background: #ffffff;
        }}
        
        .greeting {{ 
            font-size: 20px; 
            font-weight: 600; 
            color: #1a1a1a; 
            margin-bottom: 25px;
            background: linear-gradient(135deg, #F9A826 0%, #EC9A21 100%);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .quote {{ 
            font-style: italic; 
            text-align: center; 
            color: #666666; 
            padding: 25px; 
            margin: 25px 0; 
            border-top: 2px solid #f0f0f0;
            background: linear-gradient(135deg, #fefefe 0%, #fafafa 100%);
            border-radius: 12px;
        }}
        
        .signature {{ 
            border-top: 3px solid #F9A826; 
            padding: 35px; 
            background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%);
            display: flex; 
            align-items: flex-start; 
            gap: 25px;
            position: relative;
            justify-content: flex-start;
        }}
        
        .signature-icon {{
            flex-shrink: 0;
            margin-top: 5px;
        }}
        
        .signature-content {{
            flex: 1;
            text-align: left;
        }}
        
        .signature::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #F9A826 0%, #EC9A21 50%, #D98C1E 100%);
        }}
        
        .sig-name {{ 
            font-size: 20px; 
            font-weight: 600; 
            color: #1a1a1a;
            background: linear-gradient(135deg, #F9A826 0%, #EC9A21 100%);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .sig-contact {{ 
            font-size: 14px; 
            color: #666666; 
            line-height: 1.6;
        }}
        
        .footer {{ 
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            color: white; 
            text-align: center; 
            padding: 25px; 
            font-size: 13px;
            position: relative;
        }}
        
        .footer::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #F9A826 0%, #EC9A21 50%, #D98C1E 100%);
        }}
        
        /* Responsive design */
        @media (max-width: 600px) {{ 
            .content, .signature {{ 
                padding: 25px 20px !important; 
            }} 
            .signature {{ 
                flex-direction: row; 
                gap: 15px;
                align-items: flex-start;
            }}
            .signature-icon {{
                margin-top: 0;
            }}
            .signature-content {{
                text-align: left;
            }}
            .header {{
                padding: 30px 20px;
            }}
            .header h1 {{
                font-size: 24px;
            }}
        }}
        
        /* Apollo-specific enhancements */
        .apollo-glow {{
            box-shadow: 0 0 20px rgba(249, 168, 38, 0.3);
        }}
        
        .apollo-text-gradient {{
            background: linear-gradient(135deg, #F9A826 0%, #EC9A21 100%);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            {logo_image}
        </div>
        <div class="content">{conteudo}</div>
        <div class="signature">
            <div class="signature-icon">{icon_image}</div>
            <div class="signature-content">
                <div class="sig-name">{nome_remetente}</div>
                <div style="font-size: 15px; color: #F9A826; margin: 8px 0; font-weight: 500;">Founder</div>
                <div class="sig-contact">
                    📧 {email_remetente}<br>
                    📱 (11) 95101-7666<br>
                    🌐 <a href="https://www.nerd-o.com.br" target="_blank" style="color: #F9A826; text-decoration: none;">www.nerd-o.com.br</a>
                </div>
            </div>
        </div>
        <div class="footer">© {ano} Nerd-o - Transformando Educação</div>
    </div>
</body>
</html>'''

    def get_template_1_content(self, nome_remetente, nome_escola, metodo_ensino):
        """Template 1: Um detalhe que pode transformar ainda mais o dia a dia"""
        return f'''
        <div class="greeting">Olá, equipe da {nome_escola}!</div>
        
        <p>O <strong>{metodo_ensino}</strong> entrega uma base sólida de conteúdo, mas o que realmente transforma a sala de aula é o que acontece entre as linhas — no vínculo com o aluno.</p>
        
        <p>Temos observado um movimento bonito em escolas que estão resgatando a presença afetiva no ensino. Nosso trabalho nasce justamente desse sonho: <strong>fortalecer essa ponte entre professor e aluno</strong>.</p>
        
        <p>Será que essa conversa também faz sentido por aí?</p>
        
        <div class="quote">
            "A educação não é preparação para a vida; a educação é a própria vida."<br><strong>— John Dewey</strong>
        </div>
        '''

    def get_template_2_content(self, nome_remetente, nome_escola, metodologia):
        """Template 2: E se o engajamento dos alunos pudesse ir ainda além?"""
        return f'''
        <div class="greeting">Oi, pessoal!</div>
        
        <p>Sabemos como a <strong>{nome_escola}</strong> se dedica à excelência — o <strong>{metodologia}</strong> já é um passo firme nessa direção.</p>
        
        <p>Mas e se os professores conseguissem atingir os alunos de forma ainda mais direta, emocional e transformadora? A gente acredita que o próximo salto da educação está na <strong>conexão, não só na instrução</strong>.</p>
        
        <p>Estamos aqui pra caminhar junto nessa visão.</p>
        
        <div class="quote">
            "O professor medíocre conta. O bom professor explica. O professor superior demonstra. O grande professor inspira."<br><strong>— William Arthur Ward</strong>
        </div>
        '''

    def get_template_3_content(self, nome_remetente, nome_escola):
        """Template 3: O que diferencia as escolas que marcam gerações?"""
        return f'''
        <div class="greeting">Olá, tudo bem por aí?</div>
        
        <p>Algumas escolas seguem o currículo à risca, mas outras deixam marcas que os alunos levam pra vida inteira.</p>
        
        <p>A <strong>{nome_escola}</strong> já é uma referência — e talvez esteja na hora de fortalecer ainda mais esse diferencial. Hoje, quem se destaca não é só quem ensina mais, mas quem cria <strong>relações mais fortes</strong>.</p>
        
        <p>Será que conseguimos sonhar esse próximo passo juntos?</p>
        
        <div class="quote">
            "A educação é o passaporte para o futuro, pois o amanhã pertence àqueles que se preparam para ele hoje."<br><strong>— Malcolm X</strong>
        </div>
        '''

    def get_template_4_content(self, nome_remetente, nome_escola, metodologia):
        """Template 4: Quando a relação esfria, nem o melhor conteúdo segura o aluno"""
        return f'''
        <div class="greeting">Oi, pessoal da {nome_escola}!</div>
        
        <p>Mesmo com um sistema robusto como o <strong>{metodologia}</strong>, a gente sabe que às vezes o aluno se desconecta — e o professor sente isso.</p>
        
        <p>Essa distância silenciosa, quando cresce, cobra um preço alto no engajamento e nos resultados. A gente acredita que dá pra evitar esse afastamento com <strong>gestos pequenos, mas consistentes</strong>.</p>
        
        <p>Talvez possamos conversar sobre como proteger esse vínculo tão essencial.</p>
        
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