class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        prop_string = ""
        for prop in self.props:
            prop_string += f' {prop}="{self.props[prop]}"'
        return prop_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    


class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value)
        self.children = None

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(props)
        self.tag = tag
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError(("no children"))
        
        children_html = []
        for children in self.children:
            children_html.append(children.to_html())
        
        final_string = "".join(children_html)
        return f"<{self.tag}>{final_string}</{self.tag}>"