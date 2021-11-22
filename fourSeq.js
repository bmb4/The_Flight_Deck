var player1_username = '';
var player2_username = '';

$(document).ready(function() {
    var player1 = prompt("Please enter first player's username:", '');
    var player2 = prompt("Please enter second player's your username:", '');
    $.ajax({
        type: 'POST',
        url: '/verify_users',
        data: JSON.stringify([player1, player2]),
        success: function(data) {
            if (data == "invalid") {
                alert("Entered invalid username(s). Going back to landing page......");
                location.href = "/landingpage";
            }
            else { player1_username = player1; player2_username = player2; }
        }
    });
});

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
const _purple = "rgb(120, 0, 138)";
const _green = "rgb(0, 215, 0)";
const _orange = "rgb(255, 103, 0)";
const _yellow = "rgb(250, 237, 39)";
var win_indices = [0, 0, 0, 0, 0, 0, 0, 0];


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

function game_result(isDraw, winner, loser) {
    $.ajax({
        type: 'POST',
        url: '/game_result',
        data: JSON.stringify({isDraw: isDraw, winner: winner, loser: loser}),
        success: function(data){
            $(".modal-title").html(data);
            $("#endgameModal").modal();
            $(".gamebutton").each(function() {
                $(this).prop("disabled", true);
            });
        }
    });
}

