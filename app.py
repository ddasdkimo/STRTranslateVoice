import pysrt
from pydub import AudioSegment
name = "檔案名稱路徑，不包含尾檔名"
subtitleList = pysrt.open(name+".srt", encoding="utf-8")
sound = AudioSegment.from_file(name+".wav", "wav")

for i in range(1,len(subtitleList)):
    print(str(i)+"_"+str(subtitleList[i-1].end - subtitleList[i].start))

root = "output/"

for item in subtitleList:
    soundtmp = sound[item.start.ordinal:item.end.ordinal]
    soundtmp.export(root+str(item.index)+"_"+item.text+".wav", format='wav') 