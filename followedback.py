import json

# get information from followers file
with open('followers.json', 'r') as f:  
    follower = json.load(f) 

# get information from following file
with open('following.json', 'r') as g:  
    following = json.load(g) 

followers_list = []
following_list = []

# adds to followers list
for i in follower:
  followers_list.append(i['string_list_data'][0]['value'])

# adds to following list
for i in following['relationships_following']:
  following_list.append(i['string_list_data'][0]['value'])

# converts lists into sets
followersset = set(followers_list)
followingset = set(following_list)

# who's in following and not followers
NoFollowBack = (followingset.difference(followersset))

# prints number of people who don't follow back
print(len(NoFollowBack))

# make into a sorted list
list1 = list(NoFollowBack)
list1 = sorted(list1)

# prints people who don't follow back
for name in list1:
    print(name)