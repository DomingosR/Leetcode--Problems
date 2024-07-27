var countSubarrays = function(nums, k) {
    let maxVal = Math.max(...nums);
    let numSubArrays = 0;
    let currentCount = 0;
    let j = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === maxVal) {
            currentCount++;
        }
        while (currentCount >= k) {
            if (nums[j] === maxVal) {
                currentCount--;
            }
            j++;
        }
        numSubArrays += j;
    }

    return numSubArrays;
};
