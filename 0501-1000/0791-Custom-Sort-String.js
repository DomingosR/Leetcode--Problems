var customSortString = function(order, s) {
    let charMap = {};

    for (let i = 0; i < order.length; i++) {
        charMap[order[i]] = i;
    }

    for (let i = 0; i < s.length; i++) {
        if (charMap[s[i]] == undefined) {
            charMap[s[i]] = 100;
        }
    }
    
    s = s.split("");
    return s.sort((a, b) => charMap[a] - charMap[b]).join("");

};