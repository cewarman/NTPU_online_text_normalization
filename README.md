# 中英夾雜文字正規化系統 CEmix text normalization system
這個項目只是利用<a href="http://120.126.151.132/">http://120.126.151.132/</a>的文字正規化網頁服務跟Python HTTP庫裡的requests，在終端機上用指令實現文字正規化功能。
This project just uses the text-normalization service from 120.126.151.132 and requests in the Python HTTP library to implement text normalization on the terminal.

用法(usage)：
```
$ python3 reqtest.py testin.txt
```

這是一個規則法的文字正規化系統，以openfst建立標記NSW的搜尋網路，再以相對應的規則做轉換。
