from discord_webhook import DiscordWebhook, DiscordEmbed

# Discord Sunucu Ayarları -> Entegrasyonlar -> Webhook oluştur -> Linki kopyala
url = input("Discord Webhook URL'sini yapıştır: ")
msg = input("Gönderilecek Mesaj: ")

webhook = DiscordWebhook(url=url, content=msg)

# Havalı bir Gömülü Mesaj (Embed) ekleyelim
embed = DiscordEmbed(title='Python Ajanı', description='Bu mesaj terminalden gönderildi.', color='03b2f8')
embed.set_footer(text='Intermediate Proje #38')
embed.set_timestamp()

webhook.add_embed(embed)

print("Gönderiliyor...")
response = webhook.execute()

if response.status_code == 200:
    print("✅ Mesaj Discord'a ulaştı!")
else:
    print(f"❌ Hata Kodu: {response.status_code}")