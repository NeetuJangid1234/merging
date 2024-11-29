from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/data")
def data():
    print("dddddddddddddddddddddddddd")
    return jsonify({"meaage":"welcome to git "})


if __name__=='__main__':
    app.run(debug=True,port=5007,host='0.0.0.0')