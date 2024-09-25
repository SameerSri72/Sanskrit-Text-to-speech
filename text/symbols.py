""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.
"""
_pad = "_"
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"

_data_letters_ipa = "̃"
#_data_letters = "ঁংঃঅআইঈউঊঋএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধনপফবভমযরলশষসহ়ািীুূৃেৈোৌ্ৎড়ঢ়য়ৠ"
#_data_letters = "'ं'ःअआइईउऊऋॠऌएऐओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरलवशषसहळ'ा'ि'ी'ु'ू'ृ'ॄ'े'ै'ो'ौ'्"
symbols= ["_", "\u0964", "\u0901", "\u0902", "\u0903", "\u0905", "\u0906", "\u0907", "\u0908", "\u0909", "\u090a", "\u090b", "\u090f", "\u0910", "\u0913", "\u0914", "\u0915", "\u0916", "\u0917", "\u0918", "\u0919", "\u091a", "\u091b", "\u091c", "\u091d", "\u091e", "\u091f", "\u0920", "\u0921", "\u0922", "\u0923", "\u0924", "\u0925", "\u0926", "\u0927", "\u0928", "\u092a", "\u092b", "\u092c", "\u092d", "\u092e", "\u092f", "\u0930", "\u0932", "\u0933", "\u0935", "\u0936", "\u0937", "\u0938", "\u0939", "\u093d", "\u093e", "\u093f", "\u0940", "\u0941", "\u0942", "\u0943", "\u0944", "\u0947", "\u0948", "\u094b", "\u094c", "\u094d", "\u0960", "\u0962", " "]
# Export all symbols:
#symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa) + list(_data_letters_ipa) + list(_data_letters)+ list("ङचछजझञटठडढ")


# Special symbol ids
SPACE_ID = symbols.index(" ")
