text = "X-DSPAM-Confidence:    0.8475"
sppos = text.find(' ')
print(sppos)
val = text[19:]
print(val)
flval = float(val)
print(flval)
