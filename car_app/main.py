from pydantic import BaseModel
from typing import List,Dict, Optional

class Comment(BaseModel):
    author: str
    comment: str
    likes: int
    
class Post(BaseModel):
    author: str
    co_author: Optional[str] = None
    date: str
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[Comment]

comment = [
Comment(author= "Jiant_Joe", comment ="Nice post!",likes= 8),
Comment(author= "Harold_Hues", comment ="Nice post!",likes= 8),
Comment(author= "Fernando", comment ="Nice post!",likes= 8)
]


post = Post(
    author = "John Doe",
    co_author = "Fernando Cabrera",
    date = "1/12/1978",
    title = "Hello World",
    content = "lorem Ipsum",
    id = 21,
    likes = ["john doe", 'harlem shake', 'cool bryan'],
    comments= comment

)
print(post)