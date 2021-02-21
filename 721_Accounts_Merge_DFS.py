'''
Accounts is a list of strings with elements:
    [0]     : name
    [1:]    : associated emails

Goal: Merge accounts
    - Accounts can be merged ONLY IF they contain ANY common email (and will have the same name)
    - Accounts CANNOT be merged SOLELY by similar name, but accounts belonging to the same user have the same name

Return accounts in the same format, merged, EMAILS SORTED in ascending order

'''

from typing import List
from collections import defaultdict

class Solution:
    # Given an account, return the account with distinct emails sorted ascending
    def sortAccount(self, account: List[str]) -> List[str]:
        sortedAcc = [account[0]]
        emails = list(set(account[1:]))
        emails.sort()
        sortedAcc.extend(emails)
        
        return sortedAcc
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Edge case
        if(len(accounts) == 1):
            return [self.sortAccount(accounts[0])]
        
        # Map email address to list of account indices associated with email
        emailAccs = defaultdict(list)
        for accIndex in range(len(accounts)):
            currAcc = accounts[accIndex]
            for emailIndex in range(1, len(currAcc)):
                currEmail = currAcc[emailIndex]
                emailAccs[currEmail].append(accIndex)
        
        # Perform DFS traversal, accounts are adjacent if they share an email
        visited = [False] * len(accounts)
        
        # Given an account index, accumulate and return all associated emails,
        # expanding accounts with overlapping emails
        def dfs(accIndex: int, emails: set[str]) -> set[str]:
            if(visited[accIndex]):
                return emails
            visited[accIndex] = True
            
            for email in accounts[accIndex][1:]:
                emails.add(email)                           # Add each email associated with this account 
                for adjAccIndex in emailAccs[email]:        # For each account also associated with this email, perform DFS (they are linked)
                    emails = dfs(adjAccIndex, emails)
    
            return emails
        
        # Build sorted output, emails are merged through DFS
        output = []
        for accIndex in range(len(accounts)):
            if not visited[accIndex]:
                mergedAcc = [accounts[accIndex][0]]         # Store account name
                emails = dfs(accIndex, set([]))             # Obtain merged emails
                mergedAcc.extend(list(emails))              
                output.append(self.sortAccount(mergedAcc))  
    
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        