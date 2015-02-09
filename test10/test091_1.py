#!/usr/bin/python
#-*-coding:utf-8-*-

# sm14946011.xmlをいじる
# urlはhttp://ext.nicovideo.jp/api/getthumbinfo/sm14946011

from lxml import etree
xml = """
<nicovideo_thumb_response status="ok">
    <thumb>
    <video_id>sm14946011</video_id>
        <title>俺のかずき</title>
        <description>
            ･･･orz とりあえず今日は飲みましょう。僕はもう飲んでますけど。かじゅきぃぃ頑張れぇぇぇぇ(｀･ω･´) 新作:sm16503370(←不出来を恥じ、次回頑張ります)
        </description>]
        <thumbnail_url>http://tn-skr4.smilevideo.jp/smile?i=14946011</thumbnail_url>
        <first_retrieve>2011-07-07T00:34:30+09:00</first_retrieve>
        <length>2:12</length>
        <movie_type>mp4</movie_type>
        <size_high>8022388</size_high>
        <size_low>4000698</size_low>
        <view_counter>3991</view_counter>
        <comment_num>130</comment_num>
        <mylist_counter>133</mylist_counter>
        <last_res_body>相変わらずいい解説だ A級復帰ならず・・・ 棋士ってのは髪の量で </last_res_body>
        <watch_url>http://www.nicovideo.jp/watch/sm14946011</watch_url>
        <thumb_type>video</thumb_type>
        <embeddable>1</embeddable>
        <no_live_play>1</no_live_play>
        <tags domain="jp">
            <tag lock="1">将棋</tag>
            <tag lock="1">木村一基</tag>
            <tag>百折不撓</tag>
            <tag>千駄ヶ谷の受け師</tag>
            <tag>愛される木村先生シリーズ</tag>
            <tag>将棋MAD</tag>
            <tag>駒得動画</tag>
            <tag>もっと評価されるべき</tag>
            <tag>晩成</tag>
            <tag>続編希望</tag>
        </tags>
        <user_id>3695965</user_id>
    </thumb>
</nicovideo_thumb_response>
"""
root = etree.fromstring(xml)
print root.tag