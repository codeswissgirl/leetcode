"""
For this problem, we can build a graph that consists of all the letters in the alphabet and draw edges from the letter that comes before to the letter that comes after in the lexicographic order. Then we use Topological Sorting to solve it.
The function alienOrder accepts a list of words and returns a string representing the order of letters in the alien language.

This solution uses the BFS version of topological sort.

The time complexity of this solution is O(C), where C is the total length of all the words combined, because each letter will be processed and compared only once. The space complexity is also O(1) or O(U), where U is the total number of unique letters in the input. This is because in the worst case, this is the space we will need for our in-degree array, the queue for the BFS, and the output list.
"""

from collections import defaultdict, deque, Counter

def alienOrder(words):
    # Step 0: Create data structures and find all unique letters.
    adj_list = defaultdict(set)
    counts = {c : 0 for word in words for c in word}

    # Step 1: Find all edges.
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): 
                return ""

    # Step 2: Breadth-first search.
    output = []
    queue = deque([c for c in counts if counts[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(counts):
        return ""

    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)
