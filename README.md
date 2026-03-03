# Calculadora de Jogos (Meta Mensal)

Uma página HTML simples (sem dependências) que calcula **quantos jogos você precisa fazer no mês** para atingir uma **meta em R$**, considerando **custos fixos** e **custo por jogo**, além de mostrar médias por **semana** e por **dia**.

---

## ✅ O que esse projeto faz

A partir dos dados informados, a calculadora retorna:

- **Lucro por jogo** (valor recebido − custo por jogo)
- **Jogos necessários no mês** (arredondado para cima)
- **Média de jogos por semana**
- **Média de jogos por dia**, com base nos dias trabalhados por semana
- Estimativas financeiras:
  - **Receita bruta**
  - **Custos variáveis**
  - **Custos fixos**
  - **Receita líquida estimada**

---

## 🧮 Como é feito o cálculo

### 1) Lucro por jogo
```txt
lucroPorJogo = valorPorJogo - custoPorJogo