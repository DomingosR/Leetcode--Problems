var reverseList = function(head) {
    let [previousNode, currentNode] = [null, head]
    
    while(currentNode) {
        [currentNode.next, previousNode, currentNode] = [previousNode, currentNode, currentNode.next]
    }
    
    return previousNode
};
