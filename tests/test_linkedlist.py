import unittest
from ds import linkedlist


class TestSuite(unittest.TestCase):

    def test_singly_linked_list(self):

        sl_list = linkedlist.SinglyLinkedList()
        self.assertEqual(0, len(sl_list))

        sl_list.append(100)
        sl_list.append(200)
        sl_list.append(300)
        self.assertEqual(3, len(sl_list))

        sl_list.append(500)
        self.assertEqual(4, len(sl_list))

        node_999 = sl_list.appendleft(999)
        self.assertEqual("999 -> 100 -> 200 -> 300 -> 500", str(sl_list))

        node_888 = sl_list.appendleft(888)
        self.assertEqual("888 -> 999 -> 100 -> 200 -> 300 -> 500", str(sl_list))

        sl_list.append_after(node_999, 998)
        self.assertEqual("888 -> 999 -> 998 -> 100 -> 200 -> 300 -> 500", str(sl_list))

        sl_list.append_after(node_888, 886)
        self.assertEqual("888 -> 886 -> 999 -> 998 -> 100 -> 200 -> 300 -> 500", str(sl_list))

        self.assertEqual(8, len(sl_list))
