from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/k2/api/test-fe.html')
def hello_world() -> 'html':
    return render_template('base.html'
                            )

@app.route('/k2/recommend')
def get_name() -> str:
    return 'gwesley' + random.choice('abcdefg&#%^*f')


@app.route('/redpack2018/loginrp/info')
def login_redpack() :

    # t = {
    #     "errno": 0,
    #     "errmsg": "success",
    #     "data": {
    #         "isSend": False, # 是否发登录红包
    #         "reason": "7天内2次或多余7天共4次，不发" # 不发红包理由（不用展示，调试用）
    #     }
    # }

    t = {
        "errno": 0,
        "errmsg": "success",
        "data": {
            "isSend": True,
            "reason": "首次发红包",
            "info": {
                "maxAmount": 99,
                "t1":"<font color=\"999999\">每日签到，领取最高<font color=\"FB3B3B\">300金币</font></font>",
                "t2":"<font color=\"999999\">每日宝箱，每天最多可拆18个宝箱，每日最高可领取<font color=\"FB3B3B\">10000金币</font></font>",
                "t3":"<font color=\"999999\">每日任务，观看视频、发表评论、关注作者、分享视频等均可获得不同数量的金币奖励</font>"
            }
        }
    }

    return jsonify(t)


@app.route('/redpack2018/loginrp/takeAwards')
def bind_redpack() :
    # print(request.cookies.__str__())

    t = {
        "errno": 0,
        "errmsg": "success",
        "data": {
            "result": 1,
            "amount": 3
        }
    }

    return jsonify(t)

@app.route('/k2/redpack2018/task/videoevent/done')
def video_task() :
    t = {
        "errno": 0,
        "errmsg": "success",
        "data": {
            "rewards": [
                {
                    "term": 17609,
                    "reward_ts": 0,
                    "dispatch_ts": 1521444232,
                    "amount": 300,
                    "award_type": 1,
                    "id": "5aaf6588966ea1486e00c284",
                    "taskId": 5,
                    "qid": 11223,
                    "taskName": "成功评论5视频",
                    "task_config_id": 10043
                }
            ]
    }

        # "unlogin_play_info"
        #
        # {
        #     "errno":0,
        #     "data": {
        #         "coin":100,
        #         "duration":1000
        #     }
        # }
}