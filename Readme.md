
# Simple social app 




Now that we’ve learned about the anatomy of our endpoints and the different request methods that we should use, it’s time for some examples:

| Method | URL                                      | Description                     |
| ------ | ---------------------------------------- |---------------------------------|
|`POST`  | `/sign_up`                                 | creates new user (signup)       | 







### Errors

When errors occur the consumer will get a JSON payload verifying that an error occurred together with a reason for why the error occurred. 


| Key       | Description                               |
|-----------|-------------------------------------------|
| `status`  | The HTTP code.                            |
| `data`    | Return request's data                     |
| `message` | A description of the error that occurred. |
| `success` | Request's success status                  |

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
