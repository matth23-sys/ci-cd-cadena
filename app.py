from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>matth calculator</title>
            <style>
                body {
                    background: #121212;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 80px;
                }
                h1 {
                    font-size: 50px;
                    margin-bottom: 15px;
                }
                p {
                    font-size: 22px;
                    opacity: .8;
                }
            </style>
        </head>
        <body>
            <h1>matth calculator</h1>
            <p>hola mundo</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2407)
