import os
import json

_cache = {}

def get_text(lang, key):
    # Eğer dil dosyası bellekte yüklüyse (cache) doğrudan oku
    if lang in _cache:
        return _cache[lang].get(key, key)
    
    # Dosya yolunu güvenli şekilde oluştur
    file_path = os.path.join(os.path.dirname(__file__), f"{lang}.json")
    
    # Dosya yoksa key değerini doğrudan dön (çökmeyi önle)
    if not os.path.exists(file_path):
        return key
        
    # Dosyayı oku ve UTF-8 formatını koru
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            _cache[lang] = json.load(f)
        return _cache[lang].get(key, key)
    except Exception:
        # Herhangi bir hata durumunda (geçersiz JSON vb.) key dönerek çökmeyi önle
        return key
