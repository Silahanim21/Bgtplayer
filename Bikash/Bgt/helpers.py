HELP_1 = """✅**<u>Admin Commands:</u>**

**c** stands for channel play.

/durdur veya /cpause - Çalınan müziği duraklatın.

 /dewam veya /cresume- Duraklatılan müziği devam ettirir.

 /sessiz veya /cmute- Çalan müziğin sesini kapatın.

 /unsessiz veya /cunmute- Sessiz müziğin sesini açar.

 /karistir veya /cshuffle- Sıradaki çalma listesini rastgele karıştırır.

 /atla veya /cskip- Geçerli çalan müziği atla.

 /son veya /cstop- Müzik çalmayı durdurun.

 /restart veya /reload - Sohbetiniz için botu yeniden başlatın 
"""

HELP_2 = """✅<u>**Auth Users:**</u>
Kimlik Doğrulama Kullanıcılar, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.

 /auth [Kullanıcı Adı] - Grubun YETKİ LİSTESİNE bir kullanıcı ekleyin.

 /unauth [Kullanıcı adı] - Bir kullanıcıyı grubun YETKİLENDİRME LİSTESİ'nden kaldırın.

 /authusers - Grubun YETKİLENDİRME LİSTESİNİ kontrol edin."""

HELP_3 = """⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**

/blacklistchat [CHAT_ID] - Müzik Botu kullanılarak yapılan tüm sohbetleri kara listeye alın

 /whitelistchat [CHAT_ID] - Müzik Botu kullanılarak kara listeye alınan tüm sohbetleri beyaz listeye ekleyin

 /blacklistedchat - Kara listedeki tüm sohbetleri kontrol edin.

👤**<u>BLOCKED FUNCTION:</u>**

/block [Kullanıcı Adı veya Kullanıcıya Yanıtla] - Kullanıcının bot komutlarını kullanmasını engeller.

 /unblock [Kullanıcı Adı veya Kullanıcıya Yanıtla] - Bir kullanıcıyı Bot'un Engellenen Listesinden kaldırın.

 /blockedusers - Engellenen Kullanıcı Listelerini kontrol edin
."""

HELP_4 = """🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Mesaj Gönder veya Mesaja Yanıt Ver] - Herhangi bir mesajı Bot'un Sunulan Sohbetlerine yayınla.

 yayın seçenekleri:

 -pin : Bu, mesajınızı sabitleyecektir 

 -pinloud : Bu, mesajınızı yüksek sesli bildirimle sabitler

 -user : Bu, mesajınızı botunuzu başlatan kullanıcılara yayınlayacaktır.

 -assistant : Bu, mesajınızı botunuzun asistan hesabından yayınlayacaktır.

 -nobot : Bu, botunuzu mesaj yayınlamamaya zorlar

 Örnek: /broadcast -user -assistant -pin Merhaba Testi

"""
HELP_5 = """✅<u>**Extra  Commands:**</u>

/loop veya /cloop [etkinleştir/devre dışı bırak] veya [1-10 arası sayılar] 
     - Etkinleştirildiğinde bot, sesli sohbette çalmakta olan müziği 1-10 kez döngüye alır.  Varsayılan olarak 10 kez.

 /language veya /langs : dili İngilizce'den Bangla'ya değiştirmek için 

 /sarkisozu [Müzik Adı] - Web'de belirli bir Müziğin Şarkı Sözlerini arar."""

HELP_6 = """✅**<u>Bot's Server Playlists:</u>**

/playlist - Sunuculardaki Kayıtlı Çalma Listenizi Kontrol Edin.

 /deleteplaylist - Çalma listenizdeki kayıtlı müzikleri silin

 /oynat - Kayıtlı Çalma Listenizi Sunuculardan oynatmaya başlayın."""

 HELP_7 = """✅<u>**ping cmd:**</u>

 /ping- Bot'a ping atın ve Bot'un Ram, Cpu vb. istatistiklerini kontrol edin.

 /stats - En İyi 10 Parçanın Küresel İstatistiklerini, En İyi 10 Bot Kullanıcısını, Bottaki En İyi 10 Sohbeti, Bir sohbette Oynanan İlk 10'u vs. alın..."""

