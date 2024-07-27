var maxSubarrayLength = function(nums, k) {
    const n = nums.length;
    let longestGood = 0;
    let j = -1;
    let numCounter = {};

    for (let i = 0; i < n; i++) {
        let num = nums[i];
        numCounter[num] = (numCounter[num] || 0) + 1;
        while (numCounter[num] > k) {
            j += 1;
            numCounter[nums[j]] -= 1;
        }
        longestGood = Math.max(longestGood, i - j);
    }

    return longestGood;
};
