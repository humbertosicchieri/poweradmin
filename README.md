# PowerAdmin - Repositório de Scripts Microsoft

[![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)](https://www.docker.com/)
[![Node.js](https://img.shields.io/badge/Node.js-18-green?logo=node.js)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 📋 Descrição

**PowerAdmin** é uma plataforma web moderna, leve e responsiva para gerenciar um repositório profissional de scripts Microsoft (PowerShell, Batch, VBScript). A solução inclui:

- 🌐 **Interface Web Moderna** - Construída com Vue 3 + Vite
- ⚡ **API Rápida** - Backend em FastAPI
- 🔄 **Automação com N8N** - Sincronização automática de scripts do GitHub via IA
- 🐳 **Docker Compose** - Deploy em uma única linha
- 💾 **Banco de Dados PostgreSQL** - Persistência robusta

## 🚀 Quick Start

### Pré-requisitos
- Docker e Docker Compose instalados
- Token GitHub (para sincronização)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/humbertosicchieri/poweradmin.git
cd poweradmin
```

2. **Configure as variáveis de ambiente:**
```bash
cp .env.example .env
# Edite o arquivo .env com seus valores
```

3. **Inicie os serviços:**
```bash
docker-compose up -d
```

4. **Acesse a aplicação:**
- 🌐 Frontend: http://localhost:3000
- 🔌 API: http://localhost:8000
- ⚙️ N8N: http://localhost:5678

## 📁 Estrutura do Projeto

```
poweradmin/
├── web/                    # Aplicação Vue 3
│   ├── src/
│   │   ├── components/     # Componentes Vue
│   │   ├── views/          # Páginas
│   │   ├── router/         # Roteamento
│   │   └── style.css       # Estilos Tailwind
│   └── package.json
├── api/                    # Backend FastAPI
│   ├── main.py            # Aplicação principal
│   ├── models.py          # Modelos de dados
│   ├── routes.py          # Rotas da API
│   └── requirements.txt
├── n8n/                    # Workflows N8N
│   └── workflows/         # Automações
├── docker-compose.yml      # Composição dos serviços
├── Dockerfile.web         # Build da aplicação web
└── Dockerfile.api         # Build da API
```

## 🔧 Configuração

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `GITHUB_TOKEN` | Token de autenticação GitHub | - |
| `GITHUB_OWNER` | Proprietário do repositório | `humbertosicchieri` |
| `GITHUB_REPO` | Nome do repositório | `poweradmin` |
| `DATABASE_URL` | String de conexão PostgreSQL | `postgresql://postgres:postgres@db:5432/poweradmin` |

## 🎨 Funcionalidades

### Frontend
- ✅ Dashboard com estatísticas
- ✅ Busca e filtro de scripts
- ✅ Visualização detalhada de scripts
- ✅ Suporte responsivo (mobile/desktop)
- ✅ Tema dark mode nativo
- ✅ Sintaxe highlighting para código

### Backend
- ✅ CRUD de scripts
- ✅ Filtros por categoria
- ✅ Integração GitHub
- ✅ Cache de performance
- ✅ Autenticação (pronto para implementar)

### Automação (N8N)
- 🔄 Sincronização automática de scripts do GitHub
- 🤖 Análise com IA para categorização
- 📧 Notificações de atualizações
- ⏰ Agendamento de tarefas

## 📊 Endpoints da API

```
GET  /                      # Status da API
GET  /scripts               # Listar scripts (com filtro e paginação)
GET  /scripts/{id}          # Obter script específico
POST /scripts               # Criar novo script
GET  /categories            # Listar categorias
POST /sync-github           # Sincronizar com GitHub
```

## 🔄 Fluxo de Sincronização (N8N)

```
GitHub Repository
       ↓
N8N Webhook
       ↓
Extrai scripts (.ps1, .bat, .vbs)
       ↓
Analisa com IA para categorização
       ↓
Salva no PostgreSQL
       ↓
Atualiza Frontend automaticamente
```

## 🛠️ Desenvolvimento

### Estrutura de Categorias

- 👥 Active Directory
- 📧 Exchange Server
- 🗄️ SQL Server
- 🖥️ Windows Server
- ☁️ Hyper-V
- 💾 Backup & Recovery
- 🌐 Network & Connectivity
- 🔒 Security & Compliance

## 📝 Tipos de Scripts Suportados

- **PowerShell** (.ps1)
- **Batch** (.bat)
- **VBScript** (.vbs)

## 🔐 Segurança

- Variáveis sensíveis em `.env`
- CORS configurado
- PostgreSQL com validação
- GitHub Token protegido

## 📦 Dependências Principais

### Frontend
- Vue 3
- Vite
- Vue Router
- Pinia (State Management)
- Tailwind CSS
- Axios
- Highlight.js

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- PyGithub
- Pydantic

### Infraestrutura
- Docker & Docker Compose
- PostgreSQL 15
- N8N

## 🚀 Deploy

### Docker Compose (Recomendado)
```bash
docker-compose up -d
```

### Kubernetes (Futuro)
Manifests Kubernetes serão adicionados em breve.

## 📈 Roadmap

- [ ] Autenticação com GitHub OAuth
- [ ] Upload de scripts via interface
- [ ] Sistema de ratings e comentários
- [ ] Versionamento de scripts
- [ ] CI/CD pipeline
- [ ] Testes automatizados
- [ ] Documentação em Swagger
- [ ] Suporte a múltiplos idiomas

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para reportar bugs ou sugerir melhorias, abra uma issue no GitHub.

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**Humberto Sicchieri**
- GitHub: [@humbertosicchieri](https://github.com/humbertosicchieri)

## 🙏 Agradecimentos

- Vue.js comunidade
- FastAPI team
- N8N community
- Tailwind CSS

---

**Desenvolvido com ❤️ para administradores Microsoft**
