toplam_satilan_veya_kiralanan_konut_sayisi=0
toplam_satilan_veya_kiralanan_is_yeri_sayisi=0
toplam_satilan_veya_kiralanan_arsa_sayisi=0
toplam_satilan_emlak_sayisi=0
toplam_satilan_konut_sayisi=0
toplam_satilan_is_yeri_sayisi=0
toplam_satilan_arsa_sayisi=0
toplam_kiralanan_konut_sayisi=0          #BU KISIMDA GENEL SABITLER BULUNMAKTADIR
toplam_kiralanan_is_yer_sayisi=0     #KOD KARMASIKLIGI OLUSMAMASI BAKIMINDAN BAZI SATIR ARALARINA BOSLUK BIRAKILMISTIR
toplam_kiralanan_arsa_sayisi=0       #ICINDE ''TOPLAM'' YAZAN SABITLER BUTUN DANISMANLARI KAPSAMAKTADIR.
toplam_emlak_sayisi=0
satilan_konutlarin_toplam_bedeli=0
satilan_is_yerlerinin_toplam_bedeli=0
satilan_arsalarin_toplam_bedeli=0
en_yuksek_bedelle_satilan_emlagin_satis_bedeli=0
en_yuksek_bedelle_satilan_emlagin_tipi=0
en_yuksek_bedelle_satilan_emlagin_danismani=0
en_yuksek_bedelle_kiralanan_emlagin_kira_bedeli=0
en_yuksek_bedelle_kiralanan_emlagin_danismani=0
kira_bedeli_asgari_ucretten_buyuk_konut_sayisi=0
hic_satis_yapamayan_danisman_sayisi=0
en_cok_satis_yapan_danismanin_satis_sayisi=0
en_cok_satis_yapan_danismanin_adi=0
en_cok_satis_yapan_danismanin_sattigi_emlak_sayilari=0
en_cok_satis_yapan_danismanin_toplam_satis_bedeli=0
toplam_satis_bedeli_en_cok_olan_danismanin_satis_bedeli=0
toplam_satis_bedeli_en_cok_olan_danismanin_adi=0
toplam_satis_bedeli_en_cok_olan_danismanin_sattigi_emlak_sayilari=0
kotasini_dolduran_danisman_sayisi=0
primi_maasindan_buyuk_olan_danisman_sayisi=0
kiralanan_emlak_adedi_ondan_buyuk_yada_yirmibesbinden_buyuk_olan_danisman_sayisi=0
en_yuksek_prim_alan_danismanin_primi=0
en_yuksek_prim_alan_danismanin_adi=0
en_yuksek_prim_alan_danismanin_maasi=0
en_yuksek_prim_alan_danismanin_toplam_ucreti=0
en_dusuk_prim_alan_danismanin_primi=float('inf')
en_dusuk_prim_alan_danismanin_adi=0
en_dusuk_prim_alan_danismanin_maasi=0
en_dusuk_prim_alan_danismanin_toplam_ucreti=0
emlak_danismanlarina_odenecek_toplam_ucret=0
acentenin_kazandigi_toplam_komisyon=0

danisman_sayisi=int(input("danisman sayisini giriniz:"))
if danisman_sayisi<=0:
    while danisman_sayisi<=0 :
        danisman_sayisi = int(input("Hatali veri girdiniz, tekrar giriniz:"))

