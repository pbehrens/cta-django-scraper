def get_tag_value(node):
    """retrieves value of given XML node
    parameter:
    node - node object containing the tag element produced by minidom

    return:
    content of the tag element as string
    """

    xml_str = node.toxml() # flattens the element to string

    # cut off the base tag to get clean content:
    start = xml_str.find('>')
    if start == -1:
        return ''
    end = xml_str.rfind('<')
    if end < start:
        return ''

    return xml_str[start + 1:end]