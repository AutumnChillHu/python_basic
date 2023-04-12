# -*- coding: utf-8 -*-
from flask import redirect, url_for, request

from . import task
from ...utils.request import get_request_params


@task.route("/info", methods=["GET"])
@task.route("/info/<int:task_id>", methods=["GET"])
def task_info(task_id=-1):
    return "here is info of task{}".format(task_id)


@task.route("/count", methods=["GET"])
def task_count():
    print(type(request))
    request_data = get_request_params()
    print(request_data)
    if "redirect" in request_data.keys() and request_data["redirect"] == "1":
        # flask.redirect：重定向
        # flask.url_for：获取blueprinName.task_info视图函数的url。动态获取，即使url规则改变了，这里也无需改动。
        return redirect(url_for(".task_info", task_id=9999999999))
    return "100"

# @task.route('/csc/assign/agentId', methods=['POST'])
# def csc_assign_agentId():
#     params = get_request_params()
#     data, msg = CscToolBoxs.csc_assign_agentId(params=params)
#     return api_response(data=data, msg=msg)
