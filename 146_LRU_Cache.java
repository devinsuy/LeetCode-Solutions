<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="2022.3">
  <style type="text/css">
    p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica}
    p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; min-height: 14.0px}
  </style>
</head>
<body>
<p class="p1">class ListNode {</p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode prev;</p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode next;</p>
<p class="p1"><span class="Apple-converted-space">    </span>public int key;</p>
<p class="p1"><span class="Apple-converted-space">    </span>public int value;</p>
<p class="p1"><span class="Apple-converted-space">    </span>public boolean isDummy;</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode(int key, int value){</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.prev = this.next = null;</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.key = key;</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.value = value;</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.isDummy = false;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode(ListNode prev, ListNode next, boolean isDummy){</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.prev = prev;</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.next = next;</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.isDummy = isDummy;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public void setVal(int newVal){</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.value = newVal;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p1">}</p>
<p class="p2"><br></p>
<p class="p1">class DLL {</p>
<p class="p1"><span class="Apple-converted-space">    </span>private ListNode head;</p>
<p class="p1"><span class="Apple-converted-space">    </span>private ListNode tail;</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public DLL(){</p>
<p class="p1"><span class="Apple-converted-space">      </span>// Maintain list using dummy head and tail nodes</p>
<p class="p1"><span class="Apple-converted-space">      </span>this.head = new ListNode(null, null, true);</p>
<p class="p1"><span class="Apple-converted-space">      </span>this.tail = new ListNode(null, null, true);</p>
<p class="p1"><span class="Apple-converted-space">      </span>this.head.next = this.tail;</p>
<p class="p1"><span class="Apple-converted-space">      </span>this.tail.prev = this.head;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode getFirst(){</p>
<p class="p1"><span class="Apple-converted-space">      </span>ListNode firstNode = this.head.next;</p>
<p class="p1"><span class="Apple-converted-space">      </span>return firstNode.isDummy ? null : firstNode;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode getLast(){</p>
<p class="p1"><span class="Apple-converted-space">      </span>ListNode lastNode = this.tail.prev;</p>
<p class="p1"><span class="Apple-converted-space">      </span>return lastNode.isDummy ? null : lastNode;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public void addFirst(ListNode node){</p>
<p class="p1"><span class="Apple-converted-space">        </span>ListNode temp = this.head.next;</p>
<p class="p1"><span class="Apple-converted-space">        </span>if(!(temp.equals(this.tail))){</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.head.next = node;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.prev = this.head;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.next = temp;</p>
<p class="p1"><span class="Apple-converted-space">            </span>temp.prev = node;</p>
<p class="p1"><span class="Apple-converted-space">        </span>}<span class="Apple-converted-space"> </span></p>
<p class="p1"><span class="Apple-converted-space">        </span>else { // Insert node into empty list<span class="Apple-converted-space"> </span></p>
<p class="p1"><span class="Apple-converted-space">            </span>this.head.next = node;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.prev = this.head;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.next = this.tail;</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.tail.prev = node;</p>
<p class="p1"><span class="Apple-converted-space">        </span>}</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public void addLast(ListNode node){</p>
<p class="p1"><span class="Apple-converted-space">        </span>ListNode temp = this.tail.prev;</p>
<p class="p1"><span class="Apple-converted-space">        </span>if(!(temp.equals(head))){</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.tail.prev = node;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.next = this.tail;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.prev = temp;</p>
<p class="p1"><span class="Apple-converted-space">            </span>temp.next = node;</p>
<p class="p1"><span class="Apple-converted-space">        </span>} else { // Insert into empty list</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.tail.prev = node;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.next = this.tail;</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.prev = this.head;</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.head.next = node;</p>
<p class="p1"><span class="Apple-converted-space">        </span>}</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>// Remove a node and update pointers</p>
<p class="p1"><span class="Apple-converted-space">    </span>public void remove(ListNode node){</p>
<p class="p1"><span class="Apple-converted-space">      </span>ListNode curr_prev = node.prev;</p>
<p class="p1"><span class="Apple-converted-space">      </span>ListNode curr_next = node.next;</p>
<p class="p1"><span class="Apple-converted-space">      </span>node.next = node.prev = null;</p>
<p class="p1"><span class="Apple-converted-space">      </span>curr_prev.next = curr_next;</p>
<p class="p1"><span class="Apple-converted-space">      </span>curr_next.prev = curr_prev;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>// Remove the last node and return it</p>
<p class="p1"><span class="Apple-converted-space">    </span>public ListNode removeLast(){</p>
<p class="p1"><span class="Apple-converted-space">        </span>ListNode lastNode = this.getLast();</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.remove(lastNode);</p>
<p class="p1"><span class="Apple-converted-space">        </span>return lastNode;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><br></p>
<p class="p1"><span class="Apple-converted-space">    </span>// Move a given node to the front of the list</p>
<p class="p1"><span class="Apple-converted-space">    </span>public void setMRU(ListNode node){</p>
<p class="p1"><span class="Apple-converted-space">      </span>this.remove(node);</p>
<p class="p1"><span class="Apple-converted-space">      </span>this.addFirst(node);</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p1">}</p>
<p class="p2"><br></p>
<p class="p1">class LRUCache {</p>
<p class="p1"><span class="Apple-converted-space">    </span>private int capacity;</p>
<p class="p1"><span class="Apple-converted-space">    </span>private HashMap&lt;Integer, ListNode&gt; keyNodes;</p>
<p class="p1"><span class="Apple-converted-space">    </span>private DLL nodes;</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public LRUCache(int capacity) {</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.capacity = capacity;</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.keyNodes = new HashMap&lt;&gt;();</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.nodes = new DLL();</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public int get(int key) {</p>
<p class="p1"><span class="Apple-converted-space">        </span>if(!(this.keyNodes.containsKey(key))){</p>
<p class="p1"><span class="Apple-converted-space">            </span>return -1;</p>
<p class="p1"><span class="Apple-converted-space">        </span>}</p>
<p class="p1"><span class="Apple-converted-space">        </span>ListNode node = this.keyNodes.get(key);</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.nodes.setMRU(node);</p>
<p class="p1"><span class="Apple-converted-space">        </span>return node.value;</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>// Locate the LRU key and remove it</p>
<p class="p1"><span class="Apple-converted-space">    </span>private void evict(){</p>
<p class="p1"><span class="Apple-converted-space">        </span>ListNode nodeToRemove = this.nodes.removeLast();</p>
<p class="p1"><span class="Apple-converted-space">        </span>this.keyNodes.remove(nodeToRemove.key);</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span>public void put(int key, int value) {</p>
<p class="p1"><span class="Apple-converted-space">        </span>ListNode node;<span class="Apple-converted-space"> </span></p>
<p class="p2"><span class="Apple-converted-space">        </span></p>
<p class="p1"><span class="Apple-converted-space">        </span>// Update an existing key and set it as MRU</p>
<p class="p1"><span class="Apple-converted-space">        </span>if(this.keyNodes.containsKey(key)){</p>
<p class="p1"><span class="Apple-converted-space">            </span>node = this.keyNodes.get(key);</p>
<p class="p1"><span class="Apple-converted-space">            </span>node.setVal(value);</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.nodes.setMRU(node);</p>
<p class="p1"><span class="Apple-converted-space">        </span>}<span class="Apple-converted-space"> </span></p>
<p class="p1"><span class="Apple-converted-space">        </span>else {</p>
<p class="p1"><span class="Apple-converted-space">            </span>if(this.keyNodes.size() == this.capacity){</p>
<p class="p1"><span class="Apple-converted-space">                </span>this.evict();</p>
<p class="p1"><span class="Apple-converted-space">            </span>}</p>
<p class="p1"><span class="Apple-converted-space">            </span>node = new ListNode(key, value);</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.keyNodes.put(key, node);</p>
<p class="p1"><span class="Apple-converted-space">            </span>this.nodes.addFirst(node);</p>
<p class="p1"><span class="Apple-converted-space">        </span>}</p>
<p class="p1"><span class="Apple-converted-space">    </span>}</p>
<p class="p1">}</p>
</body>
</html>
