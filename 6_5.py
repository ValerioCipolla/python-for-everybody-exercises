str = 'X-DSPAM-Confidence:0.8475'

colon_index = str.find(":")
target = str[colon_index + 1:]
float_target = float(target)
print(type(float_target))
