import discord
import asyncio
import os

# ===== 從環境變數讀取設定 =====
TOKEN = os.environ.get("TOKEN")
VOICE_CHANNEL_ID = int(os.environ.get("VOICE_CHANNEL_ID"))

# ==============================

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot 已上線：{client.user}")
    await join_voice_channel()

async def join_voice_channel():
    channel = client.get_channel(VOICE_CHANNEL_ID)
    if channel is None:
        print("❌ 找不到語音頻道，請確認 VOICE_CHANNEL_ID")
        return

    for vc in client.voice_clients:
        if vc.channel.id == VOICE_CHANNEL_ID:
            print("已在語音頻道中")
            return

    await channel.connect()
    print(f"🔊 已加入語音頻道：{channel.name}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.strip().lower() == "hey wake up!":
        await message.channel.send("yes")
        print(f"💬 偵測到喚醒訊息，已回覆 yes（頻道：{message.channel.name}）")

@client.event
async def on_voice_state_update(member, before, after):
    """如果 bot 被踢出語音頻道，自動重新加入"""
    if member == client.user and after.channel is None:
        print("⚠️ Bot 被移出語音頻道，5 秒後重新加入...")
        await asyncio.sleep(5)
        await join_voice_channel()

client.run(TOKEN)