### Vedat Milor API Servisi
Vedat Milor Lezzet Rehberi'ndeki işletmeleri şehir bazında çekmek için oluşturulmuş bir API servisidir.

#### Kullanım

GET isteği ile `/sehir/<string:sehir>` adresine istek atarak JSON formatında veri alabilirsiniz.

Örnek istek: `http://vedatmilor-api.vercel/sehir/istanbul`
Örnek cevap: 
```json
[
    {
        "name": "Paçacı Mahmut Usta",
        "url": "https://rehber.vedatmilor.com/item/pacaci-mahmut-usta/",
        "desc": "50’li yaşlarının başında vefat eden Mahmut Usta vaktinde Erzurum’dan İstanbul’a yerleşmiş. Meşhur Hünkar Lokantası’nda aşçılık yaptıktan sonra Kıztaşı’ndaki bu mütevazı esnaf lokantasını açmış. İlk başlarda kavurma, pilav ve paça çorbası servis edilirken zamanla menüye birçok yemek eklenmiş. Tabii, en özel yemekleri kuzudan yapılan paça çorbası. Terbiyesinde koyu kıvamlı manda yoğurdu, tereyağı ve un kullanılıyor. Sakatat sevmeyenleri bile kendisine hayran bırakacak düzeyde. Beğenilen yemeklerden bir diğeri işkembeli nohut. İlk defa Barcelona’da yemiştim. Hazırlaması kolay değil. Genel olarak, Paçacı Mahmut Usta’yı tıpkı yanındaki Paçacı Necip Usta gibi İstanbul’a değer katan bir esnaf lokantası olarak görüyorum.",
        "img": null
    }
]
```