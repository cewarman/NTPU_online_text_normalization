# NTPU-CETN 臺北大學中英夾雜文字正規化系統 
NTPU-CETN 是 「NTPU Chinese-English Mixed (CEMixed) Text Normalization System」

## 簡介 (Introduction)
這個項目利用 <a href="http://120.126.151.132/">http://120.126.151.132/</a> 的文字正規化網頁服務跟 Python HTTP 庫裡的requests，在終端機上用指令實現文字正規化功能。
在這裡「文字正規化」是指把輸入的書寫體文字，轉換成口語體的文字，應用場景為文字轉語音系統的文字處理，比如「10%」要轉換成「百分之十」。 

This project provides the text-normalization service from http://120.126.151.132. The users may simply use the API constructed by the Python HTTP library to access the CEMixed text normalization service from users' terminals. The term 'text normalization' in this service means the conversion from written-form texts to spoken-form texts. The NTPU CEMixed Text Normalization System may serve as a text analysis front-end in a Chinese-English mixed text-to-speech system, e.g., the written form "10%" is converted to a spoken form "百分之十." 

## 用法 (Usage)：
```
$ python3 reqtest.py testin.txt
```

## 原理 (Rationale)

這是一個規則法的文字正規化系統，以openfst建立標記NSW的搜尋網路，再以相對應的規則做轉換。
