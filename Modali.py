#                                                       LE MODALI

#Per produrre le nostre finestre modali abbiamo a disposizione fondamentalmente due classi:

#la classe w3-modal, che permette di produrre il contenitore del modale, ovvero il cosiddetto "overlay" che consente di separare il contenuto della finestra creata dal resto della pagina, posizionandola al di sopra di quest'ultima
#la classe w3-modal-content, che contrariamente permette di produrre il contenuto del modale

#CREAZIONE BOTTONE
#<button onclick="document.getElementById('box').style.display='block'"
#class="w3-button">Apri finestra modale</button>



#                                           PERSONALIZZAZIONE CONTENUTO


# div id="box" class="w3-modal">
# <div class="w3-modal-content">
# <header class="w3-container w3-red">
# <span onclick="document.getElementById('box').style.display='none'"
# class="w3-button w3-display-topright">&times;</span>
# <h2>La mia finestra modale</h2>
# </header>
# <div class="w3-container">
# <p>Contenuto testuale</p>
# <p>Contenuto testuale</p>
# </div>
# <footer class="w3-container w3-red">
# <p>Copyright 2019</p>
# </footer>
# </div>
# </div>



#UTILIZZO DI IMMAGGINI COME MODALI
# <img src="miaimmagine.jpg" style="cursor:zoom-in"
# # onclick="document.getElementById('box').style.display='block'">
# # <div id="box" class="w3-modal" onclick="this.style.display='none'">
# # <span class="w3-button w3-hover-red w3-xlarge w3-display-topright">&times;</span>
# # <div class="w3-modal-content">
# # <img src="miaimmagine.jpg" style="width:100%">
# # </div>
# # </div>

