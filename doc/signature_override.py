"""
    doc.signature_override
    ~~~~~~~~~~~~~~~~~~~~~~

    This module overrides signatures to old school format::

        (foo, bar, baz="spam", *args, **kwargs) => (foo, bar[, baz="spam"[, *args[, **kwargs]]])
"""


def process_signatures(app, what, name, obj, options, signature, return_annotation):
    if what not in ["function", "method", "class"]:
        return (signature, return_annotation)

    new_signature = []
    brackets = 0
    for item in signature[1:-1].split(", "):
        if "=" in item or "*" in item:
            item = "[," + item
            brackets += 1
        else:
            item = "," + item
        new_signature.append(item)
    new_signature = "({0})".format("".join(new_signature) + "]" * brackets)
    return (new_signature, return_annotation)


def setup(app):
    app.connect("autodoc-process-signature", process_signatures)
