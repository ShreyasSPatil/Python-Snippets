"""
Let's consider that you have a online platform offering various services.
And you have calculated a count of services being used by each user and stored it in a dictionary format.
{'usr1': 1, 'usr2': 6, 'usr3': 5, 'usr4': 5, 'usr5': 4, 'usr6': 6, 'usr7': 0}

Now you want to know the users according to the counts so as to get the clear idea of the usage of the services.
{0: [1, 'usr7'], 1: [1, 'usr1'], 4: [1, 'usr5'], 5: [2, 'usr3', 'usr4'], 6: [2, 'usr2', 'usr6']}
Where key '0' consists of the users with no active services and the first value of the list of values is the count of
total number of users in the list.

To achieve that, we will first use the count values in the original dictionary as the keys in the output where if a
count value is observed again the related user will be put in the list associated with the count key and the number of
users (first item of the list) will be updated.
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
