# CS 445 Task 3 milestone çalışma paketi

Hazırlanma tarihi: 14 Kasım 2026. Grup bilgileri henüz verilmediği için `GroupXXXXX` kullanıldı.

Bu klasör, grup arkadaşlarınızla inceleyip geliştireceğiniz **çalışma taslağıdır**. Veri hazırlığı, gerçek veri üzerinde EDA, kaynak seçimi, yöntem planı, rapor ve sunum dosyaları hazırlandı. Ana model eğitilmedi; model başarısı iddia edilmiyor. Üyelerin isimleri ve iş bölümü grup toplantısında tamamlanacak.

## Önce hangi dosyayı açmalıyız

1. `01_report/GroupXXXXX_milestone_report_SIMPLE.docx`: 21 Kasım güncel rapor; metin ve tablolar sadeleştirildi, analiz görselleri özgün halleriyle korundu. Kapak içermez. 4 sayfa ana metin ve 1 sayfa kaynakça; aynı isimli PDF de mevcut. Önceki `DRAFT` sürümü saklandı.
2. `02_presentation/GroupXXXXX_milestone_presentation_SIMPLE.pptx`: 6 ana slayt ve 2 gizli yedek slayt. Beyaz zemin ve siyah metin; özgün grafik korunmuştur. Düzenlenebilir grafik/tablo ve konuşmacı notları içerir.
3. `06_planning/GRUP_CALISMA_REHBERI_TR.md`: problemi, mevcut bulguları ve sıradaki kararları Türkçe açıklar.
4. `02_presentation/SUNUM_PROVA_VE_SORULAR_TR.md`: süre planı, konuşma önerisi ve olası sorular.
5. `03_analysis/GroupXXXXX_milestone_EDA.ipynb`: çalıştırılmış notebook; çıktı kayıtları korunmuştur.

Raporu düzenlemek için aynı isimli `.docx` dosyasını kullanın. `report_text_SIMPLE.txt` güncel metin ve tabloların düz metin kopyasıdır. `report_text_reference.txt` önceki sürümün paragraf referansıdır.

## Gerçekten tamamlananlar

- Resmî geliştirme verisi indirildi ve kaynak/hash bilgisi kaydedildi.
- 1.983 kullanım, 10 İsveççe hedef kelime ve 10 dönem etiketi doğrulandı.
- Veri ve referans kimlikleri bire bir eşleşti; eksik alan, sınır dışı/boş hedef aralığı ve yıl-dönem uyuşmazlığı bulunmadı.
- Kelime/dönem dağılımı, çoklu etiketler, bağlam uzunlukları ve tekrarlanan metinler incelendi.
- Dört EDA görseli PNG ve SVG olarak üretildi.
- ACL 2020, ACL 2023 ve NAACL 2024'ten üç makale seçildi; PDF ve BibTeX kayıtları saklandı.
- Resmî scorer'ın bir sürümü sabitlendi ve tek-küme format kontrolü çalıştırıldı.
- Rapor, sunum, yöntem taslağı, doğrulama önerisi ve iş paketleri hazırlandı.

## Teslimden önce sizde kalanlar

- Gerçek grup numarasını ve üyeleri yazın; iş paketlerine isim atayın.
- Öğrencilerin kendi rapor metnini hazırlaması ve kod kullanımını syllabus ile karşılaştırması gerekir. Ders PDF'sinin AI Use bölümü, raporun sıfırdan AI'a yazdırılmasına ve tüm kodun AI'a yazdırılmasına izin vermiyor. Buradaki AI taslağını doğrudan öğrenci yazımı gibi teslim etmeyin. Hazırlama kaydı `06_planning/AI_VE_KATKI_KAYDI.md` dosyasında.
- TA sunum saatini, dosya teslim saatini ve daha sonraki dil/değerlendirme kapsamını doğrulayın.
- Beş dakikalık sunumu prova edin. Her üye katılmalı ve soru-cevaba hazırlanmalı.
- Henüz neural model çalışmadı. Bu milestone için tamamlanmış model şartı belgede yok; sonraki çalışmalarda denenecek yöntem planı var.

## Klasörler

| Klasör | İçerik |
|---|---|
| `01_report` | İngilizce rapor taslağı, Word ve PDF |
| `02_presentation` | Slaytlar, Türkçe prova ve soru-cevap notu |
| `03_analysis` | Notebook, aynı analizin Python kaynağı, kurulum yönergesi |
| `04_data/raw` | Orijinal `dev.zip`, açılmış veri ve indirme manifesti |
| `04_data/processed` | Hesaplanan tablolar, kalite kayıtları, fold önerisi, scorer denemesi |
| `05_literature` | İzin verilen üç makale, okuma notları ve BibTeX |
| `06_planning` | Çalışma akışı, iş bölümü, teslim kontrolü ve katkı kaydı |
| `07_sources` | Ders PDF'si, resmî açıklama kopyaları ve değiştirilmemiş scorer |
| `08_figures` | Rapor için kullanılan ve ek inceleme için hazırlanan grafikler |
| `.build` | Üretim kaynakları ve özel görsel kontrol dosyaları; teslim malzemesi değildir |

## Kaynak sınırı

Bilimsel yöntem kaynağı olarak yalnızca hocanın izin verdiği **ACL ve NAACL** yayınları kullanıldı. Codabench ve organizatörlerin GitHub deposu görev/veri/ölçüm şartnamesi olarak kullanıldı. Blog, Medium yazısı, bağımsız arXiv ön baskısı veya izin listesi dışındaki bir workshop makalesi yöntem kaynağı yapılmadı.

Veri yalnızca yerel klasöre indirildi. SUCourse'a veya yarışma platformuna gönderim yapılmadı. Veri kullanımı için `07_sources/official/terms.md` dosyasındaki organizatör koşullarını koruyun.
