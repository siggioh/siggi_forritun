cm_str = input("Input cm: ") # do not change this line

cm_int = float(cm_str)


yards = round(cm_int // (3 * 12 * 2.54))
yards_afgangur = (cm_int % (3 * 12 * 2.54))


feets = round(yards_afgangur // (round(12*2.54)))
feets_afgangur = yards_afgangur % (round(12*2.54))

inches = round(feets_afgangur // 2.54)

print(yards, "yd. ", feets, 'ft.', inches, 'in.') # do not change this line
#, feets, 'ft.', inches, 'in.'

