# -*- coding: utf-8 -*-
from flask import redirect, url_for, request

from . import task_bp
from ..services.task import Task
from ...utils.request import get_request_params
from ...utils.response import response_dict, HttpStatusCode


@task_bp.route("/info", methods=["GET"])
@task_bp.route("/info/<int:task_id>", methods=["GET"])
def task_info(task_id=-1):
    # todo 数据库查询
    return "here is info of task{}".format(task_id)


@task_bp.route("/allcount", methods=["GET"])
def task_allcount():
    print(type(request))
    request_data = get_request_params()
    print(request_data)
    if "redirect" in request_data.keys() and request_data["redirect"] == "1":
        # flask.redirect：重定向
        # flask.url_for：获取blueprinName.task_info视图函数的url。动态获取，即使url规则改变了，这里也无需改动。
        return redirect(url_for(".task_info", task_id=9999999999))
    return "100"


@task_bp.route("/create", methods=["POST"])
def create_task():
    requests_data = get_request_params()
    # 校验参数
    if not requests_data.get("name"):
        return response_dict(status_code=HttpStatusCode.ARGS_ERROR)
    result = Task().create_task(requests_data)
    # todo 处理异常情况dd
    if not isinstance(result, tuple):
        return api_response()
    else:
        return api_response(msg=result[1], code=2001)


@task_bp.route("/update", methods=["POST"])
def update_task():
    pass


@task_bp.route("/delete", methods=["POST"])
def delete_task():
    pass

# @task_bp.route('/csc/assign/agentId', methods=['POST'])
# def csc_assign_agentId():
#     params = get_request_params()
#     data, msg = CscToolBoxs.csc_assign_agentId(params=params)
#     return api_response(data=data, msg=msg)
