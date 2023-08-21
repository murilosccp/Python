const cells = document.querySelectorAll(".row > div");
const message = document.querySelector("#message");
const resetBtn = document.querySelector("#reset");

let currentPlayer = "X";
let moves = 0;

const winningCombinations = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
];

const handleClick = (event) => {
  const cell = event.target;
  const index = Array.from(cell.parentNode.children).indexOf(cell);

  if (cell.textContent !== "") {
    return;
  }

  cell.textContent = currentPlayer;
  moves++;

  const winningMove = checkForWinningMove(currentPlayer);
  if (winningMove) {
    endGame("Player " + currentPlayer + " wins!");
  } else if (moves === 9) {
    endGame("It's a tie!");
  } else {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    message.textContent = "Player " + currentPlayer + "'s turn";
  }
};

const checkForWinningMove = (player) => {
  return winningCombinations.some((combination) => {
    return combination.every((index) => {
      return cells[index].textContent === player;
    });
  });
};

const endGame = (messageText) => {
  message.textContent = messageText;
  cells.forEach((cell) => {
    cell.removeEventListener("click", handleClick);
  });
  resetBtn.style.display = "block";
};

const startGame = () => {
  message.textContent = "Player " + currentPlayer + "'s turn";
  cells.forEach((cell) => {
    cell.addEventListener("click", handleClick);
  });
  resetBtn.style.display = "none";
  moves = 0;
  cells.forEach((cell) => {
    cell.textContent = "";
  });
};

resetBtn.addEventListener("click", startGame);

startGame();
