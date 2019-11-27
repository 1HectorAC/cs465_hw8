from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

#Data to serve with API
POSTS = {
    "0": {
        "id" : 1,
        "title" : "Cats",
        "body" : "About cats.",
        "link" : False,
        "url" : "",
        "timestamp" : get_timestamp(),
        "user_id" : 1,
        "category_id" : 3,
        "vote_count" : 3,          

    },
    "1": {
        "id" : 2,
        "title" : "Cool Stuff",
        "body" : "This is about cool stuff.",
        "link" : True,
        "url" : "www.stuff.com",
        "timestamp" : get_timestamp(),
        "user_id" : 1,
        "category_id" : 3,
        "vote_count" : 0, 
    },
    "2": {
        "id" : 3,
        "title" : "Tech Stuff",
        "body" : "About tech stuff.",
        "link" : False,
        "url" : "",
        "timestamp" : get_timestamp(),
        "user_id" : 2,
        "category_id" : 1,
        "vote_count" : 1, 
    }
}

def read():
    return [POSTS[key] for key in sorted(POSTS.keys())]
