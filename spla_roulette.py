import collections.abc
import streamlit as st
import random as rd
import streamlit.components.v1 as stc

st.title('ブキルーレットアプリ')
st.caption('created by taichaemon')
st.subheader('スプラ3全通常ブキ130種')
duplication_category = st.radio('【重複】', ('あり', 'なし'), horizontal=True)
population_category = st.radio('【人数】', ('1', '2', '3', '4', '5', '6', '7', '8'), horizontal=True)

l = ['わかば', 
    'もみじ', 
    'ボールド', 
    'ボルネオ',
    'シャーカー',
    'シマネ',
    'スシ',
    'スシコラ',
    'プライム',
    'プラコラ',
    '52',
    '52デコ',
    '96',
    '96デコ',
    'ジェッスイ',
    'ジェッカス',
    '黒ザップ',
    '赤ザップ',
    '銀モデ',
    '金モデ',
    'スペシ',
    'スペコラ',
    'L3',
    'L3D',
    'H3',
    'H3D',
    'ボトル',
    'ボイル',
    'ホッブラ',
    'ホッカス',
    'ロンブラ',
    'ロンカス',
    'ラピブラ',
    'ラピデコ',
    'エリブラ',
    'エリデコ',
    'ノヴァ',
    'ノヴァネオ',
    'クラブラ',
    'クラネオ',
    'Sブラ',
    'クイブラ',
    'スプロラ',
    'ロラコラ',
    'カーボン',
    'カーデコ',
    'ヴァリアブル',
    'ヴァリフォイ',
    'ダイナモ',
    'テスラ',
    'ワイロ',
    'ワイコラ',
    'パブロ',
    'パブヒュー',
    'ホクサイ',
    'ホクヒュー',
    'フィン',
    'フィンヒュー',
    'スプチャ',
    'チャーコラ',
    'スプスコ',
    'スココラ',
    'リッター',
    'リッカス',
    'リッスコ',
    'スコカス',
    'スクイクa',
    'スクイクb',
    '甲竹',
    '乙竹',
    'ソイチュ',
    'ソイカス',
    '青鉛筆',
    '赤鉛筆',
    'バケスロ',
    'バケデコ',
    'ヒッセン',
    'ヒッヒュー',
    'スクスロ',
    'スクネオ',
    'エクス',
    'エッカス',
    'オフロ',
    'フロデコ',
    'モップ',
    'モップD',
    'バレル',
    'バレデコ',
    'スプスピ',
    'スピコラ',
    'ハイドラ',
    'ハイカス',
    'クーゲル',
    'クゲヒュー',
    'ノーチ',
    '金ノーチ',
    'イグザミ',
    'イグヒュー',
    'スプマニュ',
    'マニュコラ',
    'ケルビン',
    'ケルデコ',
    'デュアル',
    'デュアカス',
    '赤スパ',
    '青スパ',
    '黒クア',
    '白クア',
    'ガエン',
    'ガエカス',
    'パラ',
    'パラソレ',
    'キャンプ',
    'キャンソレ',
    'スパイ',
    'スパソレ',
    '甲傘',
    '乙傘',
    'トラスト',
    'トラコラ',
    'ラクト',
    'ラクデコ',
    'フルイド',
    'フルカス',
    'ドライブ',
    'ドブデコ',
    'ジム',
    'ジムヒュー',
    '青デンタル',
    '黒デンタル']
if duplication_category == 'あり':
    l2 = rd.choices(l, k=len(l))
else:
    l2 = rd.sample(l, len(l))
if population_category == '1':
    order =  l2[0]
elif population_category == '2':
    order = '1,' + l2[0] +' 2,' + l2[1]
elif population_category == '3':
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2]
elif population_category == '4':
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2] + ' 4,' + l2[3]
elif population_category == '5':
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2] + ' 4,' + l2[3] + ' 5,' + l2[4]
elif population_category == '6':
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2] + ' 4,' + l2[3] + ' 5,' + l2[4] + ' 6,' + l2[5]
elif population_category == '7':
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2] + ' 4,' + l2[3] + ' 5,' + l2[4] + ' 6,' + l2[5] + ' 7,' + l2[6]
else:
    order = '1,' + l2[0] +' 2,' + l2[1] + ' 3,' + l2[2] + ' 4,' + l2[3] + ' 5,' + l2[4] + ' 6,' + l2[5] + ' 7,' + l2[6] + ' 8,' + l2[7]

html_content = f"""
<button onclick="navigator.clipboard.writeText('{order}')">
    コピー
</button>
"""

if st.button('ルーレット実行'):
    st.code(order, language=None, wrap_lines=True)
    stc.html(html_content, height=50)
