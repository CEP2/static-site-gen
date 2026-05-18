from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        if self.value is None:
            raise Exception (ValueError)
        if self.tag is None:
            return self.value
        html_str = f"<{self.tag}"
        html_str += self.props_to_html()
        html_str += f">{self.value}</{self.tag}>"
        return html_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
