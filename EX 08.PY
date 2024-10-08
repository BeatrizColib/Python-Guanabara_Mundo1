metro= float(input('digite uma medida em metros: '))
print('A medida em metros é {}, em centímetros é {}, em milímetros é {}'.format(metro, metro*100, metro*1000))

metro= float(input('digite uma medida em metros: '))
dm = metro*10
cm = metro*100
mm = metro*1000
dam = metro/10
hm = metro/100
km = metro/1000
print('A medida em metros é {}, '
      '\n milimetro é {:.0f},'
      ' \n centimetro {:.0f},'
      ' \n decimetro {:.0f},'
      ' \n em decametros {},'
      ' \n hectometro é {}, '
      '\n km {}'
      .format(metro,mm,cm,dm,dam,hm,km))
