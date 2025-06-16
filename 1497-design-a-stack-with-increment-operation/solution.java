class CustomStack {

    private int maxSize;
    private List<Integer> stack;

    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        this.stack = new ArrayList<>();
    }
    
    public void push(int x) {
        if(stack.size() < maxSize){
            stack.add(x);
        }   
    }
    
    public int pop() {
        if(stack.isEmpty()){
            return -1;
        }
        return stack.remove(stack.size()-1);
    }
    
    public void increment(int k, int val) {
        int n = Math.min(k,stack.size());
        for(int i=0; i<n; i++){
            stack.set(i, stack.get(i)+val);
        } 
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
