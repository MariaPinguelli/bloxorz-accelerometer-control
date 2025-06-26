# **Trabalho final de Interfaces Não Convencionais**

**Aluna:** Maria Fernanda Pinguelli Sodré

**RA:** 2046407

---

**Projeto escolhido:** Controle de Jogo por Acelerômetro

**Jogo escolhido:** [Bloxorz](https://www.crazygames.com.br/jogos/bloxorz)

---

## **Descrição Geral**  
Este projeto propõe o desenvolvimento de um controle o acelerômetro de um celular Android como interface de entrada para mover o bloco no jogo Bloxorz.

O código consiste em: 
1. **Aplicação Web**: Uma página HTML que captura os dados do acelerômetro do celular.  
2. **Servidor Flask**: Recebe os dados via WebSocket e traduz em setas direcionais do teclado do computador.  
3. **Integração com o Jogo**: O movimentos do celular vão corresponder as teclas do teclado do computador, e por sua vez vão controlar o bloco no jogo *Bloxorz*.  

A solução utiliza **Flask-SocketIO** para comunicação em tempo real e **pynput** para simular as teclas.

---

## **Materiais e Métodos**  

### **Materiais Necessários**  
- **Dispositivo móvel** (smartphone/tablet) com acelerômetro e navegador moderno.  
- **Computador** com Python instalado para executar o servidor.  
- **Jogo Bloxorz** aberto no navegador no seguinte link: https://www.crazygames.com.br/jogos/bloxorz.  

### **Métodos e Tecnologias**  
1. **Captura de Dados do Acelerômetro**  
   - Utiliza a API `DeviceMotionEvent` do JavaScript para ler os valores de aceleração (X, Y, Z).  
   - Suavização dos dados para evitar movimentos bruscos.  
   - Calibração inicial para definir a posição "neutra".  

2. **Comunicação em Tempo Real**  
   - **Flask-SocketIO** permite a troca de dados entre o navegador e o servidor via WebSocket.  
   - O servidor recebe os valores de inclinação e os converte em comandos de tecla (up, down, left, right).  

3. **Simulação de Teclas**  
   - A biblioteca **pynput** simula pressionamentos de teclas no computador.  
   - Implementação de um sistema de *cooldown* para evitar múltiplos movimentos acidentais.  

4. **Interface do Usuário**  
   - Página web que exibe os valores do acelerômetro em tempo real.  
   - Botões para **conexão** e **calibração** da posição neutra.  

---

## **Conclusão**  
Este projeto demonstra como Interfaces Não Convencionais (InCs) podem tornar a interação com jogos mais divertida e imersiva. E também serve como um protótipo para o desenvolvimento de interfaces mais imersivas e acessíveis, alinhando-se com os objetivos da disciplina de Interfaces Não Convencionais.