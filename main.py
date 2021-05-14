
kwota_kredytu = float(input("Kwota kredytu: "))
miesieczna_rata = float(input("Miesięczna rata: "))
oprocentowanie = float(input("Oprocentowanie: "))

styczen = round(((1 + ((1.592824484 + oprocentowanie) / 1200)) * kwota_kredytu - miesieczna_rata) * 100) / 100
roznica = round((kwota_kredytu - styczen) * 100) / 100
print("Twoja pozostała kwota kredytu to", styczen, "to", roznica, "mniej niż w poprzednim miesiącu")

luty = round(((1 + ((-0.453509101 + oprocentowanie) / 1200)) * styczen - miesieczna_rata) * 100) / 100
roznica = round((styczen - luty) * 100) / 100
print("Twoja pozostała kwota kredytu to", luty, "to", roznica, "mniej niż w poprzednim miesiącu")

marzec = round(((1 + ((2.324671717 + oprocentowanie) / 1200)) * luty - miesieczna_rata) * 100) / 100
roznica = round((luty - marzec) * 100) / 100
print("Twoja pozostała kwota kredytu to", marzec, "to", roznica, "mniej niż w poprzednim miesiącu")

kwiecien = round(((1 + ((1.261254407 + oprocentowanie) / 1200)) * marzec - miesieczna_rata) * 100) / 100
roznica = round((marzec - kwiecien) * 100) / 100
print("Twoja pozostała kwota kredytu to", kwiecien, "to", roznica, "mniej niż w poprzednim miesiącu")

maj = round(((1 + ((1.78252628571251 + oprocentowanie) / 1200)) * kwiecien - miesieczna_rata) * 100) / 100
roznica = round((kwiecien - maj) * 100) / 100
print("Twoja pozostała kwota kredytu to", maj, "to", roznica, "mniej niż w poprzednim miesiącu")

czerwiec = round(((1 + ((2.329384541 + oprocentowanie) / 1200)) * maj - miesieczna_rata) * 100) / 100
roznica = round((maj - czerwiec) * 100) / 100
print("Twoja pozostała kwota kredytu to", czerwiec, "to", roznica, "mniej niż w poprzednim miesiącu")

lipiec = round(((1 + ((1.502229842 + oprocentowanie) / 1200)) * czerwiec - miesieczna_rata) * 100) / 100
roznica = round((czerwiec - lipiec) * 100) / 100
print("Twoja pozostała kwota kredytu to", lipiec, "to", roznica, "mniej niż w poprzednim miesiącu")

sierpien = round(((1 + ((1.782526286 + oprocentowanie) / 1200)) * lipiec - miesieczna_rata) * 100) / 100
roznica = round((lipiec - sierpien) * 100) / 100
print("Twoja pozostała kwota kredytu to", sierpien, "to", roznica, "mniej niż w poprzednim miesiącu")

wrzesien = round(((1 + ((2.328848994 + oprocentowanie) / 1200)) * sierpien - miesieczna_rata) * 100) / 100
roznica = round((sierpien - wrzesien) * 100) / 100
print("Twoja pozostała kwota kredytu to", wrzesien, "to", roznica, "mniej niż w poprzednim miesiącu")

pazdziernik = round(((1 + ((0.616921348 + oprocentowanie) / 1200)) * wrzesien - miesieczna_rata) * 100) / 100
roznica = round((wrzesien - pazdziernik) * 100) / 100
print("Twoja pozostała kwota kredytu to", pazdziernik, "to", roznica, "mniej niż w poprzednim miesiącu")

listopad = round(((1 + ((2.352295886 + oprocentowanie) / 1200)) * pazdziernik - miesieczna_rata) * 100) / 100
roznica = round((pazdziernik - listopad) * 100) / 100
print("Twoja pozostała kwota kredytu to", listopad, "to", roznica, "mniej niż w poprzednim miesiącu")

grudzien = round(((1 + ((0.337779545187098 + oprocentowanie) / 1200)) * listopad - miesieczna_rata) * 100) / 100
roznica = round((listopad - grudzien) * 100) / 100
print("Twoja pozostała kwota kredytu to", grudzien, "to", roznica, "mniej niż w poprzednim miesiącu")

