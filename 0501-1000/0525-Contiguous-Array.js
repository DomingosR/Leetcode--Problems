var findMaxLength = function(nums) {
    let maxLen = 0;
    let currentSum = 0;
    let sumLocation = new Map();
    sumLocation.set(0, -1);

    for (let i = 0; i < nums.length; i++) {
        currentSum += 2 * nums[i] - 1;
        if(sumLocation.has(currentSum)) {
            maxLen = Math.max(maxLen, i - sumLocation.get(currentSum));
        } else {
            sumLocation.set(currentSum, i)
        }
    }

    return maxLen;
};
