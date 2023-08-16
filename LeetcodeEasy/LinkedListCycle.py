class Soluton(object):
    def hasCycle(self, head):
        # Use a fast slow pointer method
        fast = head
        slow = head
        
        while fast and fast.next:
            # We make it fast x2 and slow x1 which allows us to see whether or not the fast popionter comes around again making it a cycle
            fast = fast.next.next
            slow = slow.next
            
            # Return True if they equal
            if fast == slow:
                return True
        # Return False if fast pointer returns null meaning it was not a cycle
        return False