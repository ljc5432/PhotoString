from flask import Blueprint, request
from datetime import datetime

import show_bp
from UseSqlite import InsertQuery

upload_bp = Blueprint("upload_bp", __name__)


@upload_bp.route('/upload/', methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        # 限制文件格式
        if uploaded_file.content_type.find('jpg') == 0:
            return '<p>Please upload JPG format file<br/> <a href="/">Return</a>.'
        time_str = datetime.now().strftime('%Y%m%d%H%M%S')
        new_filename = time_str+'.jpg'
        uploaded_file.save('./static/upload/'+new_filename)
        time_info = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        description = request.form['description']
        # 脱敏处理,防止sql注入
        description = description.strip(' ').replace(
            '%', '%%').replace("'", "''")
        path = './static/upload/'+new_filename
        iq = InsertQuery('./static/RiskDB.db')
        iq.instructions("INSERT INTO photo Values('%s','%s','%s','%s')" % (
            time_info, description, path, new_filename))
        iq.do()
        return '<p>You have uploaded %s.<br/> <a href="/">Return</a>.' % (uploaded_file.filename)
    else:
        page = '''<form action="/upload"method="post"enctype="multipart/form-data">
        <input type="file"name="file"><input name="description"><input type="submit"value="Upload"></form>'''
        page += show_bp.album_view()
        return page
