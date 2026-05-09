from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/",response_class=HTMLResponse,include_in_schema=False)
def home():
    return f"<h1>Welcome to the FastAPI Blog!</h1><p>Use the /api/posts endpoint to see all posts.</p>"

@app.get("/api/posts",response_class=HTMLResponse,include_in_schema=False)
def get_posts():
    return f"<h1>Blog Posts</h1>" + "".join(f"<h2>{post['title']}</h2><p>By {post['author']} on {post['date_posted']}</p><p>{post['content']}</p>" for post in posts)
