# In Zusammenarbeit mit Felix Scholzn, Daniel Heisig und Simon Wagner Entstanden
# mem layout:
# 0: i
# 1: n
# 2: result


INP 1 # read n 
INC # increment it
STA 1 # save to data register 1
LDK 0 # initalise i and result
# init loop
STA 0 # init i
STA 2 # init result
# loop
label body:
LDA 0 # load i
PW3 # take it by the power of 3
ADD 2 # add the current result to it
STA 2 # # store it to data register 2

#end
#cmp
LDA 0 # load counter i
INC # increment i
STA 0 # store i back
CMP 1 # compare akkumulator to data register 1
JNEQ body # jump to start of loop if counter is not equal to n

# end of loop
OUT 2 # print result
HLT