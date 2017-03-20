# My 8 Ball

import random
# write answers
ans1="kskim"
ans2="dolbam"
ans3="sdhong"
ans4="son"
ans5="zeroxkim"
ans6="ianlee"

print("Welcome to My8Ball.")

choice=random.randint(1, 6)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
else:
	answer=ans6

# print the answer to the screen
print(answer)
