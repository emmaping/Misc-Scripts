# Misc-Scripts

##TransDoukanDictToCsv.py
因为很喜欢多看系统能把书摘导入印象笔记，所以刷了系统，但是之后生词本就没法导出了，研究了一下多看生词本位置在

DK_System\xKindle\res\dict\VocabularyNoteBook.dat

格式是字典列表直接转化成了字符串，于是写了这个脚本把VocabularyNoteBook.dat转化成VocabularyNoteBook.csv方便导入到其他APP（比如我最爱的ANKI）中复习。

使用时候把脚本放在VocabularyNoteBook.dat同目录中执行即可，生成csv文件的第一列是生词，第二列是释义，第三列是时间，忽略即可。另外用Excel打开是乱码，不用担心，不影响Anki导入后效果,用notepad++之类软件打开也是正常的。

PS:遗憾的是，Kindle原生系统生词本会保留生词所在例句，多看系统只有生词和释义, 而且有些释义被截断了，原始文件就这样

##ImportAnki -Voice as question.py
我喜欢用Aboboo看《好媳妇》，遇到听不懂的句子就ctrl+A保存到句库，但是这样复习起来很麻烦，Aboboo可以把句库导出为单个音频+lrc文件的格式，我写了这个脚本用来把音频和对应英文导入Anki复习用。用法是这样的：
1. Aboboo->我的->句库->导出->按句子方式导出到文件夹
2. ImportAnki -Voice as question.py放入文件夹中，执行
3. 把所有mp3文件拷贝到Anki存放多媒体文件的目录，类似C:\Users\xxx\Documents\Anki\xxx\collection.media
4. 打开Anki，导入生成的Tobeimport.csv，注意分隔符是逗号
