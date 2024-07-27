var timeRequiredToBuy = function(tickets, k) {
    let numUnitsTime = 0;
    let targetTickets = tickets[k];

    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) {
            numUnitsTime += Math.min(targetTickets, tickets[i]);
        } else {
            numUnitsTime += Math.min(targetTickets - 1, tickets[i]);
        }
    }

    return numUnitsTime;
};
