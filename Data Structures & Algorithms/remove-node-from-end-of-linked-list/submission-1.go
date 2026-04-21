/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
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

    rev := reverse(head)
    c:=1

    d:=&ListNode{Next:rev}
    p:=d
    for c<=n+1{
        if c==n{

            p.Next=p.Next.Next
            break
        }
        c++
        p=p.Next

    }
    head = reverse(d.Next)
    return head
}
