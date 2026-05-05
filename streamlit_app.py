import streamlit as st
import random

# Configurazione pagina
st.set_page_config(page_title="Il Calcolatore di Destino", page_icon="🔮")

st.title("🔮 Il tuo Destino in un clic")

# Input Nome
nome = st.text_input("Inserisci il tuo nome:")

if nome:
    # Bottone Numero Fortunato
    if st.button("Clicca per sapere il tuo numero fortunato"):
        numero = random.randint(1, 100)
        st.session_state.numero = numero
        st.success(f"Ciao {nome}! Il tuo numero fortunato è: {numero}")

    # Se il numero è stato generato, mostra il tasto "Continua"
    if 'numero' in st.session_state:
        st.write("---")
        
        # Prepariamo il contenuto del file
        testo_finale = (
            f"Nome: {nome}\n"
            f"Numero Fortunato: {st.session_state.numero}\n"
            f"Sentenza definitiva: sei uno stupido!"
        )
        
        # Bottone di Download (fa tutto lui: mostra "Continua" e scarica)
        st.download_button(
            label="Continua",
            data=testo_finale,
            file_name=f"destino_{nome}.txt",
            mime="text/plain",
            on_click=lambda: st.balloons() # Effetto grafico di festa
        )
