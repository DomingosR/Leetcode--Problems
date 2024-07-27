var countStudents = function(students, sandwiches) {
    let n = students.length;
    let countOne = students.reduce((a, b) => a + b, 0);
    let countZero = n - countOne;
    
    for (let i = 0; i < n; i++) {
        if (sandwiches[i] === 0) {
            if (countZero === 0) {
                return n - i;
            } else {
                countZero--;
            }
        }
        if (sandwiches[i] === 1) {
            if (countOne === 0) {
                return n - i;
            } else {
                countOne--;
            }
        }        
    }
    
    return 0;
    
};