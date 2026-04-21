/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    middle:=head
	fast:=head
	for fast!=nil && fast.Next!=nil{
		fast=fast.Next.Next
		middle=middle.Next
	}
	left:=head
	right:=middle.Next
	middle.Next=nil
	reverse:=func(head *ListNode) *ListNode{
		curr:=head
		nxt:=head
		var prev *ListNode
		for nxt!=nil{
			nxt=curr.Next
			curr.Next = prev
			prev = curr
			curr=nxt
		}
        return prev
	}
	right = reverse(right)
    var t1,t2 *ListNode

    for right!=nil&&left!=nil{
        t1,t2 = left.Next,right.Next
        right.Next, left.Next = left.Next, right
        right, left = t2, t1

    }
	
}
