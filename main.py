import json  

# Load liked_posts.json
with open ('liked_posts.json') as file: 
  likedposts = json.load(file)

# Load following.json
with open('following.json') as file:
  following_json = json.load(file)

# Create an empty list for liked posts and following users
liked_post_and_followingusers = []

# Add all following users to the list
for following in following_json["relationships_following"]: 
  liked_post_and_followingusers.append(following["string_list_data"][0]["value"])

# Add all image users to the list
for image in likedposts["likes_media_likes"]:
  liked_post_and_followingusers.append(image["string_list_data"][0]["value"])

# Remove duplicates from the list
liked_post_and_followingusers = list(set(liked_post_and_followingusers))

# Print out the unique list of users
for user in liked_post_and_followingusers:
  print(user)
