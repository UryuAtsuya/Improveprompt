import streamlit as st
from openai import OpenAI
import os

api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Streamlitアプリケーションの設定
st.title("AIツール初心者向けプロンプト生成サイト")

# ユーザー入力を受け取る
user_input = st.text_area("あなたの目的を入力してください:", height=100)

# OpenAI APIを使用してプロンプトを改善する関数
def improve_prompt(input_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたはAIツールの使用に関する専門家です。ユーザーの入力を元に、より効果的で具体的なプロンプトを生成してください。"},
                {"role": "user", "content": f"次の目的のためのより良いプロンプトを作成してください: {input_text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"OpenAI APIエラー: {str(e)}")
        return None

# プロンプトを生成
if user_input:
    with st.spinner('プロンプトを改善中...'):
        improved_prompt = improve_prompt(user_input)
    if improved_prompt:
        st.write("改善されたプロンプト:")
        st.write(improved_prompt)

# フィードバック機能
# feedback = st.radio("生成されたプロンプトは役立ちましたか？", ("はい", "いいえ"))
# if feedback == "いいえ":
#     improvement_suggestion = st.text_area("改善のためのフィードバックをお願いします:")
#     if st.button("フィードバックを送信"):
#         # ここでフィードバックを保存または処理するロジックを追加できます
#         st.success("フィードバックをいただき、ありがとうございます。")

# 使用方法の説明
st.markdown("""
## 使用方法
1. 上のテキストエリアにAIツールで実現したいことや目的を入力してください。
2. 入力後、自動的により効果的なプロンプトが生成されます。
3. 生成されたプロンプトを使用して、AIツールでより良い結果を得ることができます。
4. プロンプトが役立ったかどうか、フィードバックを提供してください。

## ヒント
- 具体的な目的や望む結果を明確に記述すると、より適切なプロンプトが生成されます。
- 生成されたプロンプトは、必要に応じて微調整することができます。
- フィードバックは、このツールの改善に役立ちます。
""")