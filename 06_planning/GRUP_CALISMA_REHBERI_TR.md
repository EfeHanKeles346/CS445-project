# Task 3 için grup çalışma rehberi

## 1 Problemi birlikte anlamak

Bir kelime farklı bağlamlarda farklı anlamlar taşıyabilir. Biz her kullanımı, anlam bakımından benzer kullanımlarla gruplamak istiyoruz. Sonra aynı grupların resmî dönemlerde ne kadar görüldüğünü inceleyebiliriz.

Örneğin hayvan olarak kullanılan fare ile bilgisayar aygıtı olarak kullanılan fare farklı gruplara gidebilir. Bu Türkçe örnek öğretici bir örnektir; veri setinin bir parçası değildir. Küme numarası bir isim değildir. Küme 0 ile küme 5'in numarasını değiştirmek, üyelikler aynı kaldığı sürece anlamı değiştirmez.

Bizim kapsamımız Subtask 1. 1a gruplamayı, 1b zamansal değişimi değerlendirir. İkisinin hesabı aynı kullanım tahminlerinden türetilebilir. Subtask 2'deki hazır anlam tanımına göre ikili sınıflandırma bu paketin kapsamında değil.

Güncel Codabench açıklaması eski tanıtım sayfasındaki hatayı düzeltiyor: Subtask 1 girdisinde anlam tanımı yok. `definitions.jsonl` dosyası Subtask 2 için. Değerlendirme `year` yerine `period_label` alanına dayanıyor.

## 2 Hazır veriyi nasıl okuyacağız

`04_data/raw/dev/SV/usages.jsonl` satır bazında JSON kayıtları içerir. Her kayıt için şu alanlar bulunur:

| Alan | Anlamı |
|---|---|
| `word` | Hedef kelimenin lemma biçimi |
| `sentence_id` | Kullanım kimliği; anahtar olarak word ile birlikte kullanılır |
| `text` | Hedefin geçtiği bağlam |
| `start`, `end` | Python dilimlemesiyle hedefi gösteren karakter sınırları |
| `pos` | Sözcük türü |
| `year` | Yıl metaverisi |
| `period_label` | Resmî değerlendirme dönemi |

`text[start:end]` gerçek yüzey biçimini verir. `word=kvinna` iken metindeki biçim `kvinnor` olabilir. Bu farkı otomatik hata saymayacağız ve lemmayı arayıp ilk bulduğumuz yeri hedef seçmeyeceğiz.

Referans etiketleri ayrı `subtask1.jsonl` dosyasında. İki dosya `(word, sentence_id)` ile birleştiriliyor. Tahmin biçimi örneği `04_data/processed/real_record_example.json` içinde. Buradaki örnek tahmin yalnızca formatı gösterir.

## 3 EDA bulguları bize ne söylüyor

- **1.983 kullanım:** Bunlar anotatör sayısı değil, kullanım kayıtlarıdır.
- **10 kelime:** Her kelime için ayrı anlam grupları düşünmeliyiz. Farklı kelimelerin aynı sayısal etiketi ortak anlam olmak zorunda değildir.
- **10 dönem, eksik hücreler:** Beş kelime 10 dönemde, beş kelime 5 dönemde bulunuyor. 100 olası kelime-dönem hücresinin 75'i dolu. Her kelime için 9 geçiş var diyemeyiz.
- **Uzun zaman boşluğu:** 1912-1915 döneminden sonra 2006-2007 geliyor. Arada kesintisiz gözlem yok. Grafiklerde çizgiyle sürekli tarihsel süreç varmış gibi sunmayacağız.
- **262 çoklu etiket:** 244 kayıtta iki, 18 kayıtta üç referans anlam var. Tek küme atayan başlangıç yaklaşımının bu üyelikleri ifade edemediğini belirtmeliyiz.
- **Sıklık farkı:** skär 98, motiv 291 kullanım içeriyor. Değerlendirmede kelime başına skorların ortalamasını almak bu nedenle önemlidir.
- **Beş tekrar çifti:** Metinler aynı, resmi kimlikler farklı. Bunları çıktıdan silmek scorer'ın kayıt bekleme şartını bozar. Geliştirme ayrımında tekrarların iki tarafa düşmesini engellemeliyiz.
- **Yardımcı tablo:** `senses_count.tsv` ile JSONL'den hesaplanan farklı anlam sayısı 69 hücrede uyuşmuyor. Nedenini kesin bilmiyoruz. Hesaplarımızın kaynağı JSONL etiketleridir.

Grafiklerin her biri için gruptan biri üç cümle kurabilmeli: ne ölçüldü, ne bulduk, yöntem kararını nasıl etkiliyor.

## 4 Makaleleri nasıl okuyacağız

Okuma sırası 2020 ACL, 2023 ACL, 2024 NAACL olsun. Her birini önce özet, yöntem, deney kurulumu ve sınırlılıklar açısından inceleyin. `05_literature/OKUMA_NOTLARI_TR.md` başlangıç notlarını içeriyor; tam metnin yerini almıyor.

