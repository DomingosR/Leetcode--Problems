var numSubarrayProductLessThanK = function(nums, k) {
    if (k === 0) {
        return 0;
    }
    
    let n = nums.length;
    let subArrayCount = 0;
    let j = 0;
    let currentProduct = 1;
    
    for (let i = 0; i < n; i++) {
        currentProduct *= nums[i];
        while (j <= i && currentProduct >= k) {
            currentProduct /= nums[j];
            j ++;
        }
        subArrayCount += (i - j + 1);
    }
    
    return subArrayCount;
};