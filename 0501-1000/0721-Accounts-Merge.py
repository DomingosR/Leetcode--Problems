class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailAccounts = defaultdict(list)
        
        # For each email address, make list of accounts that have it
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in emailAccounts:
                    emailAccounts[email] = [False]
                emailAccounts[email].append(i)
        
        # Indicator for whether an input account has been processed
        processed = [False] * len(accounts)
        
        # Final list of merged account
        userAccounts = []
        
        # Function to process individual input account
        def processInputUser(i, currentListOfEMails, originalAccount):
            
            # Only run function if input account has not been processed yet
            if not processed[i]:
                
                # Mark input account as processed
                processed[i] = True
                
                # Work with each email address in that input account
                for j in range(1, len(accounts[i])):
                    
                    # Getting email address
                    email = accounts[i][j]
                    
                    # Checking if email address has been processed
                    if not emailAccounts[email][0]:
                        
                        # Mark email address as processed, append to list
                        currentListOfEMails.append(email)
                        emailAccounts[email][0] = True
                        
                        # Process each of the email accounts associated with that email
                        for k in range(1, len(emailAccounts[email])):
                            processInputUser(emailAccounts[email][k], currentListOfEMails, originalAccount)
                
                # Finally, if we're working in the account first called, add final list to output
                if i == originalAccount:
                    finalListOfEMails = currentListOfEMails.copy()
                    userAccounts.append([accounts[i][0]] + sorted(finalListOfEMails))
        
        # Process each input account
        for i in range(len(accounts)):
            processInputUser(i, [], i)
            
        return userAccounts 