from fastapi import FastAPI, Path, Query, Request

app = FastAPI()

# Create a Jinja2 environment


@app.get("/idiot")
def read_root():
    return {"Hello": "Idiot"}


@app.get("/posts/{post_id}")
def read_posts(post_id: int):
    return {"post": post_id}

# The 3 dots mean None. item_id is optional.
# def read_item(item_id: int = ...):
#     return {"item_id": item_id}
# The Path object is used to specify parameters that are part of the URL path
# Also for metadata and API documentation


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="Item ID", ge=0, le=1000)):
    return {"item_id": item_id}


@app.get("/users")
def read_users(page: int = Query(..., gt=0)):
    return {"page": page}

