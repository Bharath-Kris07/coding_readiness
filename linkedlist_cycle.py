class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next       
            fast = fast.next.next     
            if slow == fast:
                return True
        return False
def build_linked_list_with_cycle(arr, pos):
    if not arr or arr[0] == -1:
        return None
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    for i in range(1, len(arr)):
        if arr[i] == -1:
            break
        new_node = ListNode(arr[i])
        current.next = new_node
        current = new_node
        if i == pos:
            cycle_node = new_node
    if pos != -1:
        current.next = cycle_node
    return head
print("Enter the linked list elements separated by a space (use -1 to stop):")
arr_input = list(map(int, input().split()))
print("Enter the index you want the cycle to loop back to (Enter -1 for NO cycle):")
cycle_pos = int(input())
linked_list_head = build_linked_list_with_cycle(arr_input, cycle_pos)
solution = Solution()
result = solution.hasCycle(linked_list_head)
print(f"\nDoes the list have a cycle? {result}")