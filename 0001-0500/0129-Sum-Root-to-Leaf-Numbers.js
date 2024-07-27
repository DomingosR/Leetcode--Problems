var sumNumbers = function(root) {
    let totalSum = 0;
    
    function processNode(currentNode, numStr) {
        numStr += currentNode.val;
        if (!currentNode.left && !currentNode.right) totalSum += +numStr;
        if (currentNode.left ) processNode(currentNode.left , numStr);
        if (currentNode.right) processNode(currentNode.right, numStr);        
    }
    
    processNode(root, "");
    return totalSum;
};
