from app_logic import set_add_values, get_add_result
from utils import parse_post, render_template



def add_values():
    """足し算のフォーム表示と結果処理"""

    # POSTされた場合は値を保存
    form = parse_post()
    if form:    
        try:
            value1 = int(form.get("value1", "0"))
            value2 = int(form.get("value2", "0"))
            set_add_values(value1, value2)
        except ValueError:
            pass  # 無効な入力は無視
    result = get_add_result()

    # HTMLのテンプレートを使って表示用のHTMLを生成して返す
    return render_template("boundaries/greeting.html", result=result, add_result_display=result or "未設定")