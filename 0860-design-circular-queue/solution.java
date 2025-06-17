class MyCircularQueue {

    private int[] queue;
    private int front;
    private int rear;
    private int size;  

    public MyCircularQueue(int k) {
        queue = new int[k];
        front = -1;
        rear = -1;
        size = k;
    }
    
    public boolean enQueue(int value) {
        if(isFull()){
            return false;
        }

        if(isEmpty()){
            front = 0;
        }

        rear = (rear+1) % size;
        queue[rear] = value;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty()){
            return false;
        }

        if(rear == front){
            front = -1;
            rear = -1;
        } else{
            front = (front+1) % size;
        }
        return true;
    }
    
    public int Front() {
        if(isEmpty()){
            return -1;
        }
        return queue[front];
    }
    
    public int Rear() {
        if(isEmpty()){
            return -1;
        }
        return queue[rear];
    }
    
    public boolean isEmpty() {
        return front == -1;
    }
    
    public boolean isFull() {
        return (rear + 1) % size == front;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
