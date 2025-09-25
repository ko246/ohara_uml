from app_logic import set_add_values, get_add_result
from utils import parse_post, render_template

def add_values(environ) -> str:
    """足し算のフォーム表示と結果処理"""
    
    # # 既存の計算結果を取得
    # value1, value2 = "", ""
    # result = get_add_result()
    
    # # POSTリクエストの場合のみデータを処理
    # if environ["REQUEST_METHOD"] == "POST":
    #     try:
    #         # environを引数として渡し、TypeErrorを回避
    #         form = parse_post(environ)
    #         value1 = int(form.get("value1", "0"))
    #         value2 = int(form.get("value2", "0"))
    #         set_add_values(value1, value2)
    #         # 新しい計算結果を再取得
    #         result = get_add_result()
    #     except ValueError:
    #         # 無効な入力（数値以外）は無視する
    #         pass

    # # HTMLのテンプレートを生成して返す
    # # resultがNoneの場合は「未設定」と表示
    return render_template("boundaries/add.html", add_result_display="未設定")