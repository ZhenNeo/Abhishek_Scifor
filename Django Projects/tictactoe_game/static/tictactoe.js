document.addEventListener('DOMContentLoaded', function () {
    const cells = document.querySelectorAll('.cell');
    const winningCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Vertical
        [0, 4, 8], [2, 4, 6] // Diagonal
    ];

    let currentPlayer = 'X';
    let gameOver = false;

    cells.forEach(cell => {
        cell.addEventListener('click', handleClick, { once: true });
    });

    function handleClick(e) {
        const cell = e.target;
        if (!gameOver && cell.textContent === '') {
            cell.textContent = currentPlayer;
            if (checkWin(currentPlayer)) {
                gameOver = true;
                message.textContent = currentPlayer + ' wins!';
            } else if (checkDraw()) {
                gameOver = true;
                message.textContent = 'It\'s a draw!';
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }
        }
    }

    function checkWin(player) {
        return winningCombos.some(combo => {
            return combo.every(index => {
                return cells[index].textContent === player;
            });
        });
    }

    function checkDraw() {
        return [...cells].every(cell => {
            return cell.textContent !== '';
        });
    }

    function resetGame() {
        cells.forEach(cell => {
            cell.textContent = '';
            cell.removeEventListener('click', handleClick);
        });
        currentPlayer = 'X';
        gameOver = false;
    
        cells.forEach(cell => {
            cell.addEventListener('click', handleClick);
        });
    }
});
