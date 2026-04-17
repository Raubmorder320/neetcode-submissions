func mergeAlternately(word1 string, word2 string) string {
    s1:= []rune(word1)
    s2:= []rune(word2)
    res:=make([]rune,0,len(s1)+len(s2))
    for i:=0;i<len(s1)&&i<len(s2);i++{
        res = append(append(res, s1[i]), s2[i])

    }
    if len(s1)<len(s2){
    res=append(res, s2[len(s1):]...)

    } else{
    res=append(res, s1[len(s2):]...)
    }
    return string(res)
}
