"""
Let's consider that you have a online platform offering various services.
And you have calculated a count of services being used by each user and stored it in a dictionary format.
"""

# Generating Data for the demonstration
import random

# Let's assume you have 100 users and 10 services
users = 100
services = 10
data_dict = {}  # Original dictionary with users as keys and the number of services they use as the count.
output_dict = {}  # Desired output with counts as keys and a list of users as the values.

for i in range(0, users):
    data_dict["usr" + str(i + 1)] = random.randint(0, services)

# Verify the randomly generated data
print(data_dict)

# Use the counts as keys in our output dictionary
for user in data_dict.keys():
    if data_dict[user] not in output_dict.keys():
        output_dict[data_dict[user]] = list([1, user])  # First item of the list is the count of users in the list.
    else:
        output_dict[data_dict[user]].append(user)
        output_dict[data_dict[user]][0] += 1  # Updates the count of users in the list.

# Verify the output dictionary.
print(output_dict)

# Count if all the users were taken into account.
usr_cnt = 0
for count in output_dict.keys():
    usr_cnt += output_dict[count][0]

# Print the observations. Can be later used for visualization.
print("Users with no active services: " + str(output_dict[0][0]))
print("Total number of users:" + str(usr_cnt))
