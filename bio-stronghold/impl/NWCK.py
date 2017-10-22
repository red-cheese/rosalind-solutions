import solution


class NWCK(solution.ArrayWriteSolution):

    def __parseSubtree(self, s, max_node_id, g, labels):
        max_node_id += 1
        node_id = max_node_id
        print()
        print('Processing node', node_id, '; s =', s)

        children_end = s.rfind(')')
        if len(s) > 0 and s[0] == '(':
            assert children_end != -1
        else:
            assert children_end == -1

        if children_end == -1:
            children = None
            label = s
        else:
            children = s[1:children_end]
            label = s[(children_end + 1):]

        print('Children:', children, 'Label:', label)

        labels[node_id] = label
        g[node_id] = set()
        if children is not None:
            prefix = ''
            split_children = []
            for i, c in enumerate(children):
                if c == ',' and children[:i].count('(') == children[:i].count(')'):
                    split_children.append(prefix)
                    prefix = ''
                else:
                    prefix += c
            split_children.append(prefix)
            children = split_children

            for child in children:
                print('Go into child', child)
                max_node_id, child_node_id = self.__parseSubtree(child, max_node_id, g, labels)
                g[node_id].add(child_node_id)
                g[child_node_id].add(node_id)
                print()
                print('Came back to', label)

        print('ID:', node_id)
        return max_node_id, node_id

    def _parseTree(self, s):
        """Parses a rooted Newick tree out of s."""

        assert s[-1] == ';'  # Root.
        g = {}
        labels = {}  # Node label to its ID.
        self.__parseSubtree(s[:-1], -1, g, labels)

        print()
        print('RESULT:')
        for k, v in g.items():
            print(k, labels[k], '->', {(vv, labels[vv]) for vv in v})
        print()

        return g, labels

    def _read(self, f):
        data = []
        while True:
            try:
                tree = next(f).strip()
                n1, n2 = next(f).strip().split()
                data.append((tree, n1, n2))
                _ = next(f)
            except StopIteration:
                return data

    def __dist(self, g, n1, n2):
        """BFS in acyclic undirected graph."""

        if n1 == n2:
            return 0

        d = 0
        q = [n1]
        visited = set()

        while q:
            d += 1
            q = [nn for n in q for nn in g[n] if nn not in visited]
            visited.update(q)
            if n2 in q:
                return d

        return -1

    def __find_label(self, n, labels):
        for node_id, label in labels.items():
            if n == label:
                return node_id
        return -1

    def solve(self, data):
        answers = []
        for s, n1, n2 in data:
            g, labels = self._parseTree(s)
            answers.append(self.__dist(g, self.__find_label(n1, labels), self.__find_label(n2, labels)))
        return answers


def _test():
    alg = NWCK()

    s = '(dog,cat);'
    alg._parseTree(s)

    print()
    print()

    s = '(cat)dog;'
    alg._parseTree(s)

if __name__ == '__main__':
    _test()
