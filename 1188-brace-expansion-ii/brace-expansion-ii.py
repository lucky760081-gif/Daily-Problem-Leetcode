class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        self.s = expression
        self.i = 0

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse_expr():
            res = parse_term()

            while self.i < len(self.s) and self.s[self.i] == ',':
                self.i += 1
                res |= parse_term()

            return res

        def parse_term():
            res = {""}

            while self.i < len(self.s) and self.s[self.i] not in "},":
                if self.s[self.i] == '{':
                    self.i += 1
                    cur = parse_expr()
                    self.i += 1
                else:
                    cur = {self.s[self.i]}
                    self.i += 1

                res = product(res, cur)

            return res

        return sorted(parse_expr())