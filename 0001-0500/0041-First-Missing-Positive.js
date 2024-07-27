var firstMissingPositive = function(nums) {
    let n = nums.length;
    
    for (let i = 0; i < n; i++) {
        if(nums[i] <= 0) {
            nums[i] = n+1;
        }
    }
    
    for (i = 0; i < n; i++) {
        if (1 <= Math.abs(nums[i]) && Math.abs(nums[i]) <= n) {
            let index = Math.abs(nums[i]) - 1;
            if (nums[index] > 0) {
                nums[index] *= -1;
            }
        }
    }
    
    for (i = 0; i < n; i++) {
        if (nums[i] > 0) {
            return i+1;
        }
    }
    
    return n+1;
};