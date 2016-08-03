# question from interview cake


def is_balanced(tree_root):
    depths = []  # we short-circuit as soon as we find more than 2

    # we'll treat this list as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):

        # pop a node and its depth from the top of our stack
        node, depth = nodes.pop()

        # case: we found a leaf
        if (not node.left) and (not node.right):

            # we only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # two ways we might now have an unbalanced tree:
                # 1) more than 2 different leaf depths
                # 2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or \
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        # case: this isn't a leaf - keep stepping down
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True