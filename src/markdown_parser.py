from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            # this means we may have work to do
            if delimiter in node.text:
                # we for sure have work to do
                strings = node.text.split(delimiter)

                if len(strings) % 2 == 0:
                    raise Exception("No End Markdown Found")
                for i in range (0, len(strings)-1, 2):
                    # i will be before the delimiter and a text node
                    # i + 1 will be the object that should be marked
                    new_nodes.append(TextNode(strings[i], TextType.TEXT))
                    new_nodes.append(TextNode(strings[i+1], text_type))
                # there will be one string left over, see if it has a value
                if strings[len(strings) - 1] != "":
                    new_nodes.append(TextNode(strings[len(strings)-1], text_type.TEXT))
        else:
            # this has already been parsed
            new_nodes.append(node)

    return new_nodes