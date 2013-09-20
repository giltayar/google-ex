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
        def add_to(attr):
            if getattr(self, attr) is None:
                setattr(self, attr, Tree(value))
            else:
                getattr(self, attr).add_mutable(value)

        for value in values:
            if value <= self.value:
                add_to('left')
            else:
                add_to('right')

        assert self._is_sorted()
        return self

    def del_mutable(self, value):
        tree, parent = self._find_with_parent(value)
        tree._delete(parent)
        assert self._is_sorted()

    def _find_with_parent(value, parent = None):
        if value < self.value:
            if self.left is None:
                raise Exception("Not found!")
            return self.left.find_with_parent(value, self)
        elif value > self.value:
            if self.right is None:
                raise Exception("Not found!")
            return self.right.find_with_parent(value, self)
        else:
            return self, parent

    def _delete(parent):
        if parent is None:
            raise Exception("Cannot delete top element!")
        if self.left is None and self.right is None:
            if parent.right == self:
                parent.right = None
            else:
                parent.left = None
        elif self.left is None:
            self.value = self.right.value
            self.left = self.right.left
            self.right = self.right.right
        elif self.right is None:
            self.value = self.left.value
            self.left = self.left.left
            self.right = self.left.left
        else:
            predecessor, pred_parent = self._find_predecessor(value)
            predecessor._delete(pred_parent)

    def _find_predecessor(value, parent=None):
        if self.left is None:
            return 
        
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


