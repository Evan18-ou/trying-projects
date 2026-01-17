#PHISHING PROJECT
#PHISHING PROJECT
import smtplib
from email.mime.text import MIMEText

expediteur = "evan.oulhen@gmail.com"
destinataire = input("Le couillon qui va se faire avoir :")
Mdp = "qtby lovi jtyj ogsz"#pour appli "Mail" 

message = MIMEText("Bonjour,\n\ncliqué sur ce lien file:///C:/NSI/PHISHING/fichier.html .\n\nCordialement")
message["Subject"] = "Test email Python"
message["From"] = expediteur
message["To"] = destinataire

serveur = smtplib.SMTP("smtp.gmail.com", 587)
serveur.starttls()
serveur.login(expediteur, Mdp)
serveur.send_message(message)
serveur.quit()

print("Email envoyé avec succès")
