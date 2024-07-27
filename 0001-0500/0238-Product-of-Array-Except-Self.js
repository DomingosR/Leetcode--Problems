var productExceptSelf = function(nums) {
    let n = nums.length;
    let finalProd = new Array(n).fill(1);
    let leftProd = 1;
    let rightProd = 1;
    
    for (let i = 0; i < n; i++) {
        finalProd[i] = finalProd[i] * leftProd;
        leftProd = leftProd * nums[i];
        finalProd[n - 1 - i] = finalProd[n - 1 - i] * rightProd;
        rightProd = rightProd * nums[n - 1 - i]
    }
    
    return finalProd;
};