Her makaleyi bitirince bir üye şu bilgileri kendi cümleleriyle yazsın: yöntemin girdisi, ürettiği çıktı, bizim alacağımız fikir ve bizim verimizde değişmesi gereken şey. Eski bir makalenin başka veri üzerindeki puanını bizim performansımız gibi kullanmayacağız.

## 5 Yöntem önerisini değerlendirmek

Öneri, hedefi işaretlenmiş bağlamlar için XL-LEXEME temsilleri çıkarmak ve aynı kelimenin tüm dönemlerdeki kullanımlarını birlikte kümelemek. Böylece ayrı dönemlerde oluşmuş iki keyfi küme numarasını yanlışlıkla aynı anlam kabul etme sorunu azalır.

Başlangıç kümeleme adayı K-means. K=2..10 arasını silhouette ile karşılaştırmak düşünülebilir. Bu aralık hazır doğru anlam sayısı değildir; 2020 makalesinden esinlenen bir başlangıçtır. Tek anlamlı kelimeyi zorunlu olarak bölme riskini incelemek için tek-küme kontrolünü ve affinity propagation alternatifini plana aldık. Suga için referansta 12 anlam bulunması da küçük sabit K aralığının sınırını gösterir; gerçek deneyde aralık duyarlılığı ayrıca incelenmelidir. Referanstaki anlam sayısını tahmin sırasında doğrudan K olarak vermeyeceğiz.

Milestone'da bu yaklaşım taslak olarak sunuluyor. Model dosyaları henüz indirilmedi, GPU gereksinimi ölçülmedi ve neural deney sonucu yok. Böyle bir sonucun var olduğunu söylemeyin.

## 6 Değerlendirmeyi nasıl planladık

`proposed_word_folds.json` dosyası seed 445 ile oluşturulan beş bölümü içerir. Her bölüm iki kelimeyi doğrulama, sekiz kelimeyi ayar seçimi için ayırır. Doğrulama kelimesinin tüm dönemlerini beraber tutuyoruz. Girdi temsilini ve kümelemeyi o kelimenin etiketsiz kullanımları üzerinde yapmak planlanan tümevarımsal kümeleme değil, transdüktif değerlendirme düzenidir; gold anlamlar modele verilmez.

Bütün veri EDA'da görüldüğü için bu bir geliştirme karşılaştırmasıdır. Bağımsız, hiç görülmemiş test sonucu diye sunulamaz. Birden fazla ayarı karşılaştırırken validation etiketlerini tekrar tekrar kullanıp bunu test sonucu gibi adlandırmayacağız.

Resmî scorer 1b için iki dönemde de en az 10 kullanım ister. Bu release'te 65 aday geçişin 60'ı kalır. Çoklu anlamın toplam ağırlığı 1 olacak şekilde paylaştırılır. Kod Jensen-Shannon **distance** kullanır; web açıklamasındaki divergence sözcüğünü koddan ayrı not ettik. Sabitlenen scorer'ı aynen kullanmak karşılaştırmayı tutarlı tutar.

Tek-küme denemesinin BCubed F1 değeri 0.7563'tür. Bu iyi bir anlamsal model yaptığımızı göstermez. Her kelimenin bütün kullanımlarını aynı kümeye koyduk. Amaç dosya biçiminin ve scorer bağlantısının çalıştığını göstermekti. Değişim skorları sabit olduğu için Spearman matematiksel olarak tanımsızdır; scorer bunu 0'a çevirir.

## 7 Grup toplantısının önerilen akışı

1. İlk 10 dakika: herkes Task 3'ü ve örnek girdiyi anlatır.
2. Sonraki 15 dakika: EDA grafikleri açılır; bir kişi veriyi açıklarken diğerleri sorar.
3. Sonraki 15 dakika: üç makalenin yöntemimize katkısı karşılaştırılır.
4. Sonraki 10 dakika: önerilen yöntem ve belirsizlikler değerlendirilir.
5. Son 10 dakika: gerçek sorumlular ve iç teslim tarihleri yazılır; sunumcu seçilir.

Bu bir toplantı önerisidir. Dört iş paketi dört kişi var demek değildir; gerçek ekip büyüklüğüne göre bölüştürün. Herkes genel proje sorularına hazırlanmalı.

## 8 Teslim öncesi kontrol

`MILESTONE_KONTROL_LISTESI.md` tamamlanmadan taslağı nihai teslim olarak kullanmayın. Raporun ana metni dört sayfa, kaynakça beşinci sayfada. Altı ana slayt yaklaşık 4 dakika 40 saniye için planlandı; 20 saniye geçiş payı var. Yedek slaytlar süreye dahil anlatılmak için değil, sorularda açılmak için hazırlanmıştır.

İlk sonraki iş: veri örneklerinden iki hedef kelime seçip arkadaşlarınıza girdi, hedef kelime aralığı, referans etiket ve tahmin biçimini açıklayın. Ardından makale okuma görevlerini paylaşın.
