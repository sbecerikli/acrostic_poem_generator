# -*- coding: utf-8 -*-

# @Author: Seyfullah Becerikli <syfbcrkl>
# @Date:   2018-01-28T15:01:09+03:00
# @Email:  mail@seyfullahbecerikli.com.tr
# @Filename: acrostic_poem.py
# @Last modified by:   syfbcrkl
# @Last modified time: 2018-01-28T15:50:54+03:00

#This program takes two parameter(word and count) and generates an acrostic poem and each line includes up to count word
# if word list includes a word begins with parameter's first character.

import random
import sys

def main():

    my_poem = ""
    hansel_gretel = ['Öğle', 'üzeri', 'babalarıyla', 'üvey', 'anneleri', 'onlar', 'için', 'bir', 'ateş', 'yakmışlar', 've', 'hemen', 'geri', 'döneceklerini', 'söyleyip', 'ormanın', 'içinde', 'yok', 'olmuşlar.', 'Tabii', 'geri', 'dönmemişler', 'Kurtlar', 'etraflarında', 'ulurken', 'tir', 'tir', 'titreyen', 'Hansel', 've', 'Gretel', 'ay', 'doğana', 'kadar', 'ateşin', 'yanından', 'ayrılmamış.', 'Sonra', 'ay', 'ışığında', 'parlayan', 'çakılları', 'izleyerek', 'hemen', 'evin', 'yolunu', 'bulmuşlar.', 'Babaları', 'onları', 'görünce', 'sevinçten', 'havalar', 'uçmuş.', 'Üvey', 'anneleri', 'de', 'çok', 'sevinmiş', 'gibi', 'davranmış', 'ama', 'aslında', 'kararını', 'değiştirmemiş.', 'Üç', 'gün', 'sonra', 'onlardan', 'kurtulmayı', 'tekrar', 'denemek', 'istemiş.', 'Gece,', 'çocukların', 'odasının', 'kapısını', 'kilitlemiş.Bu', 'sefer', 'Hansel’in', 'çakıl', 'toplamasına', 'izin', 'vermemiş.', 'Ama', 'Hansel', 'zeki', 'bir', 'çocukmuş.', 'Sabah', 'ormana', 'doğru', 'yürürlerken,', 'akşam', 'yemeğinde', 'cebine', 'sakladığı', 'kuru', 'ekmeğin', 'kırıntılarını', 'yere', 'saçıp', 'arkasında', 'bir', 'iz', 'bırakmış.', 'Öğleye', 'doğru', 'üvey', 'anneleriyle', 'babaları', 'çocukları', 'yine', 'bırakıp', 'gitmişler.', 'Onların', 'geri', 'dönmediklerini', 'görünce,', 'Hansel', 've', 'Gretel', 'sabırla', 'ayın', 'doğup', 'yollarını', 'aydınlatmasını', 'beklemişler.', 'Ama', 'bu', 'sefer', 'geride', 'bıraktıkları', 'izi', 'bulamamışlar.', 'Çünkü', 'kuşlar', 'bütün', 'ekmek', 'kırıntılarını', 'yiyip', 'bitirmişler.', 'flask', 'lale']

    list_length = len(hansel_gretel)
    if(findWordBeginsF(hansel_gretel, len(hansel_gretel), str(sys.argv[1][0]))):
        for i in range(0, len(sys.argv[1])):
            my_poem += " " + findWordBeginsF(hansel_gretel, len(hansel_gretel), str(sys.argv[1][i]))
            for j in range(0, int(sys.argv[2]) - 1):
                rnd = random.randint(0, list_length)
                my_poem += " " + hansel_gretel[rnd]
            my_poem += "\n"
    print my_poem


def findWordBeginsF(plist, n, key):
    if not plist:
        print("There is no word begins with " + '\"' + sys.argv[1][0] + '\"')
        return
    elif(plist[0][0] == key):
        return plist[0]
    else:
        return findWordBeginsF(plist[1:], n-1, key)

if __name__== "__main__":
  main()
