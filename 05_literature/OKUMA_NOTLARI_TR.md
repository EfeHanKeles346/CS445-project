# İzin verilen literatür ve okuma notları

Üç yayının konferans bilgisi ACL Anthology kaydından ve PDF'nin ilk sayfasından doğrulandı. PDF'ler `papers` klasöründe, kaynak kayıtları `references.bib` içinde. Bu kısa notlar makalelerin yerine geçmez.

| Kaynak | Yayın yeri | Önce okunacak bölüm | Bizim inceleme sorumuz |
|---|---|---|---|
| Giulianelli ve diğerleri 2020 | ACL | Bölüm 3 | Aynı kelimenin kullanımlarını nasıl temsillendirip gruplayabiliriz? |
| Cassotti ve diğerleri 2023 | ACL | Bölüm 3 ve 4 | Hedef kelimeyi dikkate alan temsili nasıl elde edebiliriz? |
| Periti ve Tahmasebi 2024 | NAACL | Bölüm 3–5 | Modelleri aynı koşullarda nasıl karşılaştırabiliriz? |

## Giulianelli ve diğerleri 2020

[Yayın kaydı](https://aclanthology.org/2020.acl-main.365/)

BERT kullanım temsilleri, kelime başına K-means ve dönemsel küme dağılımları bu çalışmanın temel parçaları. Yöntem K değerini 2–10 aralığında silhouette ile seçiyor. Biz bu aralığı kesin doğru anlam sayısı olarak almayacağız; bir başlangıç seçeneği olarak değerlendireceğiz. Makalenin İngilizce BERT kurulumu, mevcut İsveççe geliştirme verimize doğrudan aktarılmış bir deney değildir.

Okuma çıktısı: K seçimini ve ortak küme kimliklerini bir örnekle kendi cümlelerinizle açıklayın.

## Cassotti ve diğerleri 2023

[Yayın kaydı](https://aclanthology.org/2023.acl-short.135/)

XL-LEXEME, hedef kelimeyi işaretleyen ve word-in-context verisiyle eğitilmiş çokdilli bir bi-encoder sunuyor. Biz hazır modeli temsil adayı olarak değerlendireceğiz. Hedef işaretleme ve kesme kurallarını modelin yayıncı uygulamasından doğrulamak gerekiyor. Model tek başına projemizin kümeleme ve çıktı biçimini tamamlamıyor.

Okuma çıktısı: Aynı kelimenin iki farklı anlamı için temsillerin neyi ayırmasını beklediğinizi yazın. Modeli kullanmayı, modeli yeniden eğitmekten ayırın.

## Periti ve Tahmasebi 2024

[Yayın kaydı](https://aclanthology.org/2024.naacl-long.240/)

Çalışma farklı temsil modellerini ortak değerlendirme koşullarında karşılaştırıyor; word-in-context, anlam gruplama ve değişim ölçümünü ayırıyor. Bizim planımıza katkısı, yalnızca tek bir toplu değişim sayısına bakmadan kümeleme başarısını da değerlendirmek. Buradaki eski benchmark sonuçları bizim veri üzerindeki sonuçlar değildir.

Okuma çıktısı: Adil karşılaştırmada sabit tutacağımız girdileri, veri bölümünü ve değerlendirme kodunu listeleyin.

## Başlangıç kararları

- Ortak veri ve ortak scorer ile model/kümeleme karşılaştırması öneriliyor.
- XL-LEXEME adayı henüz indirilmedi veya çalıştırılmadı.
- APD tek başına kullanım kümeleri üretmediği için Subtask 1'in tamamını karşılayan ana çıktı olarak seçilmedi.
- K-means ve affinity propagation karşılaştırması plan; uygulanmış sonuç değil.
- Yeni bir makale eklenirse gerçek yayın yeri hocanın listesine göre kontrol edilmeli. ACL Anthology'nin bir arşiv olması, içindeki her workshop'u otomatik olarak izinli yapmaz.

Organizatörlerin veri ve scorer belgeleri teknik şartname olarak kullanıldı; yöntem literatürü listesine eklenmedi.
