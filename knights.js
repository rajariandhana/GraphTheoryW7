// const fs = require('fs');

const knightMovesR = [1, 2, 2, 1, -1, -2, -2, -1];
const knightMovesC = [-2, -1, 1, 2, 2, 1, -1, -2];
let rows, columns, nNodes, sourceR, sourceC;

const nodes = {};
const vis = {};
const path = [];

function validCoord(r, c) {
    return r >= 0 && c >= 0 && r < rows && c < columns;
}

function Hamiltonian(r, c) {
    vis[sourceR][sourceC] = true;
    if (path.length === nNodes) return true;

    for (let i of nodes[r][c]) {
        const curR = i[0];
        const curC = i[1];
        if (!vis[curR][curC]) {
            vis[curR][curC] = true;
            path.push([curR, curC]);
            if (Hamiltonian(curR, curC)) return true;
            vis[curR][curC] = false;
            path.pop();
        }
    }
    return false;
}

function GeneratePath() {
    for (let i = 0; i < rows; i++) {
        vis[i] = {};
        for (let j = 0; j < columns; j++) {
            vis[i][j] = false;
        }
    }
    path.push([sourceR, sourceC]);
    if (Hamiltonian(sourceR, sourceC)) {
        path.forEach((i) => {
            console.log(i[0] + " " + i[1]);
        });
        return true;
    }
    return false
}

function main() {
    rows = parseInt(prompt("Number of rows: "));
    columns = parseInt(prompt("Number of columns: "));
    sourceR = parseInt(prompt("Source row: "));
    sourceC = parseInt(prompt("Source column: "));
    nNodes = rows * columns;

    for (let i = 0; i < rows; i++) {
        nodes[i] = {};
        for (let j = 0; j < columns; j++) {
            nodes[i][j] = [];
            for (let k = 0; k < 8; k++) {
                const newR = i + knightMovesR[k];
                const newC = j + knightMovesC[k];
                if (validCoord(newR, newC)) nodes[i][j].push([newR, newC]);
            }
        }
    }

    GeneratePath();

    const data = `${rows}\n${columns}\n${sourceR}\n${sourceC}\n${nNodes}\n` + path.map(p => `${p[0]} ${p[1]}`).join('\n');

    fs.writeFile('path.txt', data, (err) => {
        if (err) {
            console.error("Unable to open file for writing.");
        } else {
            console.log("Data exported to path.txt successfully.");
        }
    });
}

// main();
function ParseInput(){
    // console.log("hehe");
    rows = document.getElementById('n_row').value;
    columns = document.getElementById('n_column').value;
    nNodes = rows*columns;
    sourceR = document.getElementById('src_row').value;
    sourceC = document.getElementById('src_column').value;
    // console.log(rows);
    // console.log(columns);
    // console.log(sourceR);
    // console.log(sourceC);
    for (let i = 0; i < rows; i++) {
        nodes[i] = {};
        for (let j = 0; j < columns; j++) {
            nodes[i][j] = [];
            for (let k = 0; k < 8; k++) {
                const newR = i + knightMovesR[k];
                const newC = j + knightMovesC[k];
                if (validCoord(newR, newC)) nodes[i][j].push([newR, newC]);
            }
        }
    }
    if(GeneratePath()) GenerateGrid();
    else{
        const notFound = document.getElementById('notFound');
        notFound.classList.remove('hidden');
    }
}
function GenerateGrid() {
    const gridBody = document.getElementById('gridBody');
    gridBody.innerHTML = '';
    gridClassName = 'grid-cols-'+columns;
    gridBody.classList.add(gridClassName);
    gridBody.classList.remove('hidden');
    for(let r=0; r<rows; r++){
        // let newRow = document.createElement('tr');
        for(let c=0; c<columns; c++)
        {
            let cell = document.createElement('td');
            cell.id = r.toString()+"_"+c.toString();
            cell.textContent = '';
            cell.classList.add('h-12','w-12','bg-indigo-200','flex','items-center','justify-center','text-center','rounded-md');
            gridBody.appendChild(cell);
            // newRow.appendChild(cell);
        }
        // gridBody.appendChild(newRow);
    }

    let index = 0;
    const interval = setInterval(() => {
        if (index < path.length) {
            const [r, c] = path[index];
            gridId = r.toString()+"_"+c.toString()
            const cell = document.getElementById(gridId);
            cell.classList.remove('bg-indigo-200');
            cell.classList.add('bg-rose-400', 'text-white');
            cell.textContent = index + 1;
            index++;
        } else {
            clearInterval(interval);
        }
    }, 500);

}