from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag,children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Children are required")
        return_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            return_string += child.to_html()
        return_string += f"</{self.tag}>"

        return return_string

        