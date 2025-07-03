# email_templates.py
from datetime import datetime
import base64
import os

class EmailTemplateGenerator:
    def __init__(self):
        # Gerar tags <img> com imagens em base64
        self.logo_image = self.get_image_tag('image/logomarca.png', 'Logo Apollo', 100)
        self.icon_image = self.get_image_tag('image/icon.png', 'Ícone Assinatura', 60)

    def get_image_tag(self, image_path, alt="", max_height=60):
        """Retorna uma tag <img> com a imagem em base64 embutida, usando caminho absoluto"""
        try:
            abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', image_path))
            with open(abs_path, "rb") as img_file:
                b64_data = base64.b64encode(img_file.read()).decode("utf-8")
                print(b64_data[:200])
            return f'<img src="data:image/png;base64,{b64_data}" alt="{alt}" style="max-height:{max_height}px;">'
        except Exception as e:
            return f'<span style="color:red">[Erro ao carregar imagem: {alt}]</span>'

    def get_base_template(self):
        """Template HTML base responsivo"""
        return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
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
            align-items: center; 
            gap: 20px;
            position: relative;
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
                flex-direction: column; 
                text-align: center; 
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
            <div>{icon_image}</div>
            <div>
                <div class="sig-name">{nome_remetente}</div>
                <div style="font-size: 15px; color: #F9A826; margin: 8px 0; font-weight: 500;">Consultor de Inteligência Artificial</div>
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