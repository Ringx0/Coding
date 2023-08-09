n = int(input())  # Read the number of participants from the user input
arr = list(map(int, input().split()))  # Read the scores and store them in a list

# Convert the list of scores to a set to remove duplicates and then convert back to a list
unique_score = list(set(arr))

# Sort the list of unique scores in descending order
unique_score.sort(reverse=True)

# The runner-up score will be the second element in the sorted list
runner_up_score = unique_score[1]

# Print the runner-up score
print(runner_up_score)
