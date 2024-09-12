class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
def addTwo(l1, l2):

    head_node = Node(0)
    current = head_node
    carry = 0
    while l1 or l2 or carry:
        
        if l1:
            carry += l1.data
            l1 = l1.next_node
        if l2:
            carry += l2.data
            l2 = l2.next_node
        current.next_node = Node(carry%10)
        carry //= 10
        
        current = current.next_node
    
    return head_node.next_node        
