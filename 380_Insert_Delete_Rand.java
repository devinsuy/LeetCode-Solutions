class RandomizedSet {
    // Maintain an arraylist for O(1) getRandom by random index
    private ArrayList<Integer> vals;

    // Map value to the index the value is stored in the arraylist
    // O(1) contains() operation on keyset and O(1) put(), remove() 
    private HashMap<Integer,Integer> elemIndex;
    
    // Generate random indices bounded by the length of the list for getRandom()
    private Random rand;
    
    /** Initialize your data structure here. */
    public RandomizedSet() {
        this.elemIndex = new HashMap<>();
        this.vals = new ArrayList<>();
        this.rand = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if(this.elemIndex.containsKey(val))
            return false;
        // Map the element to the index of it is stored at in the array
        else {
            this.vals.add(val);
            this.elemIndex.put(val, this.vals.size()-1);
            return true;
        }            
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if(this.elemIndex.containsKey(val)){
            // Copy the last element in the arraylist to the index of the value
            // being removed, then remove the last element of the array list O(1)
            if(this.vals.size() > 1){
                int valIndex = this.elemIndex.get(val);
                int lastVal = this.vals.get(this.vals.size()-1);
                this.vals.set(valIndex, lastVal);
                this.vals.remove(this.vals.size()-1);
                this.elemIndex.put(lastVal, valIndex);
            } 
            // If the RandomizedSet only contains 1 item we can just remove directly in O(1)
            else 
                this.vals.remove(0);
            
            // Remove the value from the hashmap in O(1)
            this.elemIndex.remove(val);
            return true;
        } 
        // The values being removed does not exit
        else 
            return false;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        return this.vals.get(this.rand.nextInt(this.vals.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */