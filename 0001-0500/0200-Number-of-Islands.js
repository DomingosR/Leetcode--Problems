var numIslands = function(grid) {
    let m = grid.length;
    let firstRow = grid[0];
    let n = firstRow.length;
    let numIslands = 0;
    let cellList = [];
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === "1") {
                numIslands++;
                grid[i][j] = "0";
                
                cellList.push([i, j]);
                
                while (cellList.length > 0) {
                    let currPair = cellList.pop();
                    let currI = currPair[0];
                    let currJ = currPair[1];
                    
                    if (currI > 0 && grid[currI - 1][currJ] === "1") {
                        grid[currI - 1][currJ] = "0";
                        cellList.push([currI - 1, currJ]);
                    }
                    if (currI < m - 1 && grid[currI + 1][currJ] === "1") {
                        grid[currI + 1][currJ] = "0";
                        cellList.push([currI + 1, currJ]);
                    }   
                    if (currJ > 0 && grid[currI][currJ - 1] === "1") {
                        grid[currI][currJ - 1] = "0";
                        cellList.push([currI, currJ - 1]);
                    }   
                    if (currJ < n - 1 && grid[currI][currJ + 1] === "1") {
                        grid[currI][currJ + 1] = "0";
                        cellList.push([currI, currJ + 1]);
                    }                      
                }
            }
        }
    }
    
    return numIslands;
};