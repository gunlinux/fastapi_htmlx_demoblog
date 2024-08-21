from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Пример постов
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the third post."},
]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "posts": posts}
    )


@app.get("/posts/{post_id}", response_class=HTMLResponse)
async def get_post(request: Request, post_id: int):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return templates.TemplateResponse(
            "post.html", {"request": request, "post": post}
        )
    return HTMLResponse("Post not found", status_code=404)
