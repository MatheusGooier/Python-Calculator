from flask import Flask, request, json, jsonify

app = Flask(__name__)

#Rota para a raiz do webservice, retorno simples de Home page
@app.route('/', methods=['POST'])
def home():
    return 'Home page'

#Rota para Calculadora com argumentos separados
@app.route('/Calc', methods=['POST'])
def Calc():
    #Variavel que recebe primeiro argumento X
    x = request.args.get('x')
    
    #variavel que recebe segundo argumento Y
    y = request.args.get('y')

    #variavel que recebe o operador (+, -, *, /) ===== to use +, send %2B
    operator = request.args.get('operador')

    if x is None or y is None or operator not in '+-*/':
        return jsonify(result='Nao foi informado um dos argumentos ou o operador!')    

    #Calcula o resultado da equacao
    resultado = eval(x + operator + y)
    
    return jsonify(result=resultado)


#Rota para operar Calculador recebendo tudo em um argumento
@app.route('/Calc_Completa', methods=['POST'])
def Calc_Completa():
    #Variavel que recebe todo o calculo
    calculo = request.args.get('calculo')
    if calculo is None:
        return jsonify(result='Erro ao efetuar calculo')    

    #Calcula o resultado da equacao 
    resultado = jsonify(result=(eval(calculo.replace("%2B","+"))))
    
    #Parametros de seguranca
    resultado.headers.add('Access-Control-Allow-Headers', 'content-type')
    resultado.headers.add('Access-Control-Allow-Origin', '*')

    return resultado
    

app.run()