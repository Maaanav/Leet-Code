class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder w1 = new StringBuilder();
        for(String word : word1){
            w1.append(word);
        }

        StringBuilder w2 = new StringBuilder();
        for(String word : word2){
            w2.append(word);
        }
        if(w1.toString().equals(w2.toString())){
            return true;
        }
        return false;
    }
}
