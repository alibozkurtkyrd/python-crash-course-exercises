
# not a,b,c gibi değişkenler atadım bunun nedeni someone_profile dosyasında sonuç
# print ile basılmamış return ifadesi ile dönüldüğü için fonksiyon sonucunu ayrıca
# bastırmam gerekiyor

import build_profile

a = build_profile.someone_profile('barış','manço',
                            country='Turkey',
                            carreer='singer')
print("birinci yol:",a)

#not burada önemli bir hata yapm

from build_profile import someone_profile

b = someone_profile('tarık','akan', # burada modül ismi yazmadığımıza dikkat et
                    country = 'Turkey',
                    carreer = 'actor',)
print("ikinci yol:",b)

from build_profile import someone_profile as sp

c = sp('jim', 'fallon',
       country='usa',
       carreer='comedian')
print("üçüncü yol:",c)

import build_profile as b

d = b.someone_profile("david","beckham",
                      country="england",
                      carreer="fotball player")
print("dördüncü yol:",d)

from build_profile import * 

e = someone_profile('kemal','sunal',
                   country='Turkey',
                   carreer='actor')
print("beşinci yol:",e)
    

