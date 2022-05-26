import os
from flask import Blueprint, jsonify

from UseSqlite import RiskQuery

api_bp = Blueprint("api_bp", __name__)


@api_bp.route('/api/json', methods=['GET'])
def get_phothos_info():
    rq = RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    # 初始化返回数据record和当前路径root_path
    record, root_path = {}, os.path.dirname(__file__)
    for r in rq.format_results().split('\n\n'):
        # 分割数据并去掉前后空格
        item = list(map(lambda x: x.strip(' '), r.split(',')))
        # 去除路径前缀
        if item[2].startswith('./') or item[2].startswith('.\\'):
            item[2] = item[2][2:]
        record[item[3]] = {
            "dateOfUpload":  item[0],
            "photoSize": os.stat(os.path.join(
                root_path,  item[2])).st_size,
            "phtoDescription": item[1],
        }
    if len(record) == 0:
        return {
            "photo": None
        }
    return record
