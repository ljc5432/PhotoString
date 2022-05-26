from flask import Blueprint

import show_bp
from UseSqlite import RiskQuery
search_bp = Blueprint("search_bp", __name__)

@search_bp.route("/search/", defaults={'key_word': None})
@search_bp.route("/search/<string:key_word>")
def get_database_photos(key_word: str):
    rq = RiskQuery('./static/RiskDB.db')
    sql: str
    if key_word:
        # 脱敏处理,防止sql注入
        key_word = key_word.strip(' ').replace('%', '%%').replace("'", "''")
        key_word = '%'+key_word+'%'
        sql = "SELECT * FROM photo WHERE description LIKE '%s' ORDER By time desc" % (
            key_word)
    else:
        sql = "SELECT * FROM photo ORDER By time desc"
    rq.instructions(sql)
    rq.do()
    record = '<p>My past photo</p>'
    record += '<input type="text" onkeydown="if(event.keyCode == 13)window.location.href = `/search/${event.target.value}`">'
    for r in rq.format_results().split('\n\n'):
        record += '%s' % (show_bp.make_html_paragraph(r))
    return record+'</table>\n'
