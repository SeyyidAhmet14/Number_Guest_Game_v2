import streamlit as st
import random


#50 ilaa 1 arasinda bir sayi tahmin oyunu
#5 hakkimiz olucaktir
#3 ve 6 sayilari ozel bir tekerleme gelsin(3de arkadaslar arasinda bi soz olacak)
#6 kere 6 36 amcamin inegi otladi
#3kere3=27aksiniiddaedendilimizikullanamaz✌
#baslik atilacak

st.title("NUMBER GUEST GAME V2")
st.write("The correct number is between 1 and 50. Let's see if you can find it. And there are 2 special numbers 😉")
#oturum ayarlari(Oyundaki gerekli olan kavramlar)

if "correct_number" not in st.session_state:
    st.session_state.correct_number=random.randint(1,50)
    st.session_state.benefit=5
    st.session_state.message=""

#kullanicidan tahmin alma

guest = st.number_input("Say the number in your mind",min_value=1.0,max_value=50.0,step=1.0)

#sessional state'e bir butonla gondericek
#kullanici yonlendirilmesi(yukari,asagi vb.)

if st.button(f"{guest}.This is your guest! But are you sure?"):
    if st.session_state.benefit > 0:
        #once dogru bilip bilmedigini kontrol et
        if guest == st.session_state.correct_number:
            st.session_state.message="You guessed correctly! Bravo my düd ✔!"
            st.snow()
        #dogru degilse surprise sayi kontrolu yapalim
        elif guest == 3:
            st.session_state.benefit-=1
            st.session_state.message="3 times 3 = 27. Anyone who claims otherwise cannot use our language ✌"
        elif guest == 6:
            st.session_state.benefit-=1
            st.session_state.message="6 times 6 36,my uncle's cow grazed"
        #Diger yanlis tahminler icin yonlendirme
        elif guest > st.session_state.correct_number:
            st.session_state.benefit-=1
            st.session_state.message=f"Fatih Terim was surprised, the user got it wrong 😨düd try a smaller number.Remaining Benefit:{st.session_state.benefit}"
        else:
            st.session_state.benefit-=1
            st.session_state.message=f"Fatih Terim was surprised, the user got it wrong 😨düd try a bigger number.Remaining Benefit:{st.session_state.benefit}"
#Hak bittigi ve dogru sayiyi bilemedi yasanacaklar
    elif st.session_state.benefit == 0 and guest != st.session_state.correct_number:
        st.session_state.message=f"İlber Ortaylı has never encountered such an ignorant person 😭😭😭 btw, the correct number is {st.session_state.correct_number}"
st.write(st.session_state.message)

#oyunu yeniden baslatmak icin bir buton ve basilinca balloonlar ciksin,hersey restart olsun)
if st.button("Restart?"):
    st.balloons()
    st.session_state.correct_number=random.randint(1,50)
    st.session_state.benefit=5
    st.session_state.message="I choosed a new number.Lets goooo!😉"
    st.rerun()
#And hello to the person reading the code... 👀
