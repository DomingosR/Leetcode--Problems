var makeGood = function(s) {
    let i = 0;
    
    while (i < s.length - 1) {
        if (Math.abs(s.charCodeAt(i) - s.charCodeAt(i+1)) === 32) {
            s = s.substring(0, i).concat(s.substring(i+2));
            i = 0;
        } else {
            i++;
        }
    }
    
    return s;
};
