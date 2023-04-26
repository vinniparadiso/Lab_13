#Vinni, Sarah, Breanna
fout=open("note3.txt", "w")
line7= "#There I was again tonight \n"
line8= "Forcing #laughter, faking smiles \n"
line9= "Same old tired, lonely #place \n"
line10= "Walls of #insecurity \n"
line11= "Shifting eyes #and vacancy \n"
line12= "Vanished #when I saw your face."

fout.write(line7)
fout.write(line8)
fout.write(line9)
fout.write(line10)
fout.write(line11)
fout.write(line12)

fout.close()

import re
def get_hashtag_ranking(input_sentence):
    hashtag_list=re.findall(r"#\w+", input_sentence)
    hashtag_count={}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag]+=1
        else:
            hashtag_count[hashtag]=1
    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]
    sorted_hashtags=sorted(hashtag_count.items(),key=get_frequency, reverse=True)
    output_list=[hashtag for (hashtag,count) in sorted_hashtags]
    return output_list
# my_sentence="note3.txt"
# my_list=get_hashtag_ranking(my_sentence)
fout1= open("note3.txt", "r")
for line in fout1:
    a= get_hashtag_ranking(line)
    print(a)
