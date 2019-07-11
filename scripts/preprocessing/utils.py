def get_shingles(doc, size):
    shingles = set()
    if len(doc) > size:
        for i in range(0, len(doc)-size+1):
            shingles.add(doc[i:i+size])
    return shingles
 
def jaccard(set1, set2):
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)

def near_duplicates(df, colnames):
    shingles = []

    for text in df['headline']:
        shingles.append(get_shingles(text, 4))

    colnames.append('shingles')

    return pd.DataFrame({colnames[0]:df[colnames[0]], colnames[1]:df[colnames[1]], colnames[2]:df[colnames[2]], 'shingles':shingles}, columns=colnames)

def elim_near_dups(df):
    
    dups = near_duplicates(df, list(df.columns))

    for i in dups:


#print(shingles[:5])

#print(jaccard(shingles1, shingles2), file1, file2)
