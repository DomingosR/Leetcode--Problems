# Notes on Suffix Automaton
#
# (This is a summary of the article from CP Algorithms, 
# search for "Suffix Automaton".)
#
# ----------------- Description -----------------------
#
# A suffix automaton for a string s is an acyclic directed
# graph structure with the following characteristics:
#
# > A single root, from which every node can be reached;
#
# > Labelled transitions, each label a character in s;
#
# > A node may be the source of multiple transitions, but
#   any two transitions from the same node must have different
#   labels;
#
# > Some vertices marked as terminal (which may or may not
#   be terminal in the usual graph sense), which correspond to
#   every suffix of s;
#
# > Satisfying P1 - P3, where:
#   - P1: Every substring of s corresponds to a path from the
#         root to some vertex of the graph
#   - P2: Every suffix of s is obtained by a path from the
#         root to a terminal vertex
#   - P3: if two substrings s1 and s2 are end-position equivalent
#         (meaning the end of every occurrence of either is the end
#         of every occurrence of the other), their paths end in the
#         same node of the graph.
#
# The concept of suffix links is important.  A suffix link runs from
# a state v (corresponding to s1) to the state that corresponds to
# the longest suffix of s1 not in the same equivalence class with
# respect to end-position.
#
# Example: for s = "abcdbcdecd", the strings "abcd" and "bcd" are
# end-position equivalent, since all occurrences of either end in
# positions 3 and 6 of s.  Thus, they are represented by the same
# node in the automaton.  The string "cd" is not end-position
# equivalent to either, since the set of its end-positions is {3, 6, 9}.
# Since this is the longest suffix of either "abcd" and "bcd" not in
# the same equivalence class, the suffix link from (the node corresponding
# to) "abcd" and "bcd" points to (the node corresponding to) "cd".
#
# It follows that the graph constructed using suffix links is a tree
# tree rooted in the root of the automaton.
#
# ----------------- Construction -----------------------
#
# In each node, we will keep the following values:
#
# > len: the length of the longest substring that corresponds to that node;
# > link: the suffix link corresponding to that node;
# > a list of transitions from this node.
#
# The construction starts with the creation of the root node, and we
# process the addition of each character in the string iteratively.
# The process for doing so is as follows:
#
# > Let "last" be the state corresponding to the whole string so far.
#   Suppose that the new character to be added is "c".
# > Create a new state (called "curr"), and set len(curr) = len(last) + 1.
#   At this stage, we don't know what link(curr) is.
# > Starting at "last", follow the suffix links backwards for as long as
#   we have only nodes which don't already have a transition labelled "c".
#   For each such state, add a transition to the node "curr".
# > If we reach the root node, we can assign the suffix link of curr to the
#   root node, and go to the last step.
# > If we reach a node with a transition labelled "c", denote the node reached
#   by "p" and the node the transition leads to by "q".  Then:
#   (a) If len(q) = len(p) + 1, set link(curr) to "q", and go to the last step.
#   (b) Otherwise, clone state "q" (create "clone" with the same suffix link and
#       transitions as "q", and with len(clone) = len(p) + 1); direct suffix links
#       from "q" and "curr" to "clone"; and traverse the path from "p" to 
#       root altering the transitions that lead to "q" to transitions leading
#       to "clone", until we reach a state from which there is no transition
#       to "q".
# > As a final step, set "last" to "curr".
#
# ----------------- Implementation -----------------------
#
# Note that in the below we add some properties and variables designed to 
# answer the question of Leetcode problem 1923 - Longest Common Subpath.
#

from functools import reduce

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:

        class State:
            def __init__(self, len, link, transitions = []):
                self.len = len
                self.link = link
                self.next = {} if not transitions else dict(transitions)
                self.answer = len    # Additional property for purposes of LC 1923
                                     # Will keep track of the maximum length of string
                                     # common to all strings with suffix equal to the
                                     # one corresponding to this node

                self.maxLen = 0      # Additional property for purposes of LC 1923
                                     # As a new path is considered, will store the maximum
                                     # length of a substring between new path and initial
                                     # path corresponding to this suffix

        class SuffixAutomaton:
            # Adds a state to the automaton
            def newState(self, len, link, transitions = None):
                addedState = State(len, link, transitions)
                self.container.append(addedState)
                return addedState

            # Processes a new character in the input string, adding one or
            # more states corresponding to it.  The CP Algorithms site has
            # a detailed explanation of the logic of this method.            
            def addNode(self, newChar):
                p = self.lastNode
                currentNode = self.newState(p.len + 1, self.root)
                while p:
                    if newChar in p.next:
                        q = p.next[newChar]
                        if q.len == p.len + 1:
                            currentNode.link = q
                        else:
                            cloneNode = self.newState(p.len + 1, q.link, q.next)
                            while p and p.next[newChar] == q:
                                p.next[newChar] = cloneNode
                                p = p.link
                            currentNode.link = q.link = cloneNode
                        break

                    p.next[newChar] = currentNode
                    p = p.link

                self.lastNode = currentNode

            # Checks length of common substrings between newPath and initial string
            # corresponding to each possible last character of prefix of newPath
            # The CP Algorithms site has a detailed explanation of the logic of this
            # method.
            def explore(self, newPath):
                for indState in self.container:
                    indState.maxLen = 0
                p, length = self.root, 0
                for indChar in newPath:
                    while True:
                        if indChar in p.next:
                            p = p.next[indChar]
                            length += 1
                            p.maxLen = max(p.maxLen, length)
                            t = p.link
                            while t.maxLen < t.len:
                                t.maxLen = t.len
                                t = t.link
                            break
                        if not p.link:
                            break
                        p = p.link
                        length = p.len
                        
                for indState in self.container:
                    indState.answer = min(indState.answer, indState.maxLen)

            # Computes longest common subpath
            def longestCommonSubpath(self):
                return max(map(lambda indState: indState.answer, self.container))

            # Initializes the automaton
            def __init__(self, inputStr):
                self.container = []
                self.root = self.newState(0, None)
                self.lastNode = self.root

                last = root = self.newState(0, None)
                for newChar in inputStr:
                    self.addNode(newChar)  
        
        # Compute solution
        shortestPath = reduce(lambda a, b: a if len(a) < len(b) else b, paths)
        suffixAutomaton = SuffixAutomaton(shortestPath)
        [suffixAutomaton.explore(path) for path in paths if path != shortestPath]
        return suffixAutomaton.longestCommonSubpath()