for kisi_sayisi in range(1,danisman_sayisi+1):  #DONGU BURADA BASLAMAKTADIR VE DANISMAN SAYISI KADAR DONMEKTEDİR
    satilan_emlak_adedi = 0
    kiralanan_emlak_adedi = 0
    emlak_adedi=0
    konut_tipi_emlaklarin_satis_bedeli=0
    is_yeri_tipi_emlaklarin_satis_bedeli=0
    arsa_tipi_emlaklarin_satis_bedeli=0
    kiralanan_konutlarin_toplam_kira_bedeli=0
    kiralanan_konut_say=0
    kiralanan_en_yuksek_konut_bedeli=0  #DONGU DONDUKCE HER BIR DANISMANIN VERILERI BU KISIMDA SIFIRLANMAKTADIR
    emlak_komisyonu=0
    kotasini_doldurup_doldurmadigi=0
    ikramiye=1162.35
    alacagi_ucret=0
    asgari_ucret=2324.70
    satis_say=0
    toplam_satis_bedeli=0

    adi_soyadi=input("adinizi ve soyadinizi giriniz:") #HER BIR DANISMANIN ISMI BURADA GIRILMEKTEDIR

    aldigi_maas=float(input("aylik maasinizi giriniz:")) #DANISMANLARIN AYLIK ALDIKLARI MAAS BURADAN GIRILIR
    if aldigi_maas<2324.70:
        while aldigi_maas<2324.70:
            aldigi_maas = float(input("Hatali veri girdiniz, tekrar giriniz:"))

    kota=float(input("kotanizi giriniz:")) #DANISMANLARIN KOTA SEVİYESİ BURADAN GIRILMEKTEDIR
    if kota < aldigi_maas*10:
        while kota < aldigi_maas*10:
            kota = float(input("Hatali girdiniz birdaha giriniz:"))

    cikis="e"
    while cikis=="e" : #BURADA BULUNAN DONGU, ISMI GIRILEN DANISMANIN O AY SATTIGI VEYA KIRALADIGI HER EMLAGI GIRILEN VERİLERE GORE İSLEMDEN GECİRMEKTEDIR
        emlak_tipi=input("emlak tipini giriniz, Konut, İş yeri, Arsa (K/k/İ/i/A/a karakterleri):")#DANISMANIN ISLEM YAPTIGI EMLAK TIPI BURADAN GIRILMEKTEDIR
        if emlak_tipi not in("K","k","İ","i","A","a"):
            while emlak_tipi not in ("K","k","İ","i","A","a"):
                emlak_tipi = input("Hatali girdiniz, tekrar giriniz:")
        toplam_emlak_sayisi+=1

        yapilan_islem_turu=input("yapilan islemi giriniz; Satış, Kiralama (S/s/K/k karakterleri):")#BELIRLENEN EMLAK TIPINE UYGULANAN ISLEM BU KISIMDA GIRILMEKTEDIR
        if yapilan_islem_turu not in ("S","s","K","k"):
            while yapilan_islem_turu not in ("S","s","K","k"):
                yapilan_islem_turu = input("Hatali girdiniz, tekrar giriniz:")
        if yapilan_islem_turu=="s" or yapilan_islem_turu=="S":
            satilan_emlak_adedi+=1
        else:
            kiralanan_emlak_adedi+=1
        emlak_adedi+=1

        satis_veya_kira_bedeli=float(input("satis veya kira bedelini giriniz:")) #YAPILAN ISLEMIN SATIS VEYA KIRALAMA TUTARI BU BOLUMDEN GIRILMEKTEDIR
        if satis_veya_kira_bedeli<0:
            while satis_veya_kira_bedeli<0:
                satis_veya_kira_bedeli = float(input("Hatali girdiniz, tekrar giriniz:"))

        if yapilan_islem_turu=="S" or yapilan_islem_turu=="s":
            emlak_komisyonu+=satis_veya_kira_bedeli*4/100
            satis_say+=1
            toplam_satilan_emlak_sayisi+=1
            if emlak_tipi=="K" or emlak_tipi=="k":
                konut_tipi_emlaklarin_satis_bedeli+=satis_veya_kira_bedeli
            elif emlak_tipi=="İ" or emlak_tipi=="i":
                is_yeri_tipi_emlaklarin_satis_bedeli+=satis_veya_kira_bedeli
            else:
                arsa_tipi_emlaklarin_satis_bedeli+=satis_veya_kira_bedeli
        elif yapilan_islem_turu=="K" or yapilan_islem_turu=="k":
            emlak_komisyonu+=satis_veya_kira_bedeli
            if emlak_tipi=="K" or emlak_tipi=="k":
                kiralanan_konutlarin_toplam_kira_bedeli+=satis_veya_kira_bedeli
                kiralanan_konut_say+=1
            if satis_veya_kira_bedeli>kiralanan_en_yuksek_konut_bedeli and emlak_tipi=="K" or emlak_tipi=="k":
                    kiralanan_en_yuksek_konut_bedeli=satis_veya_kira_bedeli
        if emlak_komisyonu>kota:
            kotasini_doldurup_doldurmadigi="Evet, kotasini doldurmuştur."
            alacagi_ucret= aldigi_maas + emlak_komisyonu/10 + ikramiye
        else :
            kotasini_doldurup_doldurmadigi="Hayır, kotasini doldurmamıştır."
            alacagi_ucret= aldigi_maas + emlak_komisyonu/10

               #BURADAN ITIBAREN YAPILAN ISLEMLER TUM EMLAK DANISMANLARI ICIN GECERLIDIR

        if emlak_tipi=="K" or emlak_tipi=="k":
            toplam_satilan_veya_kiralanan_konut_sayisi+=1
            if yapilan_islem_turu=="S" or yapilan_islem_turu=="s":
                toplam_satilan_konut_sayisi+=1
                satilan_konutlarin_toplam_bedeli+=satis_veya_kira_bedeli
            else:
                toplam_kiralanan_konut_sayisi+=1
        elif emlak_tipi=="İ" or emlak_tipi=="i":
            toplam_satilan_veya_kiralanan_is_yeri_sayisi+=1
            if yapilan_islem_turu=="S" or yapilan_islem_turu=="s":
                toplam_satilan_is_yeri_sayisi+=1
                satilan_is_yerlerinin_toplam_bedeli+=satis_veya_kira_bedeli
            else:
                toplam_kiralanan_is_yer_sayisi+=1
        elif emlak_tipi=="A" or emlak_tipi=="a":
            toplam_satilan_veya_kiralanan_arsa_sayisi+=1
            if yapilan_islem_turu=="S" or yapilan_islem_turu=="s":
                toplam_satilan_arsa_sayisi+=1
                satilan_arsalarin_toplam_bedeli+=satis_veya_kira_bedeli
            else:
                toplam_kiralanan_arsa_sayisi+=1
        if yapilan_islem_turu=="S" or yapilan_islem_turu=="s":
            if satis_veya_kira_bedeli>en_yuksek_bedelle_satilan_emlagin_satis_bedeli:
                en_yuksek_bedelle_satilan_emlagin_satis_bedeli=satis_veya_kira_bedeli
                en_yuksek_bedelle_satilan_emlagin_tipi=emlak_tipi
                en_yuksek_bedelle_satilan_emlagin_danismani=adi_soyadi
        elif yapilan_islem_turu=="K" or yapilan_islem_turu=="k" and emlak_tipi=="k" or emlak_tipi=="k":
            if satis_veya_kira_bedeli>en_yuksek_bedelle_kiralanan_emlagin_kira_bedeli:
                en_yuksek_bedelle_kiralanan_emlagin_kira_bedeli=satis_veya_kira_bedeli
                en_yuksek_bedelle_kiralanan_emlagin_danismani=adi_soyadi
            if satis_veya_kira_bedeli>asgari_ucret:
                kira_bedeli_asgari_ucretten_buyuk_konut_sayisi+=1
        if en_yuksek_bedelle_satilan_emlagin_tipi=="K" or en_yuksek_bedelle_satilan_emlagin_tipi=="k":
            en_yuksek_bedelle_satilan_emlagin_tipi="Konut"
        elif en_yuksek_bedelle_satilan_emlagin_tipi=="İ" or en_yuksek_bedelle_satilan_emlagin_tipi=="i":
            en_yuksek_bedelle_satilan_emlagin_tipi="İs yeri"
        elif en_yuksek_bedelle_satilan_emlagin_tipi=="A" or en_yuksek_bedelle_satilan_emlagin_tipi=="a":
            en_yuksek_bedelle_satilan_emlagin_tipi="Arsa"

        baska_emlak_olup_olmadigi = input("baska emlak var mi, (E/e/H/h karakterleri):") #BU KOMUTA "H" ya da "h" GIRILMESI DAHILINDE, DANISMANIN O AYKI VERILERİ CIKTI OLARAK YAZILMAKTADIR
        if baska_emlak_olup_olmadigi not in ("E", "e", "H", "h"):
            while baska_emlak_olup_olmadigi not in ("E", "e", "H", "h"):
                baska_emlak_olup_olmadigi = input("hatali girdiniz, tekrar giriniz:")
        elif baska_emlak_olup_olmadigi == "H" or baska_emlak_olup_olmadigi == "h":
            cikis = "h"

    toplam_satis_bedeli=konut_tipi_emlaklarin_satis_bedeli+arsa_tipi_emlaklarin_satis_bedeli+is_yeri_tipi_emlaklarin_satis_bedeli
    if satis_say==0:
        hic_satis_yapamayan_danisman_sayisi+=1
    if satis_say > en_cok_satis_yapan_danismanin_satis_sayisi:
        en_cok_satis_yapan_danismanin_satis_sayisi = satis_say
        en_cok_satis_yapan_danismanin_adi=adi_soyadi
        en_cok_satis_yapan_danismanin_sattigi_emlak_sayilari=satilan_emlak_adedi
        en_cok_satis_yapan_danismanin_toplam_satis_bedeli=konut_tipi_emlaklarin_satis_bedeli+is_yeri_tipi_emlaklarin_satis_bedeli+arsa_tipi_emlaklarin_satis_bedeli
    if  toplam_satis_bedeli > toplam_satis_bedeli_en_cok_olan_danismanin_satis_bedeli:
        toplam_satis_bedeli_en_cok_olan_danismanin_satis_bedeli=toplam_satis_bedeli
        toplam_satis_bedeli_en_cok_olan_danismanin_adi=adi_soyadi
        toplam_satis_bedeli_en_cok_olan_danismanin_sattigi_emlak_sayilari=satilan_emlak_adedi
    if emlak_komisyonu>=kota:
        kotasini_dolduran_danisman_sayisi+=1
    if emlak_komisyonu/10>aldigi_maas:
        primi_maasindan_buyuk_olan_danisman_sayisi+=1
    if kiralanan_emlak_adedi>=10 or kiralanan_konutlarin_toplam_kira_bedeli>=25000:
        kiralanan_emlak_adedi_ondan_buyuk_yada_yirmibesbinden_buyuk_olan_danisman_sayisi+=1
    if emlak_komisyonu/10>en_yuksek_prim_alan_danismanin_primi:
        en_yuksek_prim_alan_danismanin_primi=emlak_komisyonu/10
        en_yuksek_prim_alan_danismanin_adi=adi_soyadi
        en_yuksek_prim_alan_danismanin_maasi=aldigi_maas
        if emlak_komisyonu>=kota:
            en_yuksek_prim_alan_danismanin_toplam_ucreti=aldigi_maas+en_yuksek_prim_alan_danismanin_primi+ikramiye
        else:
            en_yuksek_prim_alan_danismanin_toplam_ucreti=aldigi_maas+en_yuksek_prim_alan_danismanin_primi
    if emlak_komisyonu/10<en_dusuk_prim_alan_danismanin_primi:
        en_dusuk_prim_alan_danismanin_primi=emlak_komisyonu/10
        en_dusuk_prim_alan_danismanin_adi=adi_soyadi
        en_dusuk_prim_alan_danismanin_maasi=aldigi_maas
        if emlak_komisyonu>=kota:
            en_dusuk_prim_alan_danismanin_toplam_ucreti=aldigi_maas+en_dusuk_prim_alan_danismanin_primi+ikramiye
        else:
            en_dusuk_prim_alan_danismanin_toplam_ucreti=aldigi_maas+en_dusuk_prim_alan_danismanin_primi
    emlak_danismanlarina_odenecek_toplam_ucret += alacagi_ucret
    acentenin_kazandigi_toplam_komisyon+=emlak_komisyonu

    #BU SATIRDA BULUNAN PRINT'LER ADİ GIRILEN DANISMANIN O AYKI PERFORMANSLARININ SIRALANDIGI CIKTI KISMIDIR
    print("Adi ve soyadi:", adi_soyadi)
    print("satilan emlak adedi:",format(satilan_emlak_adedi,'.2f'), "kiralanan emlak adedi:",format(kiralanan_emlak_adedi,'.2f'), "satilan emlaklarin orani","%",format(satilan_emlak_adedi*100/emlak_adedi,".2f"),"kiralanan emlaklarin orani:","%",format(kiralanan_emlak_adedi*100/emlak_adedi,".2f"))
    print("Konut tipi emlakarin toplam satis bedeli:",format(konut_tipi_emlaklarin_satis_bedeli,",.2f"),'TL',"İs yeri tipi emlaklarin toplam satis bedeli:",format(is_yeri_tipi_emlaklarin_satis_bedeli,",.2f"),'TL',"Arsa tipi emlaklarin toplam satis bedeli:",format(arsa_tipi_emlaklarin_satis_bedeli,',.2f'),'TL')
    print("Kiralanan konutlarin ortalama kira bedeli:",format(kiralanan_konutlarin_toplam_kira_bedeli/kiralanan_konut_say,'.2f'),'TL')
    print("En yuksek bedelle kiralanan konutun kira bedeli:",format(kiralanan_en_yuksek_konut_bedeli,',.2f'),'TL')
    print("O ayki aldigi maas:",format(aldigi_maas,',.2f'),'TL')
    print("O ayki aldigi prim:",format(emlak_komisyonu/10,',.2f'),'TL')
    print("O ayki Kotasi:",format(kota,'.2f'),'TL')
    print("acenteye kazandirdigi toplam komisyon tutari:",format(emlak_komisyonu,',.2f'),'TL')
    print("O ay kotasini doldurup doldurmadigi:",kotasini_doldurup_doldurmadigi)
    print("O ay kotasini doldurduysa alacagi ikramiye:",format(ikramiye,',.2f'),'TL')
    print("O ayki toplam ucret:",format(alacagi_ucret,',.2f'),'TL')

#BU SATIRDA BULUNAN PRINT'LER ISE TUM KULLANICILARIN VERILERININ CIKTI OLARAK YAZDIRILDIGI KISIMDIR
print("Konut tipi emlaklarin toplam satilma sayisi:",format(toplam_satilan_konut_sayisi,'.2f'),"İs yeri tipi emlaklarin toplam satilma sayisi:",format(toplam_satilan_is_yeri_sayisi,'.2f'),"Arsa tipi emlaklarin toplam satilma sayisi:",format(toplam_satilan_arsa_sayisi,'.2f'))
print("Konut tipi emlaklarin toplam kiralanma sayisi:",format(toplam_kiralanan_konut_sayisi,'.2f'),"İs yeri tipi emlaklarin toplam kiralanma sayisi:",format(toplam_kiralanan_is_yer_sayisi,'.2f'),"Arsa tipi emlaklarin toplam kiralanma sayisi:",format(toplam_kiralanan_arsa_sayisi,'.2f'))
print("Konut tipi emlaklarin satilma orani:","%",format(toplam_satilan_konut_sayisi*100/toplam_satilan_veya_kiralanan_konut_sayisi,'.2f'),"İs yeri tipi emlaklarin satilma orani:","%",format(toplam_satilan_is_yeri_sayisi*100/toplam_satilan_veya_kiralanan_is_yeri_sayisi,'.2f'),"Arsa tipi emlaklarin satilma orani:",'%',format(toplam_satilan_arsa_sayisi*100/toplam_satilan_veya_kiralanan_arsa_sayisi,'.2f'))
print("Konut tipi emlaklarin toplam satis bedeli:",format(satilan_konutlarin_toplam_bedeli,',.2f'),'TL',"İs yeri tipi emlaklarin toplam satis bedeli",format(satilan_is_yerlerinin_toplam_bedeli,',.2f'),'TL',"Arsa tipi emlaklarin toplam satis bedeli:",format(satilan_arsalarin_toplam_bedeli,',.2f'),'TL')
print("Konut tipi emlaklarin ortalama satis bedeli:",format(satilan_konutlarin_toplam_bedeli/toplam_satilan_konut_sayisi,',.2f'),'TL',"İs yeri tipi emlaklarin ortalama satis bedeli:",format(satilan_is_yerlerinin_toplam_bedeli/toplam_satilan_is_yeri_sayisi,',.2f'),'TL',"Arsa tipi emlaklarin ortalama satis bedeli:",format(satilan_arsalarin_toplam_bedeli/toplam_satilan_arsa_sayisi,',.2f'),'TL')
print("En yuksek bedelle satilan emlağin tipi:",en_yuksek_bedelle_satilan_emlagin_tipi,"En yuksek Bedelle satilan emlagin satis bedeli:",format(en_yuksek_bedelle_satilan_emlagin_satis_bedeli,',.2f'),'TL',"Satis yapan danismanin adi:",en_yuksek_bedelle_satilan_emlagin_danismani)
print("En yuksek bedelle kiralanan konutun kira bedeli:",format(en_yuksek_bedelle_kiralanan_emlagin_kira_bedeli,',.2f'),'TL',"Kiralayan danismanin adi soyadi:",en_yuksek_bedelle_kiralanan_emlagin_danismani)
print("Kira bedeli aylik asgari ucretten buyuk olan konut sayisi:",format(kira_bedeli_asgari_ucretten_buyuk_konut_sayisi,'.2f'),"Kiralanan konutlar icindeki orani:",'%',format(kira_bedeli_asgari_ucretten_buyuk_konut_sayisi*100/toplam_kiralanan_konut_sayisi,'.2f'))
print("Hiç satis yapmayan danismanlarin sayisi:",format(hic_satis_yapamayan_danisman_sayisi,'.2f'),"Hic satis yapmayan danisman sayisi orani:",'%',format(hic_satis_yapamayan_danisman_sayisi*100/danisman_sayisi,'.2f'))
print("Satis adedi olarak en cok satis yapan danismanin adi:",en_cok_satis_yapan_danismanin_adi,"Sattigi emlak sayisi:",format(en_cok_satis_yapan_danismanin_sattigi_emlak_sayilari,'.2f'),"Toplam satis bedeli:",format(en_cok_satis_yapan_danismanin_toplam_satis_bedeli,',.2f'),'TL')
print("Satis bedeli olarak en cok satis yapan danismanin adi:",toplam_satis_bedeli_en_cok_olan_danismanin_adi,"Sattigi emlak sayilari:",format(toplam_satis_bedeli_en_cok_olan_danismanin_sattigi_emlak_sayilari,'.2f'),"Toplam satis bedeli:",format(toplam_satis_bedeli_en_cok_olan_danismanin_satis_bedeli,',.2f'),'TL')
print("Kotasini dolduran danisman sayisi:",format(kotasini_dolduran_danisman_sayisi,'.2f'),"Kotasini dolduran danisman sayisinin tum danismanlar icerisindeki orani:",'%',format((kotasini_dolduran_danisman_sayisi*100)/danisman_sayisi,'.2f'))
print("Primi maasindan buyuk olan danisman sayisi:",format(primi_maasindan_buyuk_olan_danisman_sayisi,'.2f'),"Primi maasindan buyuk olan danisman sayisinin tum danismanlar icerisindeki orani:",'%',format((primi_maasindan_buyuk_olan_danisman_sayisi*100)/danisman_sayisi,'.2f'))
print("10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:",format(kiralanan_emlak_adedi_ondan_buyuk_yada_yirmibesbinden_buyuk_olan_danisman_sayisi,'.2f'))
print("En yuksek prim alan danismanin adi:",en_yuksek_prim_alan_danismanin_adi,"Aldigi maasi:",format(en_yuksek_prim_alan_danismanin_maasi,',.2f'),'TL',"Aldigi primi:",format(en_yuksek_prim_alan_danismanin_primi,'.2f'),'TL',"Aldigi toplam ucreti:",format(en_yuksek_prim_alan_danismanin_toplam_ucreti,',.2f'),'TL')
print("En dusuk prim alan danismanin adi:",en_dusuk_prim_alan_danismanin_adi,"Aldigi maasi:",format(en_dusuk_prim_alan_danismanin_maasi,',.2f'),'TL',"Aldigi primi:",format(en_dusuk_prim_alan_danismanin_primi,',.2f'),'TL',"Aldigi toplam ucreti:",format(en_dusuk_prim_alan_danismanin_toplam_ucreti,',.2f'),'TL')
print("O ay tum emlak danismanlarina odenecek toplam ucretlerin toplami:",format(emlak_danismanlarina_odenecek_toplam_ucret,',.2f'),'TL',"Ve ortalamasi:",format(emlak_danismanlarina_odenecek_toplam_ucret/danisman_sayisi,',.2f'),'TL')
print("Emlak acentesinin kazandigi toplam komisyon:",format(acentenin_kazandigi_toplam_komisyon,',.2f'),'TL')


















