
window.onload = () => {
        
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    var values = urlParams.get('values');
    var sudoku = values.split('').map(value=>parseInt(value, 10));

    var new_val_raw_str = urlParams.get('new_val');
    var new_val_raw = new_val_raw_str.match(/.{1,2}/g);
    var new_val = extractNewVal(new_val_raw);
    console.log(sudoku);
    printValues(sudoku, new_val);
};

function extractNewVal(new_val_raw) {
    let new_val = [];

    for (const value_str of new_val_raw) {
        let value = parseInt(value_str, 23);
        let row = [];

        for (let i = 0; i < 9; i++) {
            let bit = (value >> i) & 0x0001;
            row.unshift(bit);

        }

        new_val.push(row);
    }

    return new_val;
}

function printValues(values, color) {
    let cases = document.getElementsByClassName('case_unique');

    for (let k = 0; k < 9; k++) {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {

                let x = Math.floor(k/3)*3 + i;
                let y = (k%3)*3 + j;
                let p = k*9 + i*3 + j;

                cases[p].innerHTML = values[x*9+y];
                cases[p].style = (!color[x][y])? "color: red" : "color: black" ;
            }     
        }      
    }

}
