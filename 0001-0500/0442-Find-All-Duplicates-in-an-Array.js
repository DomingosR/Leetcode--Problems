var findDuplicates = function(nums) {
    let duplicates = [];

    for (let i = 0; i < nums.length; i++) {
        n = Math.abs(nums[i]);
        if (nums[n-1] < 0) {
            duplicates.push(n);
        }
        nums[n-1] *= -1;
    }

    return duplicates;
};
