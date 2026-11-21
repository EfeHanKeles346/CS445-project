# Sunum provası ve soru cevap notları

Sunum dili için İngilizce taslak hazırlandı. Bu dosya Türkçe çalışma yardımcısıdır. Slaytlardaki konuşmacı notları İngilizce açıklamaları içerir. Tüm metni okumak yerine kendi cümlelerinizle prova yapın.

## Süre planı

| Slayt | Konu | Hedef süre |
|---|---|---|
| 1 | Görev ve örnek | 35 sn |
| 2 | Veri ve girdi-çıktı | 40 sn |
| 3 | EDA bulguları | 50 sn |
| 4 | Üç makale | 35 sn |
| 5 | Yöntem ve değerlendirme | 65 sn |
| 6 | İş bölümü ve sonraki adımlar | 55 sn |
| | Ana anlatım toplamı | 280 sn |
| | Geçiş ve duraksama payı | 20 sn |

Güncel `SIMPLE` sürümünde 7 ve 8 numaralı slaytlar kaynakça ve ayrıntılı veri tablosudur; normal slayt gösterisinde gizlidir. Sorularda açın; ana anlatımı uzatmayın. Sunumu tek kişi yapabilir, bütün üyeler katılmalı.

## Her slaytta verilmesi gereken mesaj

**1.** Kelimenin farklı bağlamlardaki kullanımlarını anlam gruplarına ayırıyoruz. Sonra bu grupların dönemsel dağılımına bakıyoruz. Fare örneği öğretici örnek; veri setinden değil.

**2.** Resmî İsveççe geliştirme verisi hazır. 1.983 kullanım ve referans mevcut. Hedef kelime aralığını ve dönem etiketini koruyoruz. Girdide gold anlamı kullanmıyoruz.

**3.** Veri dengeli değil. Kelime başına örnek sayısı değişiyor, her kelime bütün dönemlerde yok. %13,21 çoklu etiket oranı, tek etiketli yaklaşımın sınırını gösteriyor. Grafikler gerçek veriden hesaplandı.

**4.** Üç kaynak da izinli konferanslardan. Birisi kullanım kümelemeyi, birisi temsil adayı XL-LEXEME'yi, diğeri kontrollü karşılaştırmayı destekliyor. Makale puanları bizim sonuçlarımız değil.

**5.** Yöntem plan: hedefi koruyarak temsil üretmek, kelime başına tüm dönemleri birlikte kümelemek, sonuçları resmî scorer ile ölçmek. Önerilen doğrulama beş fold ve kelime düzeyinde. Ana model henüz çalışmadı.

**6.** Bu aşamada iş paketleri öneri. Sunumdan önce To assign alanlarına gerçek isim yazılmalı. Henüz yapılmayan bir çalışmayı bir üyeye yapılmış gibi atfetmeyin. Sonraki adımlar yöntem kararını ve öğrenci raporunu tamamlamak.

## Olası sorular

**Neden sadece İsveççe?**
İndirdiğimiz güncel resmî geliştirme paketinin dili İsveççe. Çokdilli model adayı seçmek gelecekteki genişlemeyi destekleyebilir, fakat diğer dillerin verisini kullanmış değiliz.

**Kaç veri var?**
1.983 kullanım ve 1.983 eşleşen Subtask 1 referans kaydı. Bu sayı anotatör sayısı değildir. On hedef kelime var.

**Anlam sayısı hazır veriliyorsa neden kümeleme yapıyoruz?**
Geliştirme referansları EDA ve değerlendirme için erişilebilir. Tahmin algoritması gold küme kimliklerini girdi olarak almıyor. Amacımız kullanımları otomatik gruplamak.

**Küme numarasının kendisi doğru olmak zorunda mı?**
Hayır. Üyelik yapısı önemlidir. Örneğin bütün 0'ları 9 yapmak, gruplama aynıysa anlamı değiştirmez. Sayısal etiketleri doğrudan sınıf isimleriymiş gibi accuracy hesabına sokmayız.

