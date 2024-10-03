from lib2to3.fixes.fix_input import context

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

# app.mount("/static", StaticFiles(directory="templates"), name="static")


templates = Jinja2Templates(directory="templates")

users = [
    {
        "full_name": "Mahmud",
        "is_member": "Admin",
        "created_at": "2003/23/12",
        "status": "active",
        "email": "nmadur@gmail.com"
    },
    {
        "full_name": "Azizxoja Nabiyev",
        "is_member": "Member",
        "created_at": "2024/12/12",
        "status": "active",
        "email": "azik7777@gmail.com"
    },
    {
        "full_name": "Sharofiddin",
        "is_member": "BOSS",
        "created_at": "1973/12/08",
        "status": "active",
        "email": "boss@gmail.com"
    }, {
        "full_name": "Malika",
        "is_member": "Manager",
        "created_at": "2001/07/12",
        "status": "active",
        "email": "Menejer@gmail.com"
    }, {
        "full_name": "Muhammadqodir bobo",
        "is_member": "BOBO",
        "created_at": "2025/07/12",
        "status": "active",
        "email": "BOBO@gmail.com"
    }, {
        "full_name": "MuhammadDiyor ROziqov de",
        "is_member": "Odam nomli inson",
        "created_at": "2025/07/12",
        "status": "active",
        "email": "Diyor@gmail.com"
    }, {
        "full_name": "Xadichka ",
        "is_member": "Admin",
        "created_at": "2008/07/12",
        "status": "active",
        "email": "Xadicha@gmail.com"
    }
]


@app.get('/', response_class=HTMLResponse)
async def read_item(request: Request):
    context = {
        "request": request,
        'users': users
    }
    return templates.TemplateResponse('user-list.html', context=context)

# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


# # @app.get('/user/id', response_class=HTMLResponse)
# # async def read_item(request: Request, id:int):
# #     _user=None
# #     for user in users:
# #         if user['id'] == id:
# #             _user=user
#
#     context= {
#         'user':_user
#     }
#     return templates.TemplateResponse('user-detail.html',context=context)
