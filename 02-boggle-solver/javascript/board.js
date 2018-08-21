'use strict';

class Board {
    /**
     * Constructor: initialize a board with given size and letter distribution
     * @param size: the board size
     * @param distribution: the array of characters to be sampled from
     */
    constructor(size, distribution) {
        this.size = size;
        this.distribution = distribution;
        this.board = [];
        this.initBoard();
    }

    /**
     * Return generated board
     * @return {Array}
     */
    get distriBoard() {
        return this.board;
    }

    /**
     * Return this board's size
     * @return {number} the board's size
     */
    get boardSize() {
        return this.board.length;
    }

    /**
     * Return neighbouring positions of the given position.
     * Navigating on the board is done horizontally, vertically and diagonally.
     * @param position: current position
     * @return {Array} an array of neighbouring tiles on the board
     */
    getNeighbours(position) {
        let neighbours = [];
        let row = position[0];
        let col = position[1];

        let adjRows = [row];
        let adjCols = [col];

        let sizeRange = Array.from(
            new Array(this.size),
            (val, index) => index
        );

        if (sizeRange.indexOf(row - 1) > -1) {
            adjRows.push(row - 1);
        }
        if (sizeRange.indexOf(row + 1) > -1) {
            adjRows.push(row + 1);
        }
        if (sizeRange.indexOf(col - 1) > -1) {
            adjCols.push(col - 1);
        }
        if (sizeRange.indexOf(col + 1) > -1) {
            adjCols.push(col + 1);
        }

        for (let i= 0; i < adjRows.length; i++) {
            for (let j = 0; j < adjCols.length; j++) {
                neighbours.push([i, j]);
            }
        }
        let ndx = neighbours.indexOf(position);
        if (neighbours.indexOf(position) > -1) {
            neighbours.splice(ndx, 1);
        }
        return neighbours
    }

    /**
     * Generate the board based on dice distribution from the new Boggle version.
     * The result is a 2 dimensional array/list containing randomly generated characters.
     */
    initBoard() {
        let distributionSize = this.distribution[0].length;
        for (let i = 0; i < this.size * this.size; i++) {
            let row = Math.floor(i / this.size);  // integer division
            let col = i % this.size;
            let diceThrow = Math.floor(Math.random() * (distributionSize - 1));
            this.board[row][col] = this.distribution[i][diceThrow]
        }
    }
}