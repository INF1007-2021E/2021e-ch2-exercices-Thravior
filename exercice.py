#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    temp=[]
    for lettre in mot:
        if ord(lettre) == 32:
            temp.append(lettre)
        else:
            temp.append(chr(ord(lettre)-32))
    resultat = ''.join(temp)
    return resultat

### cette fonction échoue si des charactères autres que des lettres son envoyé


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
