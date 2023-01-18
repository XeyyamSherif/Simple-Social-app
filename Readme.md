
# Simple social app 



### How to run this app (Ubuntu)
```
clone app to ypur machine
Run below commands on file directory
- "python3 -m venv venv"
- pip3 install requirements.txt
- sh starts.sh 

(I will create docker configs to run this app at future)
```

### Collections of apis at Postman
 - https://www.postman.com/mogols/workspace/my-public/collection/13456460-3f846c6f-22f0-4aa3-86d4-3427ca39fffb?action=share&creator=13456460



Now that we’ve learned about the anatomy of our endpoints and the different request methods that we should use, it’s time for some examples:

| Method   | URL                                     | Description                                        |
|----------|-----------------------------------------|----------------------------------------------------|
| `POST`   | `/sign_up`                              | creates new user (signup)                          |
| `POST`   | `/log_in`                               | logging in user, returns  access and refresh token |
| `POST`   | `/create_post`                          | creates post for user, Requires a valid JWT        |
| `DELETE` | `/delete_post`                          | deletes post, Requires a valid JWT                 |
| `GET`    | `/read_posts`                           | fetches all posts, Requires a valid JWT            |
| `PATCH`  | `/update_post`                          | update post, Requires a valid JWT                  |
| `PATCH`  | `/like_post`                            | likes post, Requires a valid JWT                   |
| `PATCH`  | `/dislike_post`                         | dislikes post, Requires a valid JWT                |





#### **POST** `/sign_up`
* Used for signing up a user. Accepts `first_name`, `mail`, and `password` as payload to create a driver . Returns driver's data.

#### **POST** `/log_in`
* Used for signing in a user. Accepts `mail` and `password` as payload. Returns tokens data.

#### **POST** `/create_post`
* Used for create post. Accepts `content` and `title` as payload.  

#### **DELETE** `/delete_post`
* Deletes post. Accepts post `_id` as paramater on url

#### **GET** `/read_posts`
* Reads all posts from db


#### **PATCH** `/read_posts`
* updates post fields, accepts post id at parameter and updated fileds as payload

#### **PATCH** `/like_post`
* Used for like post, accepts post id on url parameter

#### **PATCH** `/dislike_post`
* Used for dislike post, accepts post id on url parameter

### Note
* User can like and dislike posts many times (at least for now, will be fixed with many to many relation )


### Errors

When errors occur the consumer will get a JSON payload verifying that an error occurred together with a reason for why the error occurred. 

## Base response schema

| Key          | Description                               |
|--------------|-------------------------------------------|
| `status`     | The HTTP code.                            |
| `data`       | Return request's data                     |
| `message`    | A description of the error that occurred. |
| `success`    | Request's success status                  |
| `error_code` | if there is error, shows error code       |



## HTTP Response Status Codes

One of the most important things in an API is how it returns response codes. Each response code means a different thing and consumers of your API rely heavily on these codes.

| Code  | Title                     | Description                              |
| ----- | ------------------------- | ---------------------------------------- |
| `200` | `OK`                      | When a request was successfully processed (e.g. when using `GET`, `PATCH`, `PUT` or `DELETE`). |
| `201` | `Created`                 | Every time a record has been added to the database (e.g. when creating a new user or post). |
| `400` | `Bad request`             | When the request could not be understood (e.g. invalid syntax). |
| `401` | `Unauthorized`            | When authentication failed. |
| `403` | `Forbidden`               | When an authenticated user is trying to perform an action, which he/she does not have permission to. |
| `404` | `Not found`               | When URL or entity is not found. |
| `422` | `Unprocessable entity`    | Whenever there is something wrong with the request (e.g. missing parameters, validation errors) even though the syntax is correct (ie. `400` is not warranted). |
| `500` | `Internal server error`   | When an internal error has happened (e.g. when trying to add/update records in the database fails). |

The response codes often have very precise definition and are easily misunderstood when just looking at their names. For example, `Bad Request` refers to malformed requests and not, as often interpreted, when there is something semantically wrong with the reuquest. Often `Unprocessable entity` is a better choice in those cases.
Another one that is often used incorrectly is `Precondition Failed`. The precondition this status code refers to are those defined in headers like `If-Match` and `If-Modified-Since`. Again, `Unprocessable entity` is usually the more appropriate choice if the request somehow isn't valid in the current state of the server.
When in doubt, refer to [this overview](https://httpstatuses.com) and see if the description of an status code matches your situation.