**Neden yıl yerine period_label?**
Resmî değerlendirme bu alanı kullanıyor. Yıl metaveri olarak kalıyor. Dönem aralıklarını kendimiz değiştirmek karşılaştırmayı bozar.

**Neden ayrı ayrı her dönemde kümeleme yapmıyoruz?**
Ayrı dönemlerdeki küme numaraları kendiliğinden eşleşmez. Ortak kümeleme planı aynı kelimenin tüm dönemlerinde ortak bir grup kimliği oluşturuyor. Ayrı dönem kümelemesi seçilirse ayrıca anlam eşleştirme gerekir.

**K=2..10 neden?**
Bu, 2020 ACL yönteminden esinlenen başlangıç önerisi. Doğru anlam sayısını biliyoruz demiyoruz. K=1'i dışlaması ve fazla bölme riski sınırlılık. Alternatifleri ve aralık duyarlılığını değerlendireceğiz.

**Neden rastgele satır bazında train/test ayırmadınız?**
Yöntem ayarlarının başka hedef kelimelere taşınmasını incelemek istiyoruz. Aynı kelimenin dönemlerini birlikte tutan word-level fold önerdik. Gözlenen tekrarlar aynı kelimede olduğundan iki tarafa dağılmıyor. Bu bir geliştirme planı; bağımsız test yok.

**0.7563 F1 model sonucunuz mu?**
Bu her kelimeyi tek kümeye atan tanısal kontrolün geliştirme skorudur. XL-LEXEME veya öğrenilmiş bir sistemin sonucu değildir. Yüksek görünen bu değer tek başına anlam keşfinin iyi olduğunu göstermez. Makro BCubed hesaplanır; accuracy değildir.

**1b skorunuz neden 0?**
Tek küme kontrolünde anlam dağılımı değişmez. Tahmin edilen tüm değişim değerleri sabit olduğundan Spearman tanımsızdır; resmî kod bunu 0 olarak döndürür. Bu özel dönüşümü raporda belirtiyoruz.

**Eksik dönemleri sıfır anlam sıklığı sayabilir miyiz?**
Hayır. Örnek yokluğu anlamın dilde hiç kullanılmadığını göstermez. Dolu dönemleri resmî evaluator'ın kuralına göre karşılaştırıyoruz.

**Çoklu etiket nasıl işleniyor?**
Bir kullanıma birden fazla anlam atanabiliyor. İlk model önerisi tek etiket üretebilir. Referans dağılımlarında her etiket 1/etiket_sayısı ağırlık alıyor; toplam kullanım ağırlığı 1 kalıyor.

**Milestone'a kadar ne tamamlandı?**
Veri indirildi, kalite kontrolleri ve EDA çalıştı, kaynaklar seçildi, yöntem ve doğrulama taslağı yazıldı. Neural model eğitimi plan aşamasında.

**Sizin katkınız ne olacak?**
Kontrollü yöntem karşılaştırması, veri sorunlarının incelenmesi ve hataların açıklanması planlanıyor. Gerçek katkılar üyelerin yaptığı işlerle kaydedilecek. Hazır model ve resmi scorer bize ait değil.

**Neden senses_count.tsv sayılarını kullanmadınız?**
69 hücrede JSONL etiketlerinden hesaplanan benzersiz anlam sayılarıyla farklılık var. Tanımı doğrulanmadığı için bu dosyadan anlam sayısı iddiası kurmadık. Ham dosyayı koruduk.

## TA ile netleştirilecek noktalar

- Dersin Subtask 1 beklentisinde 1a ve 1b'nin kapsamı.
- İleride hangi dillerin beklendiği.
- Ders finali 4 Ocak iken yarışma değerlendirme verisinin daha sonra açılmasının nasıl ele alınacağı.
- Gerçek sunum slotu ve dosya teslim saati.

Bu soruların yanıtı şu anki veri hazırlığı ve EDA'nın yapılmasına engel değildir. Yanıtlar geldiğinde raporun Next Steps bölümü güncellenebilir.
