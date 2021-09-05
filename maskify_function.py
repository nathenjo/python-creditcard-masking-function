def maskify(cc):
    if type(cc) == int:
        cc = str(cc)
    if len(cc) > 4:
        previousNumber = len(cc) - 4
        maskedNumbers = previousNumber*'#'
        return(f'{maskedNumbers}{cc[-4:]}')
    else:
        return(cc)

print(maskify('12569237'))
print(maskify('1256921356145711823174'))
print(maskify(1256921356145711823174))
print(maskify(12569237))
print(maskify('6431'))
print(maskify('64311'))
print(maskify('SkippyDooDa'))