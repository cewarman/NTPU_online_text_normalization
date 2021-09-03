# NTPU Online Text Normalization 臺北大學中英夾雜文字正規化系統 


---

## 簡介 (Introduction)
這個項目利用 <a href="http://slos.ce.ntpu.edu.tw/">http://120.126.151.132/</a> 的文字正規化網頁服務跟 Python HTTP 庫裡的 requests，在終端機上用指令實現文字正規化功能。
在這裡「文字正規化」是指把輸入的書寫體文字，轉換成口語體的文字，應用場景為文字轉語音系統的文字處理，比如「10%」要轉換成「百分之十」，目前此項目支援繁體中文以及繁體中文夾雜英文的輸入文字。

The *NTPU Online Text Normalization* provides the text normalization service from http://slos.ce.ntpu.edu.tw/. The users may simply use the API constructed by the Python HTTP library to access the Chinese-English mixed text normalization service from users' terminals. The term 'text normalization' in this service means the conversion from written-form texts to spoken-form texts. The NTPU Online Text Normalization may serve as a text analysis front-end in a Chinese-English mixed text-to-speech system, e.g., the written form "10%" is converted to a spoken form "百分之十." Currently, the service supports input texts encoded in traditional Chiense characters (UTF8) and/or English alphabets (ASCII).

---

## 用法 (Usage)：
```
$ python3 reqtest.py testin.txt
```
※如果要大量使用正規化功能(1G以上)，煩請告知，不然學校的網管會認為有異常。

※If you want to use the normalization function in large quantities(above 1G), please let me know, otherwise the school's network administrator will think something is abnormal.

---

## 原理 (Rationale)

這是一個基於規則法的文字正規化系統，以 openfst 建立標記需要被文字正規的文字區塊之搜尋網路，再以相對應的規則做轉換。不同於thrax將NSWs與SFWs放在FST的輸入輸出上，此系統將NSWs放在輸入，輸出則是其相對應的NSW-class。

---

## 作者 (Author)
國立臺北大學通訊工程學系語音暨訊號處理實驗室

通訊作者 (Corresponding Author)：北大通訊系研究生 李武豪, email : hank12451@gmail.com

其他作者：洪紹瑋、林衍廷、江振宇

實驗室主持人：江振宇 老師
