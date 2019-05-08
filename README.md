# python-calculator-api
REST webservice que efetua calculos matematicos básicos

### Utilizando o projeto
Clonar esse repositório
```
git clone https://github.ibm.com/Matheus-de-Souza/python-calculator-api.git
```

Pelo terminal, dentro do diretório do projeto, executar
```
python app.py
```

### Endpoints
```
/Calc
```

Necessários passar 3 argumentos, sendo "x" e "y" os valores para efetuar a conta e "operator" informando qual operacao deve ser efetuada entre adicao (%2B), subtracao (-), multiplicacao (*) ou divisao (/).


---

```
/Calc_Completa
```

Necessário passar em somente 1 argumento "calculo", expressao a ser calculada. Ex: "Calc_Completa?calculo=2+3"


---
