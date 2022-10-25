def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    n1=len(s1)
    n2=len(s2)
    n3=len(s3)
    ans='['
    if n1%2!=0:
        ans+=","+s2
    if n2%2!=0:
        ans+=","+s2
    if n3%2!=0:
        ans+=","+s3

    return ans+']'
print(main('11','22','31'))