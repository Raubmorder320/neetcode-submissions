/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
	curr:=head
	d:=make(map[int] *ListNode)
	for curr!=nil{
		if v, ok:= d[curr.Val]; ok && curr==v{
			return true
		}
		d[curr.Val]=curr
		curr=curr.Next
	}
	return false
}
