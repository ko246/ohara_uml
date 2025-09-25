from app_logic import get_add_result, set_value1, set_value2
from utils import parse_post, render_template

def add_values(environ) -> str:
    """足し算のフォーム表示と結果処理"""
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        value1 = data.get("first_value", [0])[0]
        value2 = data.get("second_value", [0])[0]

        # ここに処理を書く
        set_value1(value1)
        set_value2(value2)
        addition = get_add_result()

    # # HTMLのテンプレートを生成して返す
    return render_template("boundaries/add.html")