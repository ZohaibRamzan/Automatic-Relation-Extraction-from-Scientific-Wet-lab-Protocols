"""
Define constants.
"""
EMB_INIT_RANGE = 1.0

# vocab
PAD_TOKEN = '<PAD>'
PAD_ID = 0
UNK_TOKEN = '<UNK>'
UNK_ID = 1

VOCAB_PREFIX = [PAD_TOKEN, UNK_TOKEN]

# hard-coded mappings from fields to ids
SUBJ_NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'Action': 2, 'Reagent': 3,'Location':4, 'Mention':5, 'Concentration':6,'Time':7,'Numerical':8, 'Device':9, 'Temperature':10, 'Amount': 11, 'Modifier': 12, 'Size':13, 'Speed':14, 'Measure-Type':15, 'Method':16, 'Generic-Measure':17, 'Seal':18, 'Unit': 19, 'pH':20, 'Misc':21}

OBJ_NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'Reagent': 2, 'Numerical':3, 'Concentration':4, 'Time':5, 'Location':6 , 'Mention':7, 'Temperature':8, 'Device':9, 'Generic-Measure':10, 'Action': 11, 'Amount': 12, 'Modifier': 13, 'Method':14, 'Size':15, 'Measure-Type':16, 'Speed':17, 'Seal':18,'Unit': 19, 'pH':20, 'Misc':21}

NER_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'O': 2, 'Action': 3, 'Amount': 4, 'Location': 5, 'Modifier': 6, 'Time': 7, 'Temperature': 8, 'Concentration': 9, 'Device': 10, 'Speed': 11, 'Method': 12, 'Generic-Measure': 13, 'Size': 14, 'Numerical': 15, 'Measure-Type': 16, 'Seal': 17, 'Mention': 18, 'pH': 19, 'Misc': 20, 'Unit': 21}


POS_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'NN': 2, 'IN': 3, 'CD': 4, 'VB': 5, 'DT': 6, 'NNS': 7, '.': 8, ',': 9, 'JJ': 10, 'CC': 11, 'RB': 12, 'VBN': 13, '-RRB-': 14, 'NNP': 15, '-LRB-': 16, 'VBG': 17, 'HYPH': 18, 'SYM': 19, 'TO': 20, 'FW': 21, ':': 22, 'RP': 23, 'VBZ': 24, 'PRP': 25, 'VBP': 26, 'VBD': 27, 'MD': 28, 'RBS': 29, 'PRP$': 30, 'POS': 31, 'JJR': 32, "''": 33, '``': 34, 'WDT': 35, 'WRB': 36, 'NFP': 37, 'UH': 38, 'LS': 39, 'NNPS': 40, 'JJS': 41, '$': 42, 'EX': 43, 'PDT': 44, 'RBR': 45, 'AFX': 46, '-RSB-': 47, '-LSB-': 48, 'ADD': 49, 'GW': 50, 'WP': 51}

DEPREL_TO_ID = {PAD_TOKEN: 0, UNK_TOKEN: 1, 'punct': 2, 'case': 3, 'compound': 4, 'root': 5, 'nummod': 6, 'obl': 7, 'obj': 8, 'det': 9, 'nmod': 10, 'conj': 11, 'amod': 12, 'cc': 13, 'appos': 14, 'advmod': 15, 'mark': 16, 'advcl': 17, 'flat': 18, 'parataxis': 19, 'acl': 20, 'nsubj': 21, 'compound:prt': 22, 'aux:pass': 23, 'xcomp': 24, 'nsubj:pass': 25, 'aux': 26, 'nmod:poss': 27, 'obl:npmod': 28, 'obl:tmod': 29, 'cop': 30, 'fixed': 31, 'acl:relcl': 32, 'ccomp': 33, 'list': 34, 'dep': 35, 'nmod:npmod': 36, 'discourse': 37, 'cc:preconj': 38, 'goeswith': 39, 'expl': 40, 'nmod:tmod': 41, 'iobj': 42, 'det:predet': 43, 'csubj': 44, 'orphan': 45, 'vocative': 46}

NEGATIVE_LABEL = 'no-relation'



LABEL_TO_ID = {'no-relation': 0, 'Acts-on': 1,  'Setting': 2, 'Count': 3, 'Creates': 4, 'Measure': 5, 'Measure-Type-Link': 6,  'Meronym': 7, 'Misc-Link': 8, 'Of-Type': 9, 'Or': 10, 'Coreference-Link': 11, 'Site': 12, 'Using': 13, 'Mod-Link':14}

INFINITY_NUMBER = 1e12
