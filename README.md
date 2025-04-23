# 🛠️ Processo de Montagem - Simulação com Python

Este repositório contém um script em Python que simula o **processo de montagem de componentes automotivos** com foco em portas de carros, usando **orientação a objetos (OOP)** para representar as etapas de montagem na linha de produção.

## 🚗 Objetivo

O projeto tem como objetivo:

- Praticar conceitos de **herança, métodos e classes** em Python.
- Representar o fluxo de montagem de forma clara e didática.
- Criar uma estrutura reaproveitável para simulações de montagem.

## 🧩 Estrutura do Código

- `DS06`: Classe base com métodos genéricos como pegar peça, posicionar, usar apertadeira e definir bolt.
- `Passo1_Handle`: Representa a montagem da handle e do bracket.
- `Passo2_Latch`: Representa a montagem da latch e sua fixação.
- `Passo3_Sash`: Representa a montagem do sash e canaleta (channel).

Cada passo herda os métodos da classe base `DS06`.


