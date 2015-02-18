# Misc-Scripts

##TransDoukanDictToCsv.py
因为很喜欢多看系统能把书摘导入印象笔记，所以刷了系统，但是之后生词本就没法导出了，研究了一下多看生词本位置在

DK_System\xKindle\res\dict\VocabularyNoteBook.dat

格式是字典列表直接转化成了字符串，于是写了这个脚本把VocabularyNoteBook.dat转化成VocabularyNoteBook.csv方便导入到其他APP（比如我最爱的ANKI）中复习。

csv文件的第一列是生词，第二列是释义，第三列是时间，忽略即可。另外用Excel打开是乱码，不用担心，不影响Anki导入后效果,用notepad++之类软件打开也是正常的。

PS:遗憾的是，Kindle原生系统生词本会保留生词所在例句，多看系统只有生词和释义
