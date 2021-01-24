from datetime import datetime, time, timedelta
from typing import Optional, List, Dict, Union
from uuid import UUID

from fastapi import FastAPI, Body, Query, Path, Cookie, Header, HTTPException
from starlette import status
# from starlette.exceptions import HTTPException

from firstapp_data import ModelName, fake_items_db, NeedyName, Item, User, Offer, Image, \
    NewItem, other_items, UserOut, UserIn, UserInDB, PlaneItem, CarItem, drive_items

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/", tags=["items"],
         summary="get an item",
         description="get an item with all the information, name",
         response_description="The created item"
)
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}", tags=["items"])
async def read_item(
    item_id: str,
    needy: NeedyName,
    q: Optional[str] = None,
    short: bool = False
):
    item = {"item_id": item_id, "needy": needy}
    if q:
        item.update({"q": q})
    item.update({"short": short})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/me", tags=["users"])
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}", tags=["users"])
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/{user_id}/items/{item_id}", tags=["users"])
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/files/{file_path:path}", tags=["files"])
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/models/{model_name}", tags=["models"])
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        resp = {"model_name": model_name, "message": "Deep Learning FTW!"}

    elif model_name.value == "lenet":
        resp = {"model_name": model_name, "message": "LeCNN all the images"}

    else:
        resp = {"model_name": model_name, "message": "Have some residuals"}
    return resp


@app.get("/newitems/", tags=["newitems"])
async def read_items(
    q: str = Query(
        None,
        min_length=3,
        max_length=50,
        # regex="^fixed.*"
        title="Query",
        description="Query string for the items to search in the database that have a good match",
        alias="item-query"
        )):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/newitems/{item_id}", tags=["newitems"])
async def read_items(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, lt=1000),
    q: Optional[str] = Query(None, alias="item-query"),
    size: float = Query(..., gt=1000, lt=100000)
):
    results = {"item_id": item_id}
    if q or size:
        results.update({"q": q, "size": size})
    return results


@app.get("/items_list/", tags=["items"])
async def read_items(q: Optional[List[str]] = Query(None, title="Query string items",)):
    query_items = {"q": q}
    return query_items


@app.post("/items/", tags=["items"])
async def create_item(item: Item):
    """
        Create an item with all the information:

        - **name**: each item must have a name
        - **description**: a long description
        - **price**: required
        - **tax**: if the item doesn't have tax, you can omit this
        - **tags**: a set of unique tag strings for this item
        """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}", tags=["items"])
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.put("/items/update1/{item_id}", tags=["items"])
async def update_item1(
    item_id: int,
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
    q: Optional[str] = None
):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# Multiple body parameters
# Singular values in body
@app.put("/items/update2/{item_id}", tags=["items"])
async def update_item2(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(..., gt=0),  # singular value
    q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


# Embed a single body parameter
@app.put("/items/update3/{item_id}", tags=["items"])
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/images/multiple/", tags=["items"])
async def create_multiple_images(images: List[Image]):
    return images


@app.post("/offers/", tags=["items"])
async def create_offer(offer: Offer):
    return offer


@app.put("/newitems/update4/{item_id}", tags=["newitems"])
async def update_item(item_id: int, item: NewItem = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/index-weights/", tags=["weights"])
async def create_index_weights(weights: Dict[int, float]):
    return weights


@app.get("/keyword-weights/", response_model=Dict[str, float], tags=["weights"])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


@app.put("/items_time/{item_id}", tags=["items"])
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/cookies/", tags=["extra"])
async def read_cookies(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


@app.get("/headers/", tags=["extra"])
async def read_headers(
    strange_header: Optional[str] = Header(None, convert_underscores=False),
    x_token: Optional[List[str]] = Header(None)
):
    return {"strange_header": strange_header, "X-Token values": x_token}


@app.get("/items-header/{item_id}", tags=["extra"])
async def read_item_header(item_id: str):
    if item_id not in other_items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": other_items[item_id]}


@app.get("/items_resp/{item_id}",
         response_model=Item,
         response_model_exclude_unset=True,
         response_model_include={"name", "description"},
         tags=["items"]
)
async def read_item(item_id: str):
    if item_id not in other_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return other_items[item_id]


@app.get("/items_resp/{item_id}/public", response_model=Item,
         response_model_exclude={"tax"}, tags=["items"])
async def read_item_public_data(item_id: str):
    return other_items[item_id]


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut, tags=["users"])
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


@app.get("/drive_items/{item_id}", response_model=Union[PlaneItem, CarItem], tags=["items"])
async def read_item(item_id: str):
    return drive_items[item_id]


@app.get("/items_resp_list/", response_model=List[Item], tags=["items"])
async def read_items():
    return list(other_items.values())


@app.post("/item_name/", status_code=status.HTTP_201_CREATED, tags=["items"])
async def create_item(name: str):
    return {"name": name}


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
