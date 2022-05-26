from flask import Blueprint
from PIL import Image

from UseSqlite import RiskQuery

show_bp = Blueprint("show_bp", __name__)


@show_bp.route("/show", methods=["POST", "GET"])
def album_view():
    rq = RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    record = '<p>My past photo</p>'
    for r in rq.format_results().split('\n\n'):
        record += '%s' % (make_html_paragraph(r))
    return record+'</table>\n'


def make_html_paragraph(s):
    if s.strip() == '':
        return ''
    lst = s.split(',')
    picture_path: str = lst[2].strip()

    picture_name = lst[3].strip()
    im = Image.open(picture_path)
    im.thumbnail((400, 300))
    im.save('./static/figure/'+picture_name, 'jpeg')

    # 绝对url路径
    if picture_path.startswith('./') or picture_path.startswith('.\\'):
        picture_path = picture_path[2:]
    if not(picture_path.startswith('/') and picture_path.startswith('\\')):
        picture_path = '/'+picture_path

    result = '<p>'
    result += '<i>%s</i><br/>' % (lst[0])
    result += '<i>%s</i><br/>' % (lst[1])
    result += '<a href="%s"><img src="/static/figure/%s"alt="风景图"></a>' % (
        picture_path, picture_name)
    return result+'</p>'
