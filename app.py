from flask import Flask, render_template,request, jsonify, flash, redirect, url_for
from forex_python.converter import CurrencyRates, CurrencyCodes
from check_vaidity import validity

# valid = validity()
codes = CurrencyCodes()
c = CurrencyRates()
app = Flask(__name__)

app.config['SECRET_KEY'] = "d2f35gg452fergerty"


@app.route('/')
def main_page():
    ''' Sends to main Page and form'''
    return render_template('index.html')

@app.route('/get-currency')
def requested_curency():
    """ Receaves values from form and renders result """
    # print(request.args)
    from_curency = request.args['from'].upper()
    to_curency = request.args['to'].upper()
    amount = request.args['amount']

    rates = c.get_rates('USD')
    
    errorsList = validity(rates, from_curency, to_curency, amount)
    if len(errorsList) > 0:
        for err in errorsList:
            flash(f"{err}")
        return redirect(url_for('main_page'))
    

    simbol = codes.get_symbol(to_curency)
    convert = c.convert(from_curency, to_curency, float(amount))
    convert = round(convert, 2)
    
    return render_template('result.html', convert=convert, symbol=simbol)
   


    # return  jsonify({'from':from_curency, 'to': to_curency, 'amount': amount, 'converted': convert, 'symbol': simbol, 'rates': rates})
    # return render_template('result.html', convert=convert, symbol=simbol)