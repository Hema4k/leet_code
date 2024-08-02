class Solution:
	def reverseList(self,head):

		prev = None
		current = head

		while current:
			t = current.next
			current.next = prev
			prev = current
			current = t

		return prev

