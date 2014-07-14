konusucu
========

Markov zincirlerini kullanarak konuşur. Tkinter arayüzü de vardır.

Özetleme yazılımımı bitirdikten sonra, bir süredir bu yazılım üzerinde çalışıyordum. Şimdi bitti ve yayınlıyorum. Yine ilginç bir tasarım ile karşınızdayım...

Bu yazılım, .txt uzantılı bir kitabı açıyor. Ardından sizin belirlediğiniz zincir başına sözcük sayısı (ilerde açıklayacağım) ile Markov zincirleri oluşturuyor. Sonra sizinle konuşmaya hazır oluyor. İsterseniz "Ayarlar" sekmesinden yazılımın davranışlarını değiştirebilirsiniz.


Şu zincir başına sözcük sayısı ile ilgili bilgi vermek istiyorum. Çünkü yazılımında bununla ilgili verdiğim bilgiler yetersiz olabilir. Anlatayım: Zincir başına sözcük sayısı, bir diğer deyişle metnin kaçar kaçar bölünceğidir. Dolayısı ile; girdilerin, çıktıların kaçar kaçar denetleneceği, inceleneceğini de belirler. Bilmeniz gereken önemli bilgiler şunlar:
1. Bu sayı düştükçe, yazılımın verdiği çıktıların değişkenliği gelişigüzelliği artar. Bu kimi zaman yazılımı daha eğlenceli yapabilmesine karşın, sayıyı düşşürdüğünüzde anlamsız, karmaşık çıktılar alıyorsanız; bu değeri yükseltmelisiniz.
2. Bu sayı yükseldikçe yazılım daha yavaş çalışır. Hızı etkileyen en önemli etkenlerden biri budur. Yazılım yavaş çalışıyorsa, bunu düşürün.

Betikler ve görevleri:
markov.py -> Zincirleri oluşturan, girdileri alıp çıktıları veren, kısacası arkada görmediğiniz birçok işi yapan betik.
konuşucu.py -> Tkinter arayüzünü oluşturan, ayarları kaydeden ve açan betik.
