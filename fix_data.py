import json

with open("Data/processed_posts.json", "r") as f:
    data = json.load(f)

for post in data:
    if "tag" not in post:
        post["tag"] = ["General"]

with open("Data/processed_posts.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ tag field added to all posts")