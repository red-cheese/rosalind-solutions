import operator
import solution


def extract_chars(id_char_pair_set):
    return {char for _, char in id_char_pair_set}


def find_char(char, id_char_pair_set):
    for pair in id_char_pair_set:
        if pair[1] == char:
            return pair
    raise ValueError


class TRIE(solution.Solution):

    def _read(self, f):
        return [line.strip() for line in f]

    def solve(self, dna_strings):
        root = (1, None)  # ID, Symbol
        trie = {root: set()}
        max_id = 1

        for dna in dna_strings:
            i = 0
            cur_parent = root
            cur_children = trie[cur_parent]

            while True:
                try:
                    cur_parent = find_char(dna[i], cur_children)
                    cur_children = trie[cur_parent]
                    i += 1
                except ValueError:
                    break

            if i < len(dna):
                for j in range(i, len(dna)):
                    max_id += 1
                    trie[cur_parent].add((max_id, dna[j]))
                    trie[(max_id, dna[j])] = set()
                    cur_parent = (max_id, dna[j])

        res = []
        for (parent_id, _), children in trie.items():
            for child_id, child_char in children:
                res.append((parent_id, child_id, child_char))
        return sorted(res, key=operator.itemgetter(1))

    def _write(self, f, edges):
        for v_from, v_to, char in edges:
            f.write('{} {} {}\n'.format(v_from, v_to, char))
