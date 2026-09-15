pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}


def quantite_piece(stock, modele, piece ) :
    return stock[modele][piece]

def consommer_piece(stock, modele, piece, quantite):
    stock[modele][piece] -= quantite

def ajouter_modele(stock, modele, moteurs, capteurs, roues):
    stock[modele] = {"moteurs": moteurs, "capteurs": capteurs, "roues": roues}

def total_pieces(stock):
    total = {"moteurs": 0, "capteurs": 0, "roues": 0}
    for modele in stock.values():
        for piece, quantite in modele.items():
            total[piece] += quantite
    return total
 
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10
consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
ajouter_modele(pieces_stock, "ModeleC",
moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}