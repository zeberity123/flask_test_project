from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')
        print(operation)
        if operation == 'add':
            result = number1 + number2
        elif operation == 'sub':
            result = number1 - number2
        elif operation == 'mul':
            result = number1 * number2
        elif operation == 'div':
            if number1 == 0:
                result = 0
            elif number2 == 0:
                result = 0
            else:
                result = number1 / number2
        
        return render_template('first_templates.html', result = result)
    else:
        return render_template('first_templates.html', result = None)
    

if __name__ == '__main__':
    app.run(debug=True)