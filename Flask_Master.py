from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/contacts/")
def contacts():
    developer_name='Bebra'
    developer_phone='88005553535'
    developer_adress='Улица Пушкина дом Колотушкина'
    return render_template('contacts.html',name=developer_name,phone=developer_phone,adress=developer_adress)


if __name__ == "__main__":
    app.run(debug=True)