const spaces = document.querySelectorAll('.box');
var gameLive = true;
var player = 1;
var pcs1 = 0;
var pcs2 = 0;
var pcs3 = 0;
var pcs4 = 0;
var pcs5 = 0;
var pcs6 = 0;
var pcs7 = 0;
var moves = 0;

var pcs = [pcs1, pcs2, pcs3, pcs4, pcs5, pcs6, pcs7];

const row1 = [spaces[0], spaces[1], spaces[2], spaces[3], spaces[4], spaces[5], spaces[6]];
const row2 = [spaces[7], spaces[8], spaces[9], spaces[10], spaces[11], spaces[12], spaces[13]];
const row3 = [spaces[14], spaces[15], spaces[16], spaces[17], spaces[18], spaces[19], spaces[20]];
const row4 = [spaces[21], spaces[22], spaces[23], spaces[24], spaces[25], spaces[26], spaces[27]];
const row5 = [spaces[28], spaces[29], spaces[30], spaces[31], spaces[32], spaces[33], spaces[34]];
const row6 = [spaces[35], spaces[36], spaces[37], spaces[38], spaces[39], spaces[40], spaces[41]];

const col1 = [spaces[0], spaces[7], spaces[14], spaces[21], spaces[28], spaces[35]];
const col2 = [spaces[1], spaces[8], spaces[15], spaces[22], spaces[29], spaces[36]];
const col3 = [spaces[2], spaces[9], spaces[16], spaces[23], spaces[30], spaces[37]];
const col4 = [spaces[3], spaces[10], spaces[17], spaces[24], spaces[31], spaces[38]];
const col5 = [spaces[4], spaces[11], spaces[18], spaces[25], spaces[32], spaces[39]];
const col6 = [spaces[5], spaces[12], spaces[19], spaces[26], spaces[33], spaces[40]];
const col7 = [spaces[6], spaces[13], spaces[20], spaces[27], spaces[34], spaces[41]];

const columns = [col1, col2, col3, col4, col5, col6, col7];
const rows = [row1, row2, row3, row4, row5, row6];

function dropChecker(id) {
    if (pcs[id] >= 6) {
        alert("this column is full!");
    } else {
        if (player == 1) {
            columns[id][5 - pcs[id]].style.background = 'purple';
            player = 2;
        } else {
            columns[id][5 - pcs[id]].style.background = 'green';
            player = 1;
        }
        pcs[id] += 1;
        moves += 1;
        if (moves == 42) {
            alert("Draw!!!!!");
        }
        if (moves > 6) {
            if (player == 2) {
                winCheck1();
            } else {
                winCheck2();
            }
        }
    }
}

function winCheck1() {
    var count = 0;
    // First we will check for vertical wins
    for (let _col = 0; _col < 7; _col++) {
        for (let _row = 5; _row > -1; _row--) {
            if (columns[_col][_row].style.background == 'purple') {
                count += 1;
                if (count >= 4) {
                    alert("PLAYER 1 WINS!!!");
                }
            } else {
                count = 0;
            }
        }
    }

    count = 0;

    for (_row = 0; _row < 6; _row++) {
        for (_col = 0; _col < 7; _col++) {
            if (rows[_row][_col].style.background == 'purple') {
                count += 1;
                if (count >= 4) {
                    alert("PLAYER 1 WINS!!!");
                }
            } else {
                count = 0;
            }
        }
    }
}


function winCheck2() {
    var count = 0;

    for (let _col = 0; _col < 7; _col++) {
        for (let _row = 5; _row > -1; _row--) {
            if (columns[_col][_row].style.background == 'green') {
                count += 1;
                if (count >= 4) {
                    alert("PLAYER 2 WINS!!!");
                }
            } else {
                count = 0;
            }
        }
    }

    count = 0;

    for (_row = 0; _row < 6; _row++) {
        for (_col = 0; _col < 7; _col++) {
            if (rows[_row][_col].style.background == 'green') {
                count += 1;
                if (count >= 4) {
                    alert("PLAYER 2 WINS!!!");
                }
            } else {
                count = 0;
            }
        }
    }
}


