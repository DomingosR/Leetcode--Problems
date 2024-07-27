var middleNode = function(head) {
    if (head.next == null) {
        return head;
    }

    slow = head;
    fast = head.next;

    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow.next;
};
