var islandPerimeter = function(grid) {
    let m = grid.length;
    let firstRow = grid[0];
    let n = firstRow.length;
    let perimeter = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                perimeter += 4;
                if (i > 0 && grid[i-1][j] == 1) perimeter -= 1;
                if (i < m-1 && grid[i+1][j] == 1) perimeter -= 1;
                if (j > 0 && grid[i][j-1] == 1) perimeter -= 1;
                if (j < n-1 && grid[i][j+1] == 1) perimeter -= 1;
            }
        }
    }

    return perimeter;