HELP_8 = """✅<u>**Play Commands:**</u>

Kullanılabilir Komutlar = oynat, bgt, vplay, cplay

 ForcePlay Komutları = playforce, bgtforce vplayforce, cplayforce

 c kanal oynatma anlamına gelir.
 v video oynatma anlamına gelir.
 kuvvet, kuvvet oyunu anlamına gelir.

 /oynat veya /voynat veya /cplay - Bot, sesli sohbette verilen sorgunuzu oynatmaya veya sesli sohbetlerdeki canlı bağlantıları yayınlamaya başlayacaktır.

 /playforce veya /force veya /vplayforce veya /cplayforce - Force Play, sesli sohbette geçerli çalınan parçayı durdurur ve aranan parçayı sırayı bozmadan/temizlemeden anında çalmaya başlar.

 /channelplay [Sohbet kullanıcı adı veya kimliği] veya [Devre Dışı Bırak] - Kanalı bir gruba bağlayın ve grubunuzdan kanalın sesli sohbetinde müzik akışı yapın.."""

HELP_9 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**

/addsudo [Kullanıcı adı veya kullanıcıya yanıt ver]

 /delsudo [Kullanıcı Adı veya Kullanıcıya Cevap Ver]

 🛃HEROKU:

 /usage - Dyno Kullanımı.

 🌐VARLARI YAPILANDIRMA:

 /get_var - Heroku veya .env'den bir yapılandırma değişkeni alın.

 /del_var - Heroku veya .env'deki tüm değişkenleri silin.

 /set_var [Var Name] [Value] - Heroku veya .env üzerinde bir Var Ayarlayın veya Bir Var Güncelleyin.  Var ve Değerini boşlukla ayırın.


🤖**<u>BOT COMMANDS:</u>**

/reboot - Botunuzu yeniden başlatın. 
 /update - Botu Güncelle.
 /speedtest - Sunucu hızlarını kontrol edin
 /bakım [etkinleştir / devre dışı bırak] 
 /logger [etkinleştir / devre dışı bırak] - Bot, aranan sorguları günlükçü grubunda günlüğe kaydeder.
 /get_log [Satır Sayısı] - Heroku veya vps'ten botunuzun günlüğünü alın.  Her ikisi için de işe yarar.

 ⚡️ÖZEL BOT İŞLEVİ:
 /authorize [CHAT_ID] - Botunuzu kullanmak için sohbete izin verin.
 /unauthorize [CHAT_ID] - Sohbetin botunuzu kullanmasına izin vermeyin.
 /yetkili - Botunuzun izin verilen tüm sohbetlerini kontrol edin.
"""

HELP_10 = """🤑 **<u>Active Chats:</u>**

/activevoice - Bottaki aktif sesli sohbetleri kontrol edin.
 /activevideo - Bottaki etkin video görüşmelerini kontrol edin.
 /autoend [enable|disable] - Kimse dinlemiyorsa 3 dakika sonra otomatik akışın sonlandırılmasını etkinleştirin.."""
HELP_11 = """😅**<u> started with bot</u>**
/start : botu başlat

 /help : Komutların ayrıntılı açıklamalarını içeren Komut Yardımcı Menüsünü alın.

 /reboot : sohbetiniz için botu yeniden başlatın.

 /settings - Satır içi düğmelerle tüm grubun ayarlarını alın.

 /sudolist - Müzik Botunun Sudo Kullanıcılarını Kontrol Edin"""

HELP_12 = """👤**<u>GBAN FUNCTION:</u>**

/gban [Kullanıcı adı veya kullanıcıya yanıt ver] - Bir kullanıcıyı botun sunulan sohbetinden yasaklayın ve onun botunuzu kullanmasını engelleyin.

 /ungban [Kullanıcı Adı veya Kullanıcıya Cevap Ver] - Bir kullanıcıyı Bot'un yasaklı Listesinden kaldırın ve botunuzu kullanmasına izin verin

 /gbannedusers - Gbanned Kullanıcı Listelerini kontrol edin."""

HELP_13 = """🆔**<u>ID/INFO FUNCTION:</u>**

/id or /info- info çeker ya."""

HELP_14 = """**<u>GOOGLE FUNCTION:</u>**

/google - gogle arama motoru ."""

HELP_15 = """**<u>IMAGE FUNCTION:</u>**

/image - fotoğraf uluştur"""

HELP_16 = """**<u>MORE FUNCTION:</u>**

/ask - Herhangi bir şey sor 

 /bikash - Bikash'ın kim olduğunu kontrol edin

 /sahibi - bu reponun yaratıcısının kim olduğunu kontrol edin

 /donate - bot sahibine bağış yapın 🙂"""

HELP_17 = """**<u>REPO FUNCTION:</u>**

/repo - kaynak kod."""

HELP_18 = """**<u>SEEK FUNCTION:</u>**

/seek veya /cseek - İleri Müziği sürenize göre arayın

 /seekback veya /cseekback - Geriye doğru Müziği istediğiniz süreye göre arayın."""


