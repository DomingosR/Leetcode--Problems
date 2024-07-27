var trap = function(height) {
    let maxHeight = height.reduce((a, b) => (Math.max(a, b) || 0));
    let numWalls = height.length;
    let totalWaterTrapped = 0;
    
    let i = 0;
    let maxHeightLeft = 0;
    while(height[i] < maxHeight) {
        maxHeightLeft = Math.max(maxHeightLeft, height[i]);
        totalWaterTrapped += (maxHeightLeft - height[i]);
        i += 1;
    }

    let j = numWalls - 1;
    let maxHeightRight = 0;
    while(height[j] < maxHeight) {
        maxHeightRight = Math.max(maxHeightRight, height[j]);
        totalWaterTrapped += (maxHeightRight - height[j]);
        j -= 1;
    }
    
    while (i < j) {
        totalWaterTrapped += (maxHeight - height[i]);
        i += 1;
    }
    
    return totalWaterTrapped;
};