var insert = function(intervals, newInterval) {
    let [leftEnd, rightEnd] = newInterval;
    let leftCollection = [];
    let rightCollection = [];

    for (const interval of intervals) {
        const [currentLeft, currentRight] = interval;

        if (currentRight < leftEnd) {
            leftCollection.push(interval);
        } else if (currentLeft > rightEnd) {
            rightCollection.push(interval);
        } else {
            leftEnd = Math.min(leftEnd, currentLeft);
            rightEnd = Math.max(rightEnd, currentRight);
        }
    }

    return [...leftCollection, [leftEnd, rightEnd], ...rightCollection];
};
