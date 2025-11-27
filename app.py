from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Examen CI/CD - Cadena</title>
            <style>
                body { 
                    background: linear-gradient(135deg, #00c6ff, #0072ff);
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 50px;
                    color: #fff;
                }
                h1 { 
                    font-size: 2.5em;
                    text-shadow: 1px 1px 3px #000;
                }
                #board {
                    display: grid;
                    grid-template-columns: repeat(3, 120px);
                    grid-gap: 10px;
                    justify-content: center;
                    margin-top: 30px;
                }
                .cell {
                    background: white;
                    color: #0072ff;
                    border-radius: 12px;
                    font-size: 2.5em;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    cursor: pointer;
                }
                .cell:hover { background: #e6f0ff; }
                #status {
                    margin-top: 20px;
                    font-size: 20px;
                    font-weight: bold;
                }
                button {
                    padding: 12px 25px;
                    font-size: 18px;
                    background: #fff;
                    color: #0072ff;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    margin-top: 20px;
                }
                button:hover { background: #e6f0ff; }
            </style>
        </head>
        <body>
            <h1>Examen CI/CD - Cadena</h1>
            <p>Aplicación Flask corriendo con Docker + GitHub Actions + Traefik</p>

            <div id="board"></div>
            <div id="status">Turno de X</div>
            <button onclick="resetGame()">Reiniciar</button>

            <script>
                let board = ["", "", "", "", "", "", "", "", ""];
                let currentPlayer = "X";
                let gameActive = true;

                const boardElement = document.getElementById("board");
                const statusElement = document.getElementById("status");

                function renderBoard() {
                    boardElement.innerHTML = "";
                    board.forEach((cell, index) => {
                        const el = document.createElement("div");
                        el.classList.add("cell");
                        el.textContent = cell;
                        el.onclick = () => makeMove(index);
                        boardElement.appendChild(el);
                    });
                }

                function makeMove(i) {
                    if (!gameActive || board[i] !== "") return;

                    board[i] = currentPlayer;

                    if (checkWinner()) {
                        statusElement.textContent = "Ganó " + currentPlayer;
                        gameActive = false;
                    } else if (board.every(c => c !== "")) {
                        statusElement.textContent = "Empate";
                        gameActive = false;
                    } else {
                        currentPlayer = currentPlayer === "X" ? "O" : "X";
                        statusElement.textContent = "Turno de " + currentPlayer;
                    }

                    renderBoard();
                }

                function checkWinner() {
                    const wins = [
                        [0,1,2],[3,4,5],[6,7,8],
                        [0,3,6],[1,4,7],[2,5,8],
                        [0,4,8],[2,4,6]
                    ];
                    return wins.some(w => w.every(i => board[i] === currentPlayer));
                }

                function resetGame() {
                    board = ["", "", "", "", "", "", "", "", ""];
                    currentPlayer = "X";
                    gameActive = true;
                    statusElement.textContent = "Turno de X";
                    renderBoard();
                }

                renderBoard();
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1002)
