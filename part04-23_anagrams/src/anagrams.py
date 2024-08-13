# Write your solution here
def anagrams(s1,s2):

    st1 = sorted(s1)
    st2 = sorted(s2)

    if st1 == st2:
        return True
    else:
        return False
