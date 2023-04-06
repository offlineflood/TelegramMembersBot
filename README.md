# Telegram Members Bot
<p align="center">
  <img src="https://raw.githubusercontent.com/offlineflood/TelegramMembersBot/master/.image/20191203_205322.jpg" width="470" height="150">
</p>

<p align="center"><img src="https://img.shields.io/badge/Version-3.1-brightgreen"></p>
<p align="center">
  <a href="https://github.com/offlineflood">
    <img src="https://img.shields.io/github/followers/offlineflood?label=Follow&style=social">
  </a>
  <a href="https://github.com/offlineflood/TelegramMembersBot">
    <img src="https://img.shields.io/github/stars/offlineflood/TelegramMembersBot?style=social">
  </a>
</p>
<p align="center">
  Telegram Members Bot
</p>
<p align="center">
</p>

---

## • API Quraşdırma
* http://my.telegram.org saytına daxil olun və daxil olun.
* API inkişaf alətlərinə klikləyin və tələb olunan sahələri doldurun.
* istədiyiniz proqram adını qoyun və platformada digərini seçin Misal:
* Tətbiq yarat düyməsini kliklədikdən sonra "api_id" və "api_hash" kopyalayın (setup.py-də istifadə olunacaq)

## • Necə Quraşdırılır və İstifadə Edilir.

```bash
$ pkg install -y git python
```

```bash
$ git clone https://github.com/offlineflood/TelegramMembersBot.git
```

```bash
$ cd TelegramMembersBot
```

* Quraşdırma tələbləri

```bash
$ python setup.py -i
```

* quraşdırma konfiqurasiya faylı (apiID, apiHASH).

```bash
$ python setup.py -c
```

* İstifadəçi məlumatlarını yaratmaq üçün

```bash
$ python scraper.py
```

* (adı dəyişsəniz, member.csv defoltdur, ondan istifadə edin)
* Toplanmış məlumatlara toplu sms göndərin.

```bash
$ python add2group.py members.csv
```

* Yeniləmə Aləti

```bash
$ python setup.py -u
```
