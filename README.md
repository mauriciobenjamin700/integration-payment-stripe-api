# 🚀 Stripe Integration API

Uma API completa para integração com Stripe, desenvolvida em Python usando FastAPI. Esta API fornece endpoints para gerenciar clientes, pagamentos, produtos, preços e assinaturas através da plataforma Stripe.

## 📋 Índice

- [🚀 Stripe Integration API](#-stripe-integration-api)
  - [📋 Índice](#-índice)
  - [🎯 Visão Geral](#-visão-geral)
  - [🏗️ Arquitetura](#️-arquitetura)
  - [🛠️ Tecnologias](#️-tecnologias)
  - [📦 Instalação e Configuração](#-instalação-e-configuração)
  - [🔧 Configuração do Ambiente](#-configuração-do-ambiente)
  - [📚 Estrutura do Projeto](#-estrutura-do-projeto)
  - [💼 Regras de Negócio](#-regras-de-negócio)
  - [📖 Schemas (Modelos de Dados)](#-schemas-modelos-de-dados)
  - [🔄 Services (Serviços)](#-services-serviços)
  - [🛣️ Rotas (Endpoints)](#️-rotas-endpoints)
  - [📡 Webhooks](#-webhooks)
  - [🔍 Utilitários e Enums](#-utilitários-e-enums)
  - [⚙️ Configurações](#️-configurações)
  - [🚦 Como Executar](#-como-executar)
  - [📋 Exemplos de Uso](#-exemplos-de-uso)
  - [🔒 Segurança](#-segurança)
  - [🧪 Testes](#-testes)
  - [📝 Licença](#-licença)

## 🎯 Visão Geral

Esta API fornece uma interface RESTful para:

- **Gerenciamento de Clientes**: Criar, atualizar, recuperar e deletar clientes no Stripe
- **Processamento de Pagamentos**: Criar, confirmar e cancelar intenções de pagamento
- **Catálogo de Produtos**: Gerenciar produtos e seus preços
- **Sistema de Assinaturas**: Criar e gerenciar assinaturas recorrentes
- **Webhooks**: Processar eventos em tempo real do Stripe

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas com separação clara de responsabilidades:

```
├── Core Layer (Configurações e Classes Base)
├── Schema Layer (Modelos de Dados e Validação)
├── Service Layer (Lógica de Negócio)
├── Route Layer (Endpoints da API)
└── Utils Layer (Utilitários e Enums)
```

### Princípios Arquiteturais

- **Single Responsibility**: Cada módulo tem uma responsabilidade específica
- **Dependency Injection**: Configurações centralizadas
- **Validation First**: Validação rigorosa usando Pydantic
- **Error Handling**: Tratamento consistente de erros
- **Type Safety**: Tipagem forte em Python

## 🛠️ Tecnologias

### Core Stack
- **Python 3.13+**: Linguagem principal
- **FastAPI**: Framework web moderno e performático
- **Pydantic**: Validação de dados e serialização
- **Stripe SDK**: Biblioteca oficial do Stripe para Python
- **Uvicorn**: Servidor ASGI de alta performance

### Ferramentas de Desenvolvimento
- **Ruff**: Linter e formatter para Python
- **Pydantic Settings**: Gerenciamento de configurações
- **HTTPX**: Cliente HTTP assíncrono

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.13 ou superior
- Conta no Stripe (modo teste ou produção)
- Git

### Clonando o Repositório
```bash
git clone <url-do-repositorio>
cd integration-payment-stripe-api
```

### Instalação de Dependências
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Instalar dependências
pip install -e .
```

## 🔧 Configuração do Ambiente

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
STRIPE_PUBLIC_KEY=pk_test_sua_chave_publica_aqui
STRIPE_SECRET_KEY=sk_test_sua_chave_secreta_aqui
```

### Configurações de Segurança

- **Chaves de Teste**: Use `pk_test_*` e `sk_test_*` para desenvolvimento
- **Chaves de Produção**: Use `pk_live_*` e `sk_live_*` apenas em produção
- **Webhooks**: Configure endpoints seguros para receber eventos

## 📚 Estrutura do Projeto

```
integration-payment-stripe-api/
├── src/
│   ├── core/                 # Configurações e classes base
│   │   ├── __init__.py
│   │   ├── base.py          # BaseSchema e BaseEnum
│   │   └── settings.py      # Configurações da aplicação
│   ├── schemas/             # Modelos de dados (Pydantic)
│   │   ├── __init__.py
│   │   ├── customer.py      # Schemas de clientes
│   │   ├── payment.py       # Schemas de pagamentos
│   │   ├── product.py       # Schemas de produtos e preços
│   │   └── subscription.py  # Schemas de assinaturas
│   ├── services/            # Lógica de negócio
│   │   ├── __init__.py
│   │   ├── customer.py      # Serviços de clientes
│   │   ├── payment.py       # Serviços de pagamentos
│   │   ├── product.py       # Serviços de produtos
│   │   ├── subscription.py  # Serviços de assinaturas
│   │   └── webhook.py       # Processamento de webhooks
│   ├── routes/              # Endpoints da API
│   │   ├── __init__.py
│   │   ├── customer.py      # Rotas de clientes
│   │   ├── payment.py       # Rotas de pagamentos
│   │   ├── product.py       # Rotas de produtos
│   │   └── subscription.py  # Rotas de assinaturas
│   ├── utils/               # Utilitários e enums
│   │   ├── __init__.py
│   │   └── payment.py       # Enums para pagamentos
│   ├── __init__.py
│   └── app.py              # Configuração principal do FastAPI
├── main.py                 # Ponto de entrada da aplicação
├── pyproject.toml          # Configurações do projeto
├── Makefile               # Comandos úteis
├── .env                   # Variáveis de ambiente (não versionado)
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto
```

## 💼 Regras de Negócio

### 🏢 Gerenciamento de Clientes

#### Criação de Clientes
- **Unicidade**: Email deve ser único no sistema
- **Metadata**: Suporte a `user_id` para vincular com sistema interno
- **Endereçamento**: Endereços completos obrigatórios (billing e shipping)
- **Validação**: Validação rigorosa de dados pessoais

#### Atualização de Clientes
- **Preservação**: Histórico de transações é mantido
- **Validação**: Alterações passam por validação similar à criação

### 💳 Processamento de Pagamentos

#### Payment Intents
- **Moedas Suportadas**: BRL, USD, EUR
- **Métodos Automáticos**: Google Pay, Apple Pay, cartões, PIX, boleto
- **Metadata**: Rastreamento por `user_id` e `product_id`
- **Status**: `requires_payment_method`, `succeeded`, `canceled`

#### Cancelamento
- **Timing**: Apenas pagamentos não confirmados podem ser cancelados
- **Refunds**: Para pagamentos confirmados, use refunds (não implementado nesta versão)

### 🛍️ Catálogo de Produtos

#### Produtos
- **Hierarquia**: Produto → Preços → Assinaturas
- **Estados**: Ativo ou arquivado (não deletado permanentemente)
- **Metadata**: Suporte a informações customizadas

#### Preços
- **Tipos**: Únicos ou recorrentes (assinaturas)
- **Intervalos**: Diário, semanal, mensal, anual
- **Trial**: Suporte a períodos de teste
- **Moedas**: Múltiplas moedas por produto

### 🔄 Sistema de Assinaturas

#### Criação de Assinaturas
- **Customer Obrigatório**: Todo subscription precisa de um customer
- **Price Required**: Deve referenciar um preço válido
- **Trial Support**: Períodos de teste opcionais
- **Invoice Generation**: Faturas automáticas

#### Estados de Assinatura
- **active**: Assinatura ativa e funcionando
- **incomplete**: Aguardando primeiro pagamento
- **trialing**: Em período de teste
- **past_due**: Pagamento em atraso
- **canceled**: Cancelada
- **unpaid**: Não paga após tentativas

#### Cancelamento
- **Imediato**: Cancela imediatamente
- **Fim do Período**: Cancela no final do período atual (padrão)

### 📡 Webhooks

#### Eventos Suportados
- `payment_intent.succeeded`: Pagamento bem-sucedido
- `payment_intent.payment_failed`: Falha no pagamento
- `customer.created`: Cliente criado
- `customer.subscription.created`: Assinatura criada
- `customer.subscription.updated`: Assinatura atualizada
- `customer.subscription.deleted`: Assinatura cancelada

#### Verificação de Segurança
- **Signature Verification**: Verificação da assinatura do Stripe
- **Payload Validation**: Validação do payload do evento

## 📖 Schemas (Modelos de Dados)

### 👤 Customer Schemas

#### CustomerCreate
```python
class CustomerCreate(BaseSchema):
    email: str                    # Email único do cliente
    name: str                     # Nome completo
    shipping: Shipping            # Endereço de entrega
    address: Address              # Endereço de cobrança
    metadata: Metadata | None     # Metadados opcionais
```

#### Address
```python
class Address(BaseSchema):
    city: str                     # Cidade
    country: str                  # País
    line1: str                    # Linha 1 do endereço
    postal_code: str              # CEP/Código postal
    state: str                    # Estado/Província
```

#### Metadata
```python
class Metadata(BaseSchema):
    user_id: str                  # ID do usuário no sistema interno
```

### 💳 Payment Schemas

#### PaymentIntentCreate
```python
class PaymentIntentCreate(BaseSchema):
    amount: int                   # Valor em centavos
    currency: CurrencyEnum        # Moeda (BRL, USD, EUR)
    automatic_payment_methods: dict  # Métodos automáticos habilitados
    metadata: CustomerMetadata | None  # Metadados opcionais
```

#### PaymentIntentResponse
```python
class PaymentIntentResponse(BaseSchema):
    id: str                       # ID único do payment intent
    client_secret: str            # Segredo para o frontend
    status: str                   # Status atual
    amount: int                   # Valor cobrado
    currency: CurrencyEnum        # Moeda
    metadata: CustomerMetadata | None  # Metadados
    created: int                  # Timestamp de criação
```

### 🛍️ Product Schemas

#### ProductCreate
```python
class ProductCreate(BaseSchema):
    name: str                     # Nome do produto
    description: str | None       # Descrição opcional
    metadata: dict[str, str] | None  # Metadados opcionais
```

#### PriceCreate
```python
class PriceCreate(BaseSchema):
    product_id: str               # ID do produto pai
    unit_amount: int              # Valor em centavos
    currency: CurrencyEnum        # Moeda
    recurring: Recurring          # Configurações de recorrência
```

#### Recurring
```python
class Recurring(BaseSchema):
    interval: SubscriptionInterval  # Intervalo (month, year, etc.)
    interval_count: int           # Quantidade de intervalos
    trial_period_days: int | None # Dias de trial opcional
```

### 🔄 Subscription Schemas

#### SubscriptionCreate
```python
class SubscriptionCreate(BaseSchema):
    customer_id: str | None       # ID do cliente (pode ser None se criado junto)
    price_id: str                 # ID do preço
    trial_period_days: int | None # Dias de trial
    metadata: Metadata | None     # Metadados opcionais
```

#### SubscriptionResponse
```python
class SubscriptionResponse(BaseSchema):
    id: str                       # ID único da assinatura
    status: SubscriptionStatus    # Status atual
    customer: str                 # ID do cliente
    start_date: int               # Data de início
    ended_at: int | None          # Data de término (None se ativa)
    price_id: str                 # ID do preço
    amount: int                   # Valor cobrado
    currency: str                 # Moeda
    interval: SubscriptionInterval # Intervalo de cobrança
    trial_start: int | None       # Início do trial
    trial_end: int | None         # Fim do trial
    metadata: dict[str, str] | None # Metadados
```

## 🔄 Services (Serviços)

### 👤 CustomerService

#### Métodos Principais

```python
class CustomerService:
    @staticmethod
    def create_customer(data: CustomerCreate) -> CustomerResponse:
        """
        Cria um cliente no Stripe.
        
        Validações:
        - Email único
        - user_id único (se fornecido)
        
        Raises:
        - HTTPException(409): Cliente já existe
        - HTTPException(500): Erro interno
        """
    
    @staticmethod
    def get_customer_by_user_id(user_id: str) -> CustomerResponse:
        """
        Busca cliente por user_id usando metadata.
        
        Returns:
        - CustomerResponse: Dados do cliente
        
        Raises:
        - HTTPException(404): Cliente não encontrado
        """
```

### 💳 PaymentService

#### Métodos Principais

```python
class PaymentService:
    @staticmethod
    def create_payment_intent(data: PaymentIntentCreate) -> PaymentIntentResponse:
        """
        Cria um payment intent no Stripe.
        
        Features:
        - Métodos de pagamento automáticos
        - Suporte a metadata personalizada
        - Tratamento robusto de erros
        """
    
    @staticmethod
    def get_payment_intent_by_user_id(user_id: str, limit: int = 1) -> list[PaymentIntentResponse]:
        """
        Busca payment intents por user_id.
        
        Parameters:
        - user_id: ID do usuário no sistema interno
        - limit: Número máximo de resultados
        """
```

### 🛍️ ProductService

#### Métodos Principais

```python
class ProductService:
    @staticmethod
    def create_product(data: ProductCreate) -> ProductResponse:
        """
        Cria um produto no Stripe.
        
        Returns:
        - ProductResponse: Dados do produto criado
        """
    
    @staticmethod
    def create_price(data: PriceCreate) -> PriceResponse:
        """
        Cria um preço para um produto.
        
        Features:
        - Suporte a recorrência
        - Múltiplas moedas
        - Períodos de trial
        """
    
    @staticmethod
    def delete_product(product_id: str) -> dict:
        """
        Arquiva um produto (não deleta permanentemente).
        
        Process:
        1. Arquiva todos os preços ativos
        2. Arquiva o produto
        
        Note:
        - Stripe não permite deleção permanente
        - Mantém integridade de dados históricos
        """
```

### 🔄 SubscriptionService

#### Métodos Principais

```python
class SubscriptionService:
    @staticmethod
    def create_subscription(data: SubscriptionCreate) -> SubscriptionResponse:
        """
        Cria uma assinatura no Stripe.
        
        Process:
        1. Valida customer e price
        2. Cria subscription
        3. Gera invoice automática
        
        Returns:
        - SubscriptionResponse: Dados da assinatura
        """
    
    @staticmethod
    def create_subscription_with_trial(data: SubscriptionCreate) -> SubscriptionResponse:
        """
        Cria assinatura com período de trial.
        
        Features:
        - Trial de 7 dias por padrão
        - Sem cobrança inicial
        - Invoice gerada ao final do trial
        """
    
    @staticmethod
    def cancel_subscription(subscription_id: str, at_period_end: bool = True) -> CancelSubscriptionResponse:
        """
        Cancela uma assinatura.
        
        Parameters:
        - at_period_end: Se True, cancela no final do período atual
        """
```

### 📡 WebhookService

#### Métodos Principais

```python
class WebhookService:
    @staticmethod
    def verify_webhook_signature(payload: bytes, sig_header: str) -> stripe.Event:
        """
        Verifica a assinatura do webhook.
        
        Security:
        - Validação criptográfica
        - Proteção contra replay attacks
        """
    
    @staticmethod
    def handle_webhook_event(event: stripe.Event) -> dict[str, Any]:
        """
        Processa diferentes tipos de eventos.
        
        Supported Events:
        - payment_intent.succeeded
        - payment_intent.payment_failed
        - customer.created
        """
```

## 🛣️ Rotas (Endpoints)

### 👤 Customer Routes (`/customer`)

| Método | Endpoint | Descrição | Schema Request | Schema Response |
|--------|----------|-----------|----------------|----------------|
| POST | `/customer/` | Criar cliente | `CustomerCreate` | `CustomerResponse` |
| GET | `/customer/{customer_id}` | Buscar cliente por ID | - | `CustomerResponse` |
| GET | `/customer/user/{user_id}` | Buscar cliente por user_id | - | `CustomerResponse` |
| PUT | `/customer/{customer_id}` | Atualizar cliente | `CustomerCreate` | `CustomerResponse` |
| DELETE | `/customer/{customer_id}` | Deletar cliente | - | `dict` |
| DELETE | `/customer/user/{user_id}` | Deletar cliente por user_id | - | `dict` |

#### Exemplos de Uso

```bash
# Criar cliente
curl -X POST http://localhost:4242/customer/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@exemplo.com",
    "name": "João Silva",
    "address": {
      "city": "São Paulo",
      "country": "Brasil",
      "line1": "Rua das Flores, 123",
      "postal_code": "01234-567",
      "state": "SP"
    },
    "shipping": {
      "name": "João Silva",
      "address": {
        "city": "São Paulo",
        "country": "Brasil",
        "line1": "Rua das Flores, 123",
        "postal_code": "01234-567",
        "state": "SP"
      }
    },
    "metadata": {
      "user_id": "12345"
    }
  }'
```

### 💳 Payment Routes (`/payment-intents`)

| Método | Endpoint | Descrição | Schema Request | Schema Response |
|--------|----------|-----------|----------------|----------------|
| POST | `/payment-intents/` | Criar payment intent | `PaymentIntentCreate` | `PaymentIntentResponse` |
| GET | `/payment-intents/{payment_intent_id}` | Buscar payment intent | - | `PaymentIntentResponse` |
| GET | `/payment-intents/user/{user_id}` | Buscar por user_id | - | `list[PaymentIntentResponse]` |
| POST | `/payment-intents/{payment_intent_id}/cancel` | Cancelar payment intent | - | `CancelPaymentIntentResponse` |

#### Exemplos de Uso

```bash
# Criar payment intent
curl -X POST http://localhost:4242/payment-intents/ \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 2000,
    "currency": "brl",
    "metadata": {
      "user_id": "12345",
      "product_id": "prod_123"
    }
  }'
```

### 🛍️ Product Routes (`/products`)

| Método | Endpoint | Descrição | Schema Request | Schema Response |
|--------|----------|-----------|----------------|----------------|
| POST | `/products/` | Criar produto | `ProductCreate` | `ProductResponse` |
| GET | `/products/` | Listar produtos | Query: `include_archived` | `list[ProductResponse]` |
| DELETE | `/products/{product_id}` | Arquivar produto | - | `dict` |
| POST | `/products/prices` | Criar preço | `PriceCreate` | `PriceResponse` |
| DELETE | `/products/prices/{price_id}` | Arquivar preço | - | `dict` |

#### Exemplos de Uso

```bash
# Criar produto
curl -X POST http://localhost:4242/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Plano Premium",
    "description": "Acesso completo aos recursos",
    "metadata": {
      "category": "subscription",
      "tier": "premium"
    }
  }'

# Criar preço
curl -X POST http://localhost:4242/products/prices \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": "prod_ABC123",
    "unit_amount": 2990,
    "currency": "brl",
    "recurring": {
      "interval": "month",
      "interval_count": 1,
      "trial_period_days": 7
    }
  }'
```

### 🔄 Subscription Routes (`/subscriptions`)

| Método | Endpoint | Descrição | Schema Request | Schema Response |
|--------|----------|-----------|----------------|----------------|
| POST | `/subscriptions/` | Criar assinatura | `SubscriptionCreate` | `SubscriptionResponse` |
| GET | `/subscriptions/users/{user_id}` | Buscar assinaturas do usuário | - | `list[SubscriptionResponse]` |
| POST | `/subscriptions/{subscription_id}/cancel` | Cancelar assinatura | Query: `at_period_end` | `CancelSubscriptionResponse` |

#### Exemplos de Uso

```bash
# Criar assinatura
curl -X POST http://localhost:4242/subscriptions/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "cus_ABC123",
    "price_id": "price_XYZ789",
    "trial_period_days": 7,
    "metadata": {
      "user_id": "12345"
    }
  }'

# Cancelar assinatura (no final do período)
curl -X POST http://localhost:4242/subscriptions/sub_123/cancel?at_period_end=true
```

## 📡 Webhooks

### Configuração de Webhooks

1. **No Dashboard do Stripe**:
   - Vá para "Developers" → "Webhooks"
   - Adicione endpoint: `https://sua-api.com/webhooks`
   - Selecione eventos relevantes

2. **Eventos Recomendados**:

   ```bash
   payment_intent.succeeded
   payment_intent.payment_failed
   customer.created
   customer.subscription.created
   customer.subscription.updated
   customer.subscription.deleted
   invoice.payment_succeeded
   invoice.payment_failed
   ```

### Implementação

```python
@app.post("/webhooks")
async def handle_webhook(
    request: Request,
    stripe_signature: str = Header(None, alias="stripe-signature")
):
    """Handle Stripe webhooks."""
    payload = await request.body()
    
    try:
        event = WebhookService.verify_webhook_signature(payload, stripe_signature)
        result = WebhookService.handle_webhook_event(event)
        return {"received": True, "processed": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

## 🔍 Utilitários e Enums

### Enums Disponíveis

#### CurrencyEnum

```python
class CurrencyEnum(BaseEnum):
    BRL = "brl"    # Real Brasileiro
    USD = "usd"    # Dólar Americano
    EUR = "eur"    # Euro
```

#### PaymentMethodTypeEnum

```python
class PaymentMethodTypeEnum(BaseEnum):
    CARD = "card"
    PIX = "pix"
    BOLETO = "boleto"
    # ... outros métodos de pagamento
```

#### SubscriptionInterval

```python
class SubscriptionInterval(BaseEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"
```

#### SubscriptionStatus

```python
class SubscriptionStatus(BaseEnum):
    ACTIVE = "active"
    CANCELED = "canceled"
    INCOMPLETE = "incomplete"
    TRIALING = "trialing"
    PAST_DUE = "past_due"
    UNPAID = "unpaid"
    # ... outros status
```

## ⚙️ Configurações

### Settings Class

```python
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    STRIPE_PUBLIC_KEY: str = ""   # Chave pública do Stripe
    STRIPE_SECRET_KEY: str = ""   # Chave secreta do Stripe
```

### CORS Configuration

```python
ORIGINS = [
    "http://localhost:3000",    # React dev server
    "http://localhost:5173",    # Vite dev server
    "http://localhost:4173",    # Vite preview
    "http://localhost:4242",    # API local
]

METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
```

## 🚦 Como Executar

### Desenvolvimento Local

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Executar a aplicação
python main.py

# Ou usando uvicorn diretamente
uvicorn src.app:app --host 0.0.0.0 --port 4242 --reload
```

### Usando Makefile

```bash
# Formatação e linting
make lint-fix

# Executar aplicação (implementar se necessário)
make run
```

### Docker (Implementação Futura)

```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY . .
RUN pip install -e .

EXPOSE 4242
CMD ["python", "main.py"]
```

## 📋 Exemplos de Uso

### Fluxo Completo: E-commerce

#### 1. Criar Cliente

```bash
curl -X POST http://localhost:4242/customer/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@loja.com",
    "name": "Maria Santos",
    "address": {...},
    "shipping": {...},
    "metadata": {"user_id": "user_789"}
  }'
```

#### 2. Criar Produto e Preço

```bash
# Produto
curl -X POST http://localhost:4242/products/ \
  -d '{"name": "Curso Premium", "description": "Curso completo"}'

# Preço
curl -X POST http://localhost:4242/products/prices \
  -d '{
    "product_id": "prod_ABC",
    "unit_amount": 9900,
    "currency": "brl",
    "recurring": {"interval": "month"}
  }'
```

#### 3. Criar Assinatura

```bash
curl -X POST http://localhost:4242/subscriptions/ \
  -d '{
    "customer_id": "cus_123",
    "price_id": "price_456",
    "trial_period_days": 14
  }'
```

### Fluxo de Pagamento Único

#### 1. Criar Payment Intent

```bash
curl -X POST http://localhost:4242/payment-intents/ \
  -d '{
    "amount": 5000,
    "currency": "brl",
    "metadata": {"user_id": "user_789", "product_id": "prod_123"}
  }'
```

#### 2. No Frontend (JavaScript)

```javascript
const stripe = Stripe('pk_test_...');

// Confirmar pagamento
const {error} = await stripe.confirmCardPayment(client_secret, {
  payment_method: {
    card: cardElement,
    billing_details: {
      name: 'Maria Santos',
    },
  }
});
```

## 🔒 Segurança

### Boas Práticas Implementadas

1. **Validação de Entrada**:
   - Schemas Pydantic rigorosos
   - Validação de tipos e formatos
   - Sanitização automática

2. **Configuração Segura**:
   - Chaves em variáveis de ambiente
   - Separação teste/produção
   - CORS configurado

3. **Webhook Security**:
   - Verificação de assinatura
   - Validação de payload
   - Proteção contra replay

4. **Error Handling**:
   - Não exposição de dados sensíveis
   - Logs estruturados
   - Mensagens de erro padronizadas

### Checklist de Segurança

- [ ] Chaves do Stripe em ambiente seguro
- [ ] HTTPS em produção
- [ ] Webhook endpoints protegidos
- [ ] Rate limiting implementado
- [ ] Logs de auditoria
- [ ] Monitoramento ativo

## 🧪 Testes

### Testes com Stripe CLI

```bash
# Instalar Stripe CLI
# https://stripe.com/docs/stripe-cli

# Login
stripe login

# Escutar webhooks localmente
stripe listen --forward-to localhost:4242/webhooks

# Simular eventos
stripe trigger payment_intent.succeeded
```

### Testes Manuais

1. **Health Check**:

   ```bash
   curl http://localhost:4242/
   ```

2. **Criar e Testar Fluxos**:
   - Use as rotas documentadas
   - Verifique no Dashboard do Stripe
   - Teste casos de erro

### Dados de Teste do Stripe

```bash
# Cartões de teste
4242424242424242  # Visa aprovado
4000000000000002  # Cartão recusado
4000000000009995  # Cartão insuficiente

# PIX (Brasil)
# Use qualquer CPF válido em modo teste
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas e suporte:

- [Documentação oficial do Stripe](https://stripe.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
