from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMessageBox, QDialog, QInputDialog, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os

app = QApplication([])
root = loadUi('main.ui')

def obtenir_mot_de_passe():
    mot_de_passe, ok_appuye = "", False

    dialog = QDialog()
    dialog.setWindowTitle('Entre une clé de décryptage')
    dialog_layout = QVBoxLayout()
    dialog.setGeometry(400, 400, 300, 100)

    champ_mot_de_passe = QLineEdit()
    bouton_afficher_masquer = QPushButton()
    bouton_afficher_masquer.setIcon(QIcon(os.path.join("image", f"eye_icon.png")))
    bouton_afficher_masquer.setCheckable(True)

    def basculer_visibilite_mot_de_passe():
        if bouton_afficher_masquer.isChecked():
            champ_mot_de_passe.setEchoMode(QLineEdit.Normal)
            bouton_afficher_masquer.setIcon(QIcon(os.path.join("image", f"eye_closed.png")))
        else:
            champ_mot_de_passe.setEchoMode(QLineEdit.Password)
            bouton_afficher_masquer.setIcon(QIcon(os.path.join("image", f"eye_icon.png")))

    bouton_afficher_masquer.clicked.connect(basculer_visibilite_mot_de_passe)
    champ_mot_de_passe.setEchoMode(QLineEdit.Password)
    layout_champ_saisie = QHBoxLayout()
    layout_champ_saisie.addWidget(champ_mot_de_passe)
    layout_champ_saisie.addWidget(bouton_afficher_masquer)

    dialog_layout.addLayout(layout_champ_saisie)

    bouton_ok = QPushButton('OK')
    bouton_annuler = QPushButton('Annuler')

    def accepter():
        nonlocal ok_appuye, mot_de_passe
        mot_de_passe = champ_mot_de_passe.text()
        ok_appuye = bool(mot_de_passe)
        dialog.accept()

    def refuser():
        nonlocal ok_appuye, mot_de_passe
        ok_appuye = False
        dialog.reject()

    bouton_ok.clicked.connect(accepter)
    bouton_annuler.clicked.connect(refuser)

    dialog_layout.addWidget(bouton_ok)
    dialog_layout.addWidget(bouton_annuler)

    dialog.setLayout(dialog_layout)

    while not ok_appuye or len(mot_de_passe) < 1:
        ret = dialog.exec_()

        if ret == QDialog.Rejected:
            root.close()
            return None

        ok_appuye = bool(mot_de_passe)

        if not ok_appuye:
            ret = QMessageBox.warning(None, 'Avertissement', 'Mot de passe invalide. Veuillez entrer un mot de passe valide.', QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                root.close()
                return None

    return mot_de_passe

cle_de_decryptage = obtenir_mot_de_passe()

def verifier_radio_clic():
    root.verification.setText('')
    root.cdeca.setText('')
    root.cle_2.setText('')
    if root.dec.isChecked():
        if root.cesar.isChecked() or root.vigenere.isChecked():
            root.deca.setText("Décalage")
            root.cle_decryptage_2.hide()
            root.cle_decryptage.show()
            icon_path = os.path.join("image", "eye_icon.png")
            root.cle_2.setEchoMode(QLineEdit.Password)
            root.cdeca.setEchoMode(QLineEdit.Normal)
            icon = QIcon(icon_path)
            root.cle_decryptage.setIcon(icon)
            if root.cesar.isChecked():
                root.cdeca.setPlaceholderText('Veuillez entrer le décalage pour le Code de César')
                root.cle_2.setPlaceholderText('Veuillez insérer votre clé de décryptage ')
            else:
                root.cdeca.setPlaceholderText('Veuillez entrer le décalage pour le Code de Vigenère')
                root.cle_2.setPlaceholderText('Veuillez insérer votre clé de décryptage ')
            root.cdeca.show()
            root.deca.show()
            root.cle_2.show()
            root.cle.show()
        elif root.ROT.isChecked() or root.carre.isChecked():

            root.cdeca.setEchoMode(QLineEdit.Password)
            if root.ROT.isChecked():
                root.cdeca.setPlaceholderText('Veuillez insérer votre clé de décryptage ')
            else:
                root.cdeca.setPlaceholderText('Veuillez insérer votre clé de décryptage ')
            root.deca.setText("Clé de Décryptage")
            root.cdeca.show()
            root.cle_decryptage_2.show()
            root.cle_decryptage.hide()
            icon_path = os.path.join("image", "eye_icon.png")
            icon = QIcon(icon_path)
            root.cle_decryptage_2.setIcon(icon)
            root.deca.show()
            root.cle_2.hide()
            root.cle.hide()
    elif root.cry.isChecked():
        root.cdeca.setEchoMode(QLineEdit.Normal)
        root.cle_decryptage.hide()
        root.cle_decryptage_2.hide()
        if root.cesar.isChecked() or root.vigenere.isChecked():
            if root.cesar.isChecked():
                root.cdeca.setPlaceholderText('Veuillez entrer le décalage pour le Code de César')
            else:
                root.cdeca.setPlaceholderText('Veuillez entrer le décalage pour le Code de Vigenère')
            
            root.deca.setText("Décalage")
            root.cdeca.show()
            root.deca.show()
            root.cle_2.hide()
            root.cle.hide()
        else:
            root.cdeca.setPlaceholderText('')
            root.cdeca.hide()
            root.deca.hide()
            root.cle_2.hide()
            root.cle.hide()

def verifier_decalage():
    if root.cesar.isChecked():
        if not(root.cdeca.text().isdecimal()) and root.cdeca.text() != "":
            root.verification.setText('le décalage doit être un nombre entier')
            root.verification.setStyleSheet('color:red')
        else:
            root.verification.setText('')
    elif root.vigenere.isChecked():
        if not(root.cdeca.text().isalnum()) and root.cdeca.text() != "":
            root.verification.setText('le décalage doit être une chaîne de caractères  ,en évitant les symboles')
            root.verification.setStyleSheet('color:red')
        else:
            root.verification.setText('')

def effacer():
    ret = QMessageBox.question(root, 'confirmation', "Êtes-vous sûr de tout effacer ?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
    if ret == QMessageBox.Yes:
        root.test.setChecked(True)
        root.test1.setChecked(True)
        root.resultat.setText('Résultat')
        root.message.setText('')
        root.cdeca.hide()
        root.deca.hide()
        root.cle_2.hide()
        root.cle.hide()
        root.cle_decryptage.hide()
        root.cle_decryptage_2.hide()

def est_entier(texte):
    try:
        dechiffrer_polybe(texte)
    except:
        return False
    return True

def crypter_decrypter():
    ch = "Veuillez régler ces problèmes:"
    if root.test1.isChecked():
        ch += "\n-Veuillez entrer un texte à crypter/décrypter.\n-Veuillez choisir une action."

    if  root.cry.isChecked():
        if root.message.text() == "":
            ch += "\n-Veuillez entrer un texte à crypter."
        if not(root.cdeca.text().isdecimal()) and root.cesar.isChecked():
            ch += "\n-Veuillez entrer un décalage doit être un nombre entier."
        if not(root.cdeca.text().isalnum()) and root.vigenere.isChecked():
            ch += "\n-Veuillez entrer un décalage doit être une chaîne de caractères  ,en évitant les symboles."

    if root.dec.isChecked():
        if root.message.text() == "":
            ch += "\n-Veuillez entrer un texte à decrypter."
        if root.ROT.isChecked() and root.cdeca.text() != cle_de_decryptage:
            ch += "\n-Veuillez entrer une clé de décryptage valide."
        elif root.carre.isChecked():
            if root.cdeca.text() != cle_de_decryptage:
                ch += "\n-Veuillez entrer une clé de décryptage valide."
            elif not(est_entier(root.message.text())):
                ch += "\n-Veuillez entrer un valide message pour décrypter."

        elif root.cesar.isChecked():
            if not(root.cdeca.text().isdecimal()):
                ch += "\n-Veuillez entrer un décalage doit être un nombre entier."
            if root.cle_2.text() != cle_de_decryptage:
                ch += "\n-Veuillez entrer une clé de décryptage valide."
        elif root.vigenere.isChecked():
            if not(root.cdeca.text().isalnum()):
                ch += "\n-Veuillez entrer un décalage doit être une chaîne de caractères  ,en évitant les symboles."
            if root.cle_2.text() != cle_de_decryptage:
                ch += "\n-Veuillez entrer une clé de décryptage valide."

    if root.test.isChecked():
        ch += "\n-Veuillez choisir une méthode."

    if ch != "Veuillez régler ces problèmes:":
        ret = QMessageBox.question(root, 'Erreur', f"{ch}", QMessageBox.Ok)
    else:
        if root.cry.isChecked():
            if root.ROT.isChecked():
                root.resultat.setText(chiffrer_rot13(root.message.text()))
            elif root.cesar.isChecked():
                root.resultat.setText(chiffrer_cesar(root.message.text(),int(root.cdeca.text())))
            elif root.vigenere.isChecked():
                root.resultat.setText(chiffrer_vigenere(root.message.text(),root.cdeca.text()))
            elif root.carre.isChecked():
                root.resultat.setText(chiffrer_polybe(root.message.text()))

        if root.dec.isChecked():
            if root.ROT.isChecked():
                root.resultat.setText(dechiffrer_rot13(root.message.text()))
            elif root.cesar.isChecked():
                root.resultat.setText(dechiffrer_cesar(root.message.text(),int(root.cdeca.text())))
            elif root.vigenere.isChecked():
                root.resultat.setText(dechiffrer_vigenere(root.message.text(),root.cdeca.text()))
            elif root.carre.isChecked():
                root.resultat.setText(dechiffrer_polybe(root.message.text()))

def chiffrer_rot13(message):
    message_chiffre = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                message_chiffre += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                message_chiffre += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            message_chiffre += char
    return message_chiffre

def chiffrer_cesar(message, decalage):
    message_chiffre = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                message_chiffre += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
            else:
                message_chiffre += chr((ord(char) - ord('A') + decalage) % 26 + ord('A'))
        else:
            message_chiffre += char
    return message_chiffre

def chiffrer_vigenere(message, cle):
    message_chiffre = ""
    longueur_cle = len(cle)
    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                message_chiffre += chr((ord(char) - ord('a') + ord(cle[i % longueur_cle]) - ord('a')) % 26 + ord('a'))
            else:
                message_chiffre += chr((ord(char) - ord('A') + ord(cle[i % longueur_cle]) - ord('A')) % 26 + ord('A'))
        else:
            message_chiffre += char
    return message_chiffre

def chiffrer_polybe(message):
    carre_polybe = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
                    'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24',
                    'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34',
                    'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44',
                    'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'}

    message_chiffre = ""
    for char in message:
        if char.isalpha():
            char = char.upper()
            message_chiffre += carre_polybe[char] + ' '
        else:
            message_chiffre += char
    return message_chiffre.strip()

def dechiffrer_rot13(message):
    return chiffrer_rot13(message)

def dechiffrer_cesar(message, decalage):
    return chiffrer_cesar(message, -decalage)

def dechiffrer_vigenere(message, cle):
    message_dechiffre = ""
    longueur_cle = len(cle)
    for i, char in enumerate(message):
        if char.isalpha():
            if char.islower():
                message_dechiffre += chr((ord(char) - ord(cle[i % longueur_cle]) + 26) % 26 + ord('a'))
            else:
                message_dechiffre += chr((ord(char) - ord(cle[i % longueur_cle]) + 26) % 26 + ord('A'))
        else:
            message_dechiffre += char
    return message_dechiffre

def dechiffrer_polybe(message):
    carre_polybe = {'11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E',
                    '21': 'F', '22': 'G', '23': 'H', '24': 'I', '25': 'K',
                    '31': 'L', '32': 'M', '33': 'N', '34': 'O', '35': 'P',
                    '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U',
                    '51': 'V', '52': 'W', '53': 'X', '54': 'Y', '55': 'Z'}

    message = message.split()
    message_dechiffre = ""
    for item in message:
        message_dechiffre += carre_polybe[item]

    return message_dechiffre

def mode_de_passe_2():
    mode_actuel = root.cdeca.echoMode()

    if mode_actuel == QLineEdit.Password:
        nouveau_mode = QLineEdit.Normal
        chemin_icone = os.path.join("image", "eye_closed.png")
        icone = QIcon(chemin_icone)
        root.cle_decryptage_2.setIcon(icone)
    else:
        nouveau_mode = QLineEdit.Password
        chemin_icone = os.path.join("image", "eye_icon.png")
        icone = QIcon(chemin_icone)
        root.cle_decryptage_2.setIcon(icone)
    root.cdeca.setEchoMode(nouveau_mode)

def mode_de_passe():
    mode_actuel = root.cle_2.echoMode()

    if mode_actuel == QLineEdit.Password:
        nouveau_mode = QLineEdit.Normal
        chemin_icone = os.path.join("image", "eye_closed.png")
        icone = QIcon(chemin_icone)
        root.cle_decryptage.setIcon(icone)
    else:
        nouveau_mode = QLineEdit.Password
        chemin_icone = os.path.join("image", "eye_icon.png")
        icone = QIcon(chemin_icone)
        root.cle_decryptage.setIcon(icone)
    root.cle_2.setEchoMode(nouveau_mode)

root.test.hide()
root.test1.hide()
root.cdeca.hide()
root.cle_decryptage.hide()
root.cle_decryptage_2.hide()
root.deca.hide()
root.cle_2.hide()
root.cle.hide()

root.delet.clicked.connect(effacer)
root.cry.toggled.connect(verifier_radio_clic)
root.dec.toggled.connect(verifier_radio_clic)
root.cesar.toggled.connect(verifier_radio_clic)
root.vigenere.toggled.connect(verifier_radio_clic)
root.ROT.toggled.connect(verifier_radio_clic)
root.carre.toggled.connect(verifier_radio_clic)
root.cdeca.textChanged.connect(verifier_decalage)
root.confirmer.clicked.connect(crypter_decrypter)
root.cle_decryptage_2.clicked.connect(mode_de_passe_2)
root.cle_decryptage.clicked.connect(mode_de_passe)

if cle_de_decryptage is not None:
    root.show()
    app.exec_()

