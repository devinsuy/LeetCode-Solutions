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
from queue import Queue

class Solution:
    # Given an account, return the account with distinct emails sorted ascending
    def sortAccount(self, account: List[str]) -> List[str]:
        sortedAcc = [account[0]]
        emails = list(set(account[1:]))
        emails.sort()
        sortedAcc.extend(emails)
        return sortedAcc

    
    # Given two account, return the account with their emails merged or None if no overlap
    def merge(self, accL: List[str], accR: List[str]) -> List[str]:
        emailsL = set(accL[1:])
        emailsR = set(accR[1:])
        canMerge = len(emailsL.intersection(emailsR)) > 0

        # If there is overlap in the emails, return the distinct emails of both
        if canMerge:
            acc = [accL[0]]
            acc.extend(emailsL.union(emailsR))
            return acc
        else:
            return None
        
        
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Edge case
        if(len(accounts) == 1):
            return [self.sortAccount(accounts[0])]
        
        # Map name -> to a list of accounts with that name
        nameAccs = defaultdict(list)
        for acc in accounts:
            nameAccs[acc[0]].append(acc) 
            
        # Begin merging accounts one name at a time, sorting and building output
        output = []
        for name, accList in nameAccs.items():
            currQ = Queue()
            nextQ = Queue()
            for acc in accList:
                currQ.put(acc)
            
            # Attempt to merge accounts with the same name
            currAccs = accList
            while(True):
                mergeDone = False
                mergedIndices = set([])
                nextAccs = []
                
                # Check each account against every other account, stop if two 
                # accounts can be merged, record their indices and copy to next list 
                for i in range(len(currAccs)):
                    for j in range(i+1, len(currAccs)):
                        
                        # Do not reprocess accounts that have merged this iteration
                        if(i in mergedIndices or j in mergedIndices):
                            continue
                        mergedAcc = self.merge(currAccs[i], currAccs[j])
                        
                        # Accounts were able to merge, log indices and copy the merged account for next pass
                        if(mergedAcc):
                            mergedIndices.add(i)
                            mergedIndices.add(j)
                            nextAccs.append(mergedAcc)
                            mergeDone = True
                            break
                            
                # No accounts were able to merge, exit search
                if not mergeDone: 
                    break
                    
                # Copy remaining accounts that were unable to merge this pass
                for i in range(len(currAccs)):
                    if i not in mergedIndices:
                        nextAccs.append(currAccs[i])
                currAccs = nextAccs
                
            # Sort the merged accounts and append to output
            for acc in currAccs:
                output.append(self.sortAccount(acc))
        
        return output
        
        
        
        
        
