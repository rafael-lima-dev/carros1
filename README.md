🏎️ RV Veículos — Sistema de Gestão de Carros

Aplicação web desenvolvida com Django (Python) para cadastro, listagem e gerenciamento de veículos.
O sistema foi construído com foco em boas práticas de backend, integração com IA (Gemini API) e tratamento inteligente de arquivos de imagem.

🚀 Tecnologias Utilizadas
Categoria	Tecnologias
Backend	Python 3.11 • Django 5.2
Banco de Dados	PostgreSQL
Front-end (templates)	HTML5 • CSS3 • Bootstrap (via templates Django)
Integrações	Gemini API (IA para descrição automática dos veículos)
Gerenciamento de ambiente	python-dotenv
Upload e tratamento de arquivos	ImageField (Django ORM) + signals personalizados
Outros pacotes	Pillow • psycopg2-binary • django-humanize
⚙️ Funcionalidades Principais

✅ CRUD completo de veículos e marcas
✅ Upload de imagens com validação e remoção automática de arquivos antigos
✅ Geração automática de descrição (bio) via integração com API Gemini
✅ Busca dinâmica por modelo de carro
✅ Controle de acesso com autenticação de usuários
✅ Atualização automática de inventário (quantidade total de carros e valor total)
✅ Tratamento de exceções e dados vazios (ex.: placa e foto opcionais)

🧠 Destaques Técnicos
🔹 Modelos (models.py)

Car e Brand estruturam a base do domínio.

Campos opcionais (blank=True, null=True) evitam erros de exibição.

CarInventory guarda histórico agregado de preços e quantidades de veículos.

🔹 Formulários (forms.py)

CarModelForm com validações customizadas (clean_price, clean_factory_year, clean_photo)

Lógica condicional que obriga o envio de foto apenas no cadastro, não na edição.

🔹 Views (views.py)

Uso de Class-Based Views (CBVs): ListView, CreateView, DetailView, UpdateView, DeleteView.

Implementação do decorador login_required para proteger rotas críticas.

Busca por nome do modelo via GET com icontains.

🔹 Signals (signals.py)

Integração com Gemini API para gerar descrições automáticas de veículos.

Atualização do inventário a cada inserção, atualização ou exclusão.

Limpeza automática de imagens antigas e remoção do arquivo ao deletar um veículo.

🔹 Settings

Configuração de MEDIA_ROOT e MEDIA_URL para upload de imagens.

dotenv para gerenciamento de variáveis sensíveis.

ALLOWED_HOSTS = ['*'] (modo dev) e DEBUG = True.

🗂️ Estrutura do Projeto
carros-master/
├── cars/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── signals.py
│   ├── templates/
│   │   ├── cars.html
│   │   ├── new_car.html
│   │   ├── car_detail.html
│   │   ├── car_update.html
│   │   └── car_delete.html
│   └── ...
├── accounts/
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── static/
├── manage.py
└── requirements.txt

🧰 Instalação e Execução Local
# 1️⃣ Clone o repositório
git clone https://github.com/seuusuario/carros-master.git
cd carros-master

# 2️⃣ Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

# 3️⃣ Instale as dependências
pip install -r requirements.txt

# 4️⃣ Configure o arquivo .env
cp .env.example .env
# e adicione suas variáveis (chave da API Gemini, DB etc.)

# 5️⃣ Execute as migrações
python manage.py migrate

# 6️⃣ Inicie o servidor
python manage.py runserver

🧩 Demonstração de Recursos
Recurso	Descrição
🖼️ Upload de imagem	Cada carro pode ter uma foto; se substituída, a antiga é apagada do disco automaticamente
🤖 Bio automática	Gerada via Gemini API ao salvar um carro sem descrição
🧾 Inventário automático	Atualiza quantidade e valor agregado em tempo real
🔍 Busca por modelo	Filtra carros pelo nome no campo de pesquisa
🔒 Login obrigatório	Para criar, editar ou excluir veículos
🧠 Aprendizados Técnicos

Durante o desenvolvimento foram aplicadas práticas de:

Design orientado a modelos (Django ORM)

CBVs e MVT Pattern (Model-View-Template)

Validações customizadas e limpezas (clean_)

Uso de signals para lógica de backend desacoplada

Integração com API externa e tratamento de erros

Manuseio de arquivos e caminhos com os.path e MEDIA_ROOT

🧾 Licença

Este projeto é de uso livre para fins educacionais e de portfólio.
Desenvolvido por Rafael França 💻

📧 Contato: [rafaelfrancadev01@gmail.com]

🌐 LinkedIn: [linkedin.com/in/rafael-frança-31b7b9291]

🐙 GitHub: [https://github.com/rafael-lima-dev]