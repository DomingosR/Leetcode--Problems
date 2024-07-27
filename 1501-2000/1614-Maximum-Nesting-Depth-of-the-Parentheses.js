var maxDepth = function(s) {
    let maxDepth = 0;
    let currDepth = 0;
    
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (char === "(") {
            currDepth++;
            maxDepth = Math.max(maxDepth, currDepth);
        }
        if (char === ")") {
            currDepth--;
        }
    }
    
    return maxDepth;
};