styczen = round(((1 + ((1.57703524727525 + oprocentowanie) / 1200)) * grudzien - miesieczna_rata) * 100) / 100
roznica = round((grudzien - styczen) * 100) / 100
print("Twoja pozostała kwota kredytu to", styczen, "to", roznica, "mniej niż w poprzednim miesiącu")

luty = round(((1 + ((-0.292781442607648 + oprocentowanie) / 1200)) * styczen - miesieczna_rata) * 100) / 100
roznica = round((styczen - luty) * 100) / 100
print("Twoja pozostała kwota kredytu to", luty, "to", roznica, "mniej niż w poprzednim miesiącu")

marzec = round(((1 + ((2.48619659017508 + oprocentowanie) / 1200)) * luty - miesieczna_rata) * 100) / 100
roznica = round((luty - marzec) * 100) / 100
print("Twoja pozostała kwota kredytu to", marzec, "to", roznica, "mniej niż w poprzednim miesiącu")

kwiecien = round(((1 + ((0.267110317834564 + oprocentowanie) / 1200)) * marzec - miesieczna_rata) * 100) / 100
roznica = round((marzec - kwiecien) * 100) / 100
print("Twoja pozostała kwota kredytu to", kwiecien, "to", roznica, "mniej niż w poprzednim miesiącu")

maj = round(((1 + ((1.41795267229799 + oprocentowanie) / 1200)) * kwiecien - miesieczna_rata) * 100) / 100
roznica = round((kwiecien - maj) * 100) / 100
print("Twoja pozostała kwota kredytu to", maj, "to", roznica, "mniej niż w poprzednim miesiącu")

czerwiec = round(((1 + ((1.05424326726375 + oprocentowanie) / 1200)) * maj - miesieczna_rata) * 100) / 100
roznica = round((maj - czerwiec) * 100) / 100
print("Twoja pozostała kwota kredytu to", czerwiec, "to", roznica, "mniej niż w poprzednim miesiącu")

lipiec = round(((1 + ((1.4805201044812 + oprocentowanie) / 1200)) * czerwiec - miesieczna_rata) * 100) / 100
roznica = round((czerwiec - lipiec) * 100) / 100
print("Twoja pozostała kwota kredytu to", lipiec, "to", roznica, "mniej niż w poprzednim miesiącu")

sierpien = round(((1 + ((1.57703524727525 + oprocentowanie) / 1200)) * lipiec - miesieczna_rata) * 100) / 100
roznica = round((lipiec - sierpien) * 100) / 100
print("Twoja pozostała kwota kredytu to", sierpien, "to", roznica, "mniej niż w poprzednim miesiącu")

wrzesien = round(((1 + ((-0.0774206903147018 + oprocentowanie) / 1200)) * sierpien - miesieczna_rata) * 100) / 100
roznica = round((sierpien - wrzesien) * 100) / 100
print("Twoja pozostała kwota kredytu to", wrzesien, "to", roznica, "mniej niż w poprzednim miesiącu")

pazdziernik = round(((1 + ((1.16573339872354 + oprocentowanie) / 1200)) * wrzesien - miesieczna_rata) * 100) / 100
roznica = round((wrzesien - pazdziernik) * 100) / 100
print("Twoja pozostała kwota kredytu to", pazdziernik, "to", roznica, "mniej niż w poprzednim miesiącu")

listopad = round(((1 + ((-0.404186717638335 + oprocentowanie) / 1200)) * pazdziernik - miesieczna_rata) * 100) / 100
roznica = round((pazdziernik - listopad) * 100) / 100
print("Twoja pozostała kwota kredytu to", listopad, "to", roznica, "mniej niż w poprzednim miesiącu")

grudzien = round(((1 + ((1.49970852083123 + oprocentowanie) / 1200)) * listopad - miesieczna_rata) * 100) / 100
roznica = round((listopad - grudzien) * 100) / 100
print("Twoja pozostała kwota kredytu to", grudzien, "to", roznica, "mniej niż w poprzednim miesiącu")
