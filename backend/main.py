"""
基于fastapi实现后端简易服务
运行：
> uvicorn main:app --reload
"""
import time
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


def response(success: bool = True, error={}, data: any = []) -> dict:
    """
    自定义接口返回格式
    """
    if error == {}:
        error_code = ""
        error_msg = ""
    else:
        success = False
        error_code = list(error.keys())[0]
        error_msg = list(error.values())[0]

    resp = {
        "success": success,
        "error": {
            "code": error_code,
            "message": error_msg
        },
        "result": data
    }
    return resp


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/projects/list")
def project_list():
    """
    项目列表
    """
    projects = []
    for i in range(10):
        projects.append({
            "id": i,
            "name": "项目1"+str(i),
            "describe": "describe",
            "user_name": "admin",
            "create_time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": time.strftime("%Y-%m-%d %H:%M:%S")
        })
    data = {
        "page": 1,
        "size": 10,
        "total": 20,
        "projectList": projects
    }
    return response(data=data)


@app.get("/api/v1/project/detail")
def project_detail():
    """
    项目详情
    """
    data = {
        "id": 1,
        "name": "项目1",
        "describe": "describe",
        "user_name": "admin",
        "create_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "update_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return response(data=data)


@app.post("/api/v1/project/delete")
def project_delete():
    """
    删除项目
    :return:
    """
    data = {
        "id": 1,
        "name": "项目1",
        "describe": "describe",
        "user_name": "admin",
        "create_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "update_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return response(data=data)


@app.put("/api/v1/project/update")
def project_update():
    """
    更新项目
    """
    data = {
        "id": 1,
        "name": "项目1",
        "describe": "describe",
        "user_name": "admin",
        "create_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "update_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return response(data=data)


@app.post("/api/v1/project/create")
def project_create():
    """
    创建项目
    """
    data = {
        "id": 1,
        "name": "项目1",
        "describe": "describe",
        "user_name": "admin",
        "create_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "update_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return response(data=data)

