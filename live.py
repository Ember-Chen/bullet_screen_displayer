from bilibili_api import Credential
import json
credential = Credential(
    sessdata="bc0c8478%2C1732251861%2Cba3de%2A52CjBz5ESK5_pQE8dK7HviE8uLtvPdShMDMD3T6_R7B9oWayBZAujOLyAMW-BgFsC-LCoSVkhZRWl6YUhNazlWYkRicVIzZ19RVlVPZTFxVzlBSkN1Ri1fN3NBOGNaR1VSTjRkOERydjlLV19uYlh5SHg0UmxxV0R4OGU2bzhHckhoVFBrVVJBQkx3IIEC",
    bili_jct="5d10d29620babf68b23129c612efa8b2",
    buvid3="E5BBCAF6-E4D2-72A3-11E1-5C2FA0F2061086293infoc",
    dedeuserid="176491860",
    ac_time_value="4b5f2c9f6533c56daadda0a6604a6952"
)

from bilibili_api import live, sync

room = live.LiveDanmaku(14047,credential=credential)

@room.on('DANMU_MSG')
async def on_danmaku(event):
    # 收到弹幕
    print(event)
    msg = event["data"]["info"][1]
    print(f"信息: {msg}")
    with open(file='output.json',mode='a',encoding='UTF-8') as f:
        f.write(json.dumps(event))
        f.write(',\n')

@room.on('SEND_GIFT')
async def on_gift(event):
    # 收到礼物
    print(event)

sync(room.connect())