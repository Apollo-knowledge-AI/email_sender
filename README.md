# 📧 Apollo AI - Sistema de Envio de Emails

Sistema profissional para envio de emails educacionais com templates personalizados e interface gráfica intuitiva.

## ✨ Funcionalidades

### 🎨 Templates Profissionais
- **Template 1**: Presença Afetiva no Ensino
- **Template 2**: Engajamento Avançado dos Alunos  
- **Template 3**: Escolas que Marcam Gerações
- **Template 4**: Protegendo Vínculos Essenciais

### 🔐 Gerenciamento de Credenciais
- **Salvar credenciais**: Botão para salvar email e senha em arquivo `.env`
- **Carregar credenciais**: Carregamento automático e manual das credenciais
- **Segurança**: Arquivo `.env` protegido no `.gitignore`

### 🖥️ Interface Moderna
- **Scrollbar**: Navegação suave em telas menores
- **Design responsivo**: Adapta-se a diferentes tamanhos de tela
- **Preview em tempo real**: Visualização instantânea dos emails
- **Preview no navegador**: Visualização completa em HTML

## 🚀 Como Usar

### 1. Configuração Inicial
```bash
# Clone o repositório
git clone [url-do-repositorio]
cd email_sender

# Execute o programa
python main.py
```

### 2. Configurar Credenciais
1. **Preencha** seu nome, email e senha
2. **Clique** em "💾 Salvar Credenciais"
3. As credenciais serão salvas no arquivo `.env`
4. Na próxima execução, elas serão carregadas automaticamente

### 3. Para Gmail
- Ative a **autenticação de 2 fatores**
- Use uma **"Senha de App"** em vez da senha normal
- Acesse: Conta Google > Segurança > Senhas de app

### 4. Enviar Emails
1. **Preencha** os dados da escola destinatária
2. **Selecione** o método/metodologia da escola
3. **Escolha** um dos 4 templates disponíveis
4. **Visualize** o preview do email
5. **Clique** em "📤 Enviar Email"

## 📁 Estrutura do Projeto

```
email_sender/
├── main.py              # Arquivo principal (limpo e organizado)
├── app/                 # Módulo principal da aplicação
│   ├── __init__.py      # Configurações do módulo
│   ├── gui.py           # Interface gráfica (GUI)
│   ├── templates.py     # Lógica de negócio e funcionalidades
│   └── base_email.py    # Gerador de templates HTML
├── env_example.txt      # Exemplo de arquivo .env
├── .env                 # Credenciais (criado automaticamente)
├── image/               # Imagens e logos
│   ├── icon.png
│   └── logomarca.png
└── README.md
```

## 🔧 Configuração do Arquivo .env

O arquivo `.env` é criado automaticamente quando você salva as credenciais:

```env
# Credenciais do Apollo AI Email Sender
NAME=Seu Nome Completo
EMAIL=seu_email@gmail.com
PASSWORD=sua_senha_de_app

# Configurações SMTP
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## ⚠️ Segurança

- **Nunca compartilhe** o arquivo `.env`
- **Use senhas de app** para Gmail
- O arquivo `.env` está no `.gitignore`
- As credenciais são armazenadas localmente

## 🎯 Templates Disponíveis

### Template 1: Presença Afetiva
**Assunto**: "Um detalhe que pode transformar ainda mais o dia a dia da [escola]"
- Foco no vínculo entre professor e aluno
- Abordagem emocional e humana

### Template 2: Engajamento Avançado  
**Assunto**: "E se o engajamento dos alunos da [escola] pudesse ir ainda além?"
- Conexão emocional e transformadora
- Próximo nível de engajamento

### Template 3: Escolas que Marcam
**Assunto**: "O que diferencia as escolas que marcam gerações?"
- Diferencial educacional
- Legado e impacto duradouro

### Template 4: Protegendo Vínculos
**Assunto**: "Quando a relação esfria, nem o melhor conteúdo segura o aluno"
- Prevenção de desconexão
- Manutenção de relacionamentos

## 🛠️ Tecnologias

- **Python 3.x**
- **Tkinter** (Interface gráfica)
- **SMTP** (Envio de emails)
- **HTML/CSS** (Templates responsivos)

## 🏗️ Arquitetura

O projeto foi organizado seguindo boas práticas de desenvolvimento:

- **Separação de responsabilidades**: GUI, lógica de negócio e templates separados
- **Modularização**: Código organizado em módulos específicos
- **Manutenibilidade**: Estrutura clara e fácil de manter
- **Escalabilidade**: Fácil adição de novos templates e funcionalidades

## 📞 Suporte

Para dúvidas ou problemas:
- Verifique se as credenciais estão corretas
- Confirme se a autenticação de 2 fatores está ativa (Gmail)
- Use senhas de app em vez de senhas normais

---

**Desenvolvido pela Apollo AI**