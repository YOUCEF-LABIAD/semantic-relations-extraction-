#basic graph with composed words, and word "types"

#construct start node	
	#construire classe relation??
	#chercher les IDs de chaque mot??
	#construire relation r_succ avec IDs???
construct r_succ(start, first_word)
type = look for word-type
	#r_pos (rym)
	#attacher r_pos dans le graphe
construct r_pos(first_word,type )
last_word=first_word
for each word
    construct r_succ(last_word,current_word)
    type = look for current_word-type
    construct r_pos(current_word,type )
    found=look for composed words
    if found:
        construct r_succ(last_word,composed_word)
        construct r_succ(composed_word,next_word)
        type = look for composed_word-type
        construct r_pos(composed_word,type )
    last_word=current_word
construct r_succ(last_word,END)




#implementer analyseur syntaxique???
