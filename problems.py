def twice(s):
    if len(s) == 0:
        return False
    look_up = set()
    for char in s:
        if char not in look_up:
            look_up.add(char)
        else:
            return char


# print(twice("letter"))

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    count_s1 = {}
    count_s2 = {}
    for char in s1:
        if char not in count_s1:
            count_s1[char] = 1
        else:
            count_s1[char] += 1
    for char in s2:
        if char not in count_s2:
            count_s2[char] = 1
        else:
            count_s2[char] += 1
    if count_s1 == count_s2:
        return True
    return False


# print(anagram('dog','gode'))

def pair_sum(nums, k):
    seen = {}
    result = set()
    for num in nums:
        compliment = k - num
        if compliment in seen:
            result.add((compliment, num))
        else:
            seen[num] = True
    return result


# print(pair_sum([1], 5))
from collections import Counter


def missing_element(l1, l2):
    c1 = Counter(l1)
    c2 = Counter(l2)
    for value in c1:
        if value not in c2:
            return value


def missing_element(l1, l2):
    c1 = {}
    c2 = {}
    for value in l1:
        if value not in c1:
            c1[value] = 1
        else:
            c1[value] += 1
    for value in l2:
        if value not in c2:
            c2[value] = 1
        else:
            c2[value] += 1
    for value in c1:
        if value not in c2:
            print(value)
            return value


# print(missing_element([1, 2, 3, 4, 5], [4, 3, 1, 2]))
def large_cont_sum(arr):
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(curr_sum, max_sum)

    return max_sum


print(large_cont_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def max_subarray_sum(arr):
    if not arr:
        return 0, None, None

    max_sum = current_sum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
            s = i

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i

    return max_sum, start, end


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start_index, end_index = max_subarray_sum(arr)
print(f"Largest continuous sum is {max_sum} from index {start_index} to {end_index}")

# s1, s2 = 'clint eastwood', 'old west action'
# print(sorted(s1))
# print([a for a in zip([1, 2, 3, 8, 9], [1, 2, 3, 4])])
import collections
d = collections.defaultdict(int)
d[5] += 1
# print(d)
# e = {}
# e[5] += 1
# print(e)

import collections


def finder2(arr1, arr2):
    # Using default dict to avoid key errors
    d = collections.defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        d[num] += 1

        # Check if num not in dictionary
    for num in arr1:
        if d[num] == 0:
            return num

            # Otherwise, subtract a count
        else:
            d[num] -= 1


def finder3(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num
        # print(result)

    return result

arr1 = [5,8,7,7]
arr2 = [5,7,7]

finder2(arr1,arr2)
finder3(arr1,arr2)

def large_sum(arr):
    if len(arr) == 0:
        return 0
    max_sum = current_sum = arr[0]
    start = end = 0

    for i in range(1, len(arr)):
        if current_sum+arr[i]>arr[i]:
            current_sum = current_sum+arr[i]
        else:
            current_sum = arr[i]
            start = i
        if current_sum>max_sum:
            max_sum = current_sum
            end = i
    return max_sum, start,end

print("large sum: ",large_sum([1,2,-10,3,4,10,10,-10,-1]))


def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))

print(rev_word3('   Hello John    how are you   '))

def parenthesis_check(s):
    if not s or len(s)%2 != 0:
        return False
    stack = []
    match = {")":"(","}":"{","]":"["}
    for value in s:
        if value in match.values():
            stack.append(value)
        elif value in match.keys():
            if stack == [] or match[value] != stack.pop():
                return False
        else:
            continue
    return stack==[]

print(parenthesis_check('[[((1234))]]'))


