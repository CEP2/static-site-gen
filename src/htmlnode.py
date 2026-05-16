class HTMLNode():
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        prop_str = ""
        if self.props is None:
            return prop_str
        for prop in self.props:
            prop_str +=  f" {prop}=\"{self.props[prop]}\""
        return prop_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"