class Tree(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

        assert self._is_sorted()

    def height(self):
        return 1 + max(self.left.height() if self.left else 0,
                self.right.height() if self.right else 0)

    def _is_sorted(self):
        left_value_ok = (self.value > self.left.value 
            if self.left is not None else True)
        if not left_value_ok:
            return False
        right_value_ok = (self.value < self.right.value 
            if self.right is not None else True)
        if not right_value_ok:
            return False

        return ((self.left._is_sorted() if self.left is not None else True) and
                (self.right._is_sorted() if self.right is not None else True)) 

    def add_mutable(self, *values):
        def add_to(attr, value):
            if getattr(self, attr) is None:
                setattr(self, attr, Tree(value))
            else:
                getattr(self, attr).add_mutable(value)

        for value in values:
            if value <= self.value:
                add_to('left', value)
            else:
                add_to('right', value)

        assert self._is_sorted(), "cannot add {} to {!r}".format(value, self)
        return self

    def del_mutable(self, value):
        tree, parent = self._find_with_parent(value)
        tree._delete(parent)

        assert self._is_sorted()

        return self

    def _find_with_parent(self, value, parent = None):
        if value < self.value:
            if self.left is None:
                raise Exception("Not found!")
            return self.left._find_with_parent(value, self)
        elif value > self.value:
            if self.right is None:
                raise Exception("Not found!")
            return self.right._find_with_parent(value, self)
        else:
            return self, parent

    def _delete(self, parent):
        def replace_with(tree):
            self.value = tree.value
            self.left = tree.left
            self.right = tree.right
        if self.left is None and self.right is None:
            if parent.right == self:
                parent.right = None
            else:
                parent.left = None
        elif self.left is None:
            replace_with(self.right)
        elif self.right is None:
            replace_with(self.left)
        else:
            predecessor, pred_parent = self._find_predecessor(self.value)
            self.value = predecessor.value
            predecessor._delete(pred_parent)

    def _find_predecessor(self, value, parent=None):
        if self.left is None:
            return None, self

        def find_last_rightie(tree, parent):
            if tree.right is None:
                return tree, parent
            else:
                return find_last_rightie(tree.right, tree)

        return find_last_rightie(self.left, self)
        
    def add_immutables(self, *values):
        res = self
        for value in values:
            res = res.add_immutable(value)
        return res

    def add_immutable(self, value):
        if value == self.value:
            return self
        if value < self.value:
            return Tree(self.value, 
                    self.left.add_immutable(value) 
                    if self.left is not None else Tree(value),
                    self.right)
        else: 
            return Tree(self.value, 
                    self.left,
                    self.right.add_immutable(value) 
                    if self.right is not None else Tree(value))

    def __str__(self):
        return self.as_string(0) 
   
    def __repr__(self):
        return "Tree({}, {}, {})".format(self.value, repr(self.left), repr(self.right))

    def as_string(self, indent):
       return (' ' * (indent * 2) +
               '|- ' + str(self.value) +
               ('\n' + (self.left.as_string(indent + 1) if self.left is not None else ' ' * ((indent+1)*2) + '|')) +
               ('\n' + self.right.as_string(indent + 1) if self.right is not None else '')
               )

    def as_list(self):
        return ((self.left.as_list() if self.left is not None else []) +
                [self.value] + 
                (self.right.as_list() if self.right is not None else []))


