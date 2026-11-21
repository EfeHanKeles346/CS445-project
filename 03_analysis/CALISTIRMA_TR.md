# Analizi yeniden çalıştırma

Notebook'un kayıtlı çıktıları hazır. Veri internetten yeniden indirilmeden okunabilir. Python 3.12 ile çalıştırıldı. Aşağıdaki komutlar milestone klasörünün içinde kullanılabilir; yeni sanal ortam bu klasörde oluşturulur.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r 03_analysis/requirements.txt
python 03_analysis/milestone_analysis.py
```

Çıktılar `04_data/processed` ve `08_figures` içinde yeniden üretilir. Ham veri değişmez. Script herhangi bir platforma sonuç göndermez ve model indirmez.

Notebook için VS Code veya mevcut Jupyter ortamınızda aynı sanal ortamı kernel olarak seçin. Notebook'u `03_analysis` klasöründen çalıştırın. Çalışma dizini farklıysa ilk hücrede `ROOT` değerini milestone klasörüne ayarlayın.

## İçerik ve sınırlar

- EDA ve veri kalite kontrolleri
- Önerilen beş kelime fold'u
- Her kelimeyi tek kümeye atan bir dosya biçimi denemesi
- Organizasyonun değiştirilmemiş evaluator'ı ile gerçek skor hesaplaması

`single_cluster_format_example.zip` yalnızca yerel format örneğidir; platforma yüklenmedi. Referans etiketleri tahmin üretiminde kullanılmaz. Neural model yoktur. BCubed değeri aynı geliştirme verisindeki tanısal sonuçtur; bağımsız test sonucu değildir.

İstatistiklerde boşlukla ayrılan token sayısı kullanılıyor; bu sayı modelin subword token sayısı değildir. Hedef ofsetler Python karakter dilimlemesiyle incelenir. Harf değişimi, metin temizleme veya normalizasyon yapılırsa ofsetlerin yeniden eşleştirilmesi gerekir.

## Kaynak ve katkı

Analiz script'i AI destekli çalışma taslağıdır. Ders politikasına göre inceleyin, anlayın ve izin verilen kapsamda uyarlayın. Resmî scorer `07_sources/scorer` içinde ayrı tutulmuştur. Bu dosyaları kendi yazdığınız kod gibi sunmayın. `requirements.txt` analizin çalıştığı paket sürümlerini sabitler.