function dropChecker(id) {
    if (pcs[id] >= 6) {
        alert("this column is full!");
    } else {
        if (player == 1) {
            columns[id][5 - pcs[id]].style.background = _purple;
            player = 2;
        } else {
            columns[id][5 - pcs[id]].style.background = _green;
            player = 1;
        }
        pcs[id] += 1;
        moves += 1;
        if (moves == 42) {
//            alert("Draw!!!!!");
            game_result(true, player1_username, player2_username);
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
    var iterations = 0;
    var _colSlide = 0;
    var _rowPush = 0;

    // First we will check for vertical wins
    for (let _col = 0; _col < 7; _col++) {
        count = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _row = 5; _row > -1; _row--) {
            let check = columns[_col][_row];
            if (window.getComputedStyle(check).backgroundColor == _purple) {
                count += 1;
                win_indices[(2 * count) - 2] = _col;
                win_indices[(2 * count) - 1] = _row;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        columns[win_indices[i]][win_indices[i + 1]].style.background = _orange;
                    }
                    game_result(false, player1_username, player2_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
        }
    }

    // Next check for horizontal wins
    for (let _row = 0; _row < 6; _row++) {
        count = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _col = 0; _col < 7; _col++) {
            let check = rows[_row][_col];
            if (window.getComputedStyle(check).backgroundColor == _purple) {
                count += 1;
                win_indices[(2 * count) - 2] = _row;
                win_indices[(2 * count) - 1] = _col;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _orange;
                    }
                    game_result(false, player1_username, player2_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
        }
    }

    // negative sloping diagonal wins 
    // on bottom half of the board
    // if slicing along row0,col0 to row5, col5
    for (let _row = 0; _row < 3; _row++) {
        count = 0;
        _rowPush = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _col = 0; _col < (6 - iterations); _col++) {
            let check = rows[_row + _rowPush][_col];
            if (window.getComputedStyle(check).backgroundColor == _purple) {
                count += 1;
                win_indices[(2 * count) - 2] = _row + _rowPush;
                win_indices[(2 * count) - 1] = _col;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _orange;
                    }
                    game_result(false, player1_username, player2_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
            _rowPush += 1;
        }
        iterations += 1;
    }

    // negative sloping diagonal wins 
    // on top half of the board
    // if slicing along row0,col0 to row5, col5
    iterations = 0;
    for (let _col = 1; _col < 4; _col++) {
        count = 0;
        _colSlide = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _row = 0; _row < (6 - iterations); _row++) {
            let check = rows[_row][_col + _colSlide];
            if (window.getComputedStyle(check).backgroundColor == _purple) {
                count += 1;
                win_indices[(2 * count) - 2] = _row;
                win_indices[(2 * count) - 1] = _col + _colSlide;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _orange;
                    }
                    game_result(false, player1_username, player2_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }    
            _colSlide += 1;
        }
        iterations += 1;
    }

    // positive sloping diagonal wins
    // on top half of board
    // if slicing along col0, row6 to col5, row0
    iterations = 0;
    for (let _row = 5; _row > 2; _row--) {
        count = 0;
        _rowPush = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _col = 0; _col < (6 - iterations); _col++) {
            let check = rows[_row - _rowPush][_col];
            if (window.getComputedStyle(check).backgroundColor == _purple) {
                count += 1;
                win_indices[(2 * count) - 2] = _row - _rowPush;
                win_indices[(2 * count) - 1] = _col;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _orange;
                    }
                    game_result(false, player1_username, player2_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
            _rowPush += 1;
        }
        iterations += 1;
    }

    // positive sloping diagonal wins
    // on bottom half of board
    // if slicing along col0, row6 to col5, row0
    iterations = 0;
    for (let _col = 1; _col < 4; _col++) {
        count = 0;
        _colSlide = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _row = 5; _row > (iterations - 1); _row--) {
            let check = rows[_row][_col + _colSlide];
            if (window.getComputedStyle(check).backgroundColor == _purple) {
                count += 1;
                win_indices[(2 * count) - 2] = _row;
                win_indices[(2 * count) - 1] = _col + _colSlide;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _orange;
                    }
                    game_result(false, player1_username, player2_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
            _colSlide += 1;
        }
        iterations += 1;       
    }
}


function winCheck2() {
var count = 0;          
    var iterations = 0;
    var _colSlide = 0;
    var _rowPush = 0;

    // First we will check for vertical wins
    for (let _col = 0; _col < 7; _col++) {
        count = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _row = 5; _row > -1; _row--) {
            let check = columns[_col][_row];
            if (window.getComputedStyle(check).backgroundColor == _green) {
                count += 1;
                win_indices[(2 * count) - 2] = _col;
                win_indices[(2 * count) - 1] = _row;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        columns[win_indices[i]][win_indices[i + 1]].style.background = _yellow;
                    }
                    game_result(false, player2_username, player1_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
        }
    }

    // Next check for horizontal wins
    for (let _row = 0; _row < 6; _row++) {
        count = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _col = 0; _col < 7; _col++) {
            let check = rows[_row][_col];
            if (window.getComputedStyle(check).backgroundColor == _green) {
                count += 1;
                win_indices[(2 * count) - 2] = _row;
                win_indices[(2 * count) - 1] = _col;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _yellow;
                    }
                    game_result(false, player2_username, player1_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
        }
    }

    // negative sloping diagonal wins 
    // on bottom half of the board
    // if slicing along row0,col0 to row5, col5
    for (let _row = 0; _row < 3; _row++) {
        count = 0;
        _rowPush = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _col = 0; _col < (6 - iterations); _col++) {
            let check = rows[_row + _rowPush][_col];
            if (window.getComputedStyle(check).backgroundColor == _green) {
                count += 1;
                win_indices[(2 * count) - 2] = _row + _rowPush;
                win_indices[(2 * count) - 1] = _col;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _yellow;
                    }
                    game_result(false, player2_username, player1_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
            _rowPush += 1;
        }
        iterations += 1;
    }

    // negative sloping diagonal wins 
    // on top half of the board
    // if slicing along row0,col0 to row5, col5
    iterations = 0;
    for (let _col = 1; _col < 4; _col++) {
        count = 0;
        _colSlide = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _row = 0; _row < (6 - iterations); _row++) {
            let check = rows[_row][_col + _colSlide];
            if (window.getComputedStyle(check).backgroundColor == _green) {
                count += 1;
                win_indices[(2 * count) - 2] = _row;
                win_indices[(2 * count) - 1] = _col + _colSlide;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _yellow;
                    }
                    game_result(false, player2_username, player1_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }    
            _colSlide += 1;
        }
        iterations += 1;
    }

    // positive sloping diagonal wins
    // on top half of board
    // if slicing along col0, row6 to col5, row0
    iterations = 0;
    for (let _row = 5; _row > 2; _row--) {
        count = 0;
        _rowPush = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _col = 0; _col < (6 - iterations); _col++) {
            let check = rows[_row - _rowPush][_col];
            if (window.getComputedStyle(check).backgroundColor == _green) {
                count += 1;
                win_indices[(2 * count) - 2] = _row - _rowPush;
                win_indices[(2 * count) - 1] = _col;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _yellow;
                    }
                    game_result(false, player2_username, player1_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
            _rowPush += 1;
        }
        iterations += 1;
    }

    // positive sloping diagonal wins
    // on bottom half of board
    // if slicing along col0, row6 to col5, row0
    iterations = 0;
    for (let _col = 1; _col < 4; _col++) {
        count = 0;
        _colSlide = 0;
        win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
        for (let _row = 5; _row > (iterations - 1); _row--) {
            let check = rows[_row][_col + _colSlide];
            if (window.getComputedStyle(check).backgroundColor == _green) {
                count += 1;
                win_indices[(2 * count) - 2] = _row;
                win_indices[(2 * count) - 1] = _col + _colSlide;
                if (count >= 4) {
                    console.log(win_indices);
                    for( let i = 0; i < 8; i += 2) {
                        rows[win_indices[i]][win_indices[i + 1]].style.background = _yellow;
                    }
                    game_result(false, player2_username, player1_username);
                    return;
                }
            } else {
                count = 0;
                win_indices = [0, 0, 0, 0, 0, 0, 0, 0];
            }
            _colSlide += 1;
        }
        iterations += 1;       
    }
}
