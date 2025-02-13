from utils import ListNode, check_nodes_is_same, listNode2List


def solve_batch(solution_obj, cases):
    """
    批量测试
    """
    sol = solution_obj()
    fn_str = [func for func in dir(sol) if not func.startswith('__')][-1]
    fn = getattr(sol, fn_str)
    for i, case in enumerate(cases):
        result = fn(*case[:-1])
        label = case[-1]
        if isinstance(result, ListNode):
            info = f"case:{i} || {check_nodes_is_same(result, label)} || {listNode2List(result)} || {listNode2List(label)} || "
        else:
            info = f"case:{i} || {result == label} || {result=} || {label=} || "
        info += 'args='
        for param in case[:-1]:
            info += f"`{param}`, "
        print(info)
