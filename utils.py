from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class UserName:
    name: str


@dataclass
class UserPost:
    name: str
    id: int


@dataclass
class Users:
    users: list[UserPost]


@dataclass
class PostDataUser:
    title: str
    user_id: int


@dataclass
class Posts:
    post_id: int
    title: str
    created_at: datetime


@dataclass
class PostData:
    user_id: int
    title: str
    post_id: int


@dataclass
class PostList:
    posts: list[Posts]


@dataclass
class CommentPost:
    post_id: int
    user_id: int
    title: str
    parent_comment_id: Any
    is_parent: bool


@dataclass
class CommentData:
    title: str
    comment_id: str


@dataclass
class FetchComments:
    post_id: int
    parent_comment_id: Any


@dataclass
class Comments:
    title: str
    user_id: int
    created_at: Any


@dataclass
class CommentList:
    comments: list[Comments]


@dataclass
class PostLike:
    user_id: int
    post_id: int


@dataclass
class CommentLike:
    user_id: int
    comment_id: int


@dataclass
class PostID:
    post_id: int


@dataclass
class UserID:
    user_id: int


@dataclass
class CommentID:
    comment_id: int


@dataclass
class Total:
    total_likes: int

