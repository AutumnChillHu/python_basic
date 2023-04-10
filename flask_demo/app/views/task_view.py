# -*- coding: utf-8 -*-
from . import task


@task.route("/info/<task_id>", methods=["GET"])
def get_task_info(task_id):
    return "here is info of task{}".format(task_id)


@task.route("/count", methods=["GET"])
def get_task_count():
    return "100"


# @task.route('/csc/assign/agentId', methods=['POST'])
# def csc_assign_agentId():
#     params = get_request_params()
#     data, msg = CscToolBoxs.csc_assign_agentId(params=params)
#     return api_response(data=data, msg=msg)
