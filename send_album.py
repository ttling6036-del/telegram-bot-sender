"""
Telegram 相册发送（GitHub Actions 版）
用法：python send_album.py <群ID>
两张图以相册形式（同一条消息）一起发，带完整文案。
"""

import sys
import requests
import json

# ============ 配置 ============
BOT_TOKEN = "9015499752:AAE63es_CeMirbJ2RWVAFTPsxqT9GBX9ZWk"

# 图片放在仓库 images/ 目录，用 raw 直链（GitHub 服务器上的图片，Telegram 可直接拉取）
REPO_RAW = "https://raw.githubusercontent.com/ttling6036-del/telegram-bot-sender/main"
IMAGE_URLS = [
    f"{REPO_RAW}/images/img1.jpg",
    f"{REPO_RAW}/images/img2.jpg",
]

MESSAGE_TEXT = """✅Winbox✅ tekan link di Bawah sekarang!!!Register ⬇⬇⬇
https://tinyurl.com/3t45kr8u

🔥Monkey King【Misi Mingguan Telah Hadir! Menangkan Angpao Keberuntungan!】🧧🎉

🎮 Selesaikan misi mingguan untuk kesempatan memenangkan Angpao Keberuntungan hingga 8,888! Setiap minggu adalah peluang baru untuk menjadi salah satu pemenang beruntung!

🔥 Game Pilihan:
⚽ Football King
🀄 DragonX Mahjong
♠️ Super Ace Plus
❄️ Iceland
🌊 Great Blue
🧚 Fairy Garden Plus

🚀 Ikuti tantangannya dan mulai perjalanan Angpao Keberuntungan Anda hari ini!

#MonkeyKing #MisiMingguan #AngpaoKeberuntungan #HadiahAngpao #FootballKing #DragonXMahjong #SuperAcePlus #Iceland #GreatBlue #FairyGardenPlus #SlotGames"""
# ================================


def send_album(chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMediaGroup"
    media = []
    for i, img_url in enumerate(IMAGE_URLS):
        item = {"type": "photo", "media": img_url}
        if i == 0:
            item["caption"] = MESSAGE_TEXT
        media.append(item)
    data = {"chat_id": chat_id, "media": json.dumps(media)}
    r = requests.post(url, data=data, timeout=60)
    return r.json()


def main():
    if len(sys.argv) < 2:
        print("用法: python send_album.py <群ID>")
        sys.exit(1)

    chat_id = sys.argv[1]
    result = send_album(chat_id)

    if result.get("ok"):
        print(f"[✓] {chat_id} 相册发送成功")
    else:
        print(f"[✗] {chat_id} 失败: {result.get('description')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
