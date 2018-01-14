import difflib
a = 'unmatched'
b = 'matcythed'
s = difflib.SequenceMatcher(None, a, b)
print(s.ratio())
matchedData = s.find_longest_match(0,len(a),0,len(b));

print(matchedData.size)