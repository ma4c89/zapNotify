# 📲 Automação de Envio de Mensagens pelo WhatsApp Web

<br> 

## 📖 Descrição

Este projeto é uma automação desenvolvida em **Python** para enviar mensagens personalizadas pelo **WhatsApp Web** utilizando dados armazenados em uma planilha do Excel.

O programa lê as informações dos clientes, como nome, telefone e data de vencimento, gera uma mensagem personalizada e envia automaticamente pelo WhatsApp Web.

Além disso, caso ocorra algum erro durante o envio, o sistema registra os dados do cliente em um arquivo de erros para facilitar futuras verificações.

---

## ✨ Funcionalidades

* 📄 Leitura de clientes a partir de uma planilha Excel (.xlsx)
* 👤 Personalização automática da mensagem com o nome do cliente
* 📅 Inclusão da data de vencimento formatada
* 💬 Envio automático de mensagens pelo WhatsApp Web
* ❌ Registro de falhas em um arquivo `erros.csv`
* 🖥️ Automatização de cliques utilizando PyAutoGUI

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* OpenPyXL
* PyAutoGUI
* Webbrowser
* Urllib
* Time

---

## 📋 Estrutura da Planilha

A planilha deve possuir uma aba chamada **cliente** contendo as informações dos clientes.

Exemplo:

| CELULAR         | DATA DE VENCIMENTO | VALOR     | PRODUTO       | STATUS   | PAGO |
| --------------- | ------------------ | --------- | ------------- | -------- | ---- |

---

### 📊 Controle Automático de Status

A planilha do Excel utiliza uma fórmula para atualizar automaticamente o status do pagamento de cada cliente:

* 🟢 **PAGO** – Quando a coluna **PAGO** contém "Sim".
* 🔴 **ATRASADO** – Quando a data de vencimento é anterior à data atual.
* 🟡 **VENCE HOJE** – Quando o vencimento é na data atual.
* 🔵 **NO PRAZO** – Quando o vencimento ainda não chegou.

Fórmula utilizada no Excel:

```excel
=SE(F3="";"";SE(J3="Sim";"PAGO";SE(F3<HOJE();"ATRASADO";SE(F3=HOJE();"VENCE HOJE";"NO PRAZO"))))
```


## ⚠️ Observações

* É necessário possuir uma conta ativa no WhatsApp.
* O WhatsApp Web deve ser acessado e autenticado por meio do QR Code antes do envio das mensagens.
* As coordenadas utilizadas pelo PyAutoGUI (`x` e `y`) podem variar conforme a resolução da tela. Caso necessário, ajuste-as para o seu computador.
* A planilha deve estar no mesmo diretório do programa.
