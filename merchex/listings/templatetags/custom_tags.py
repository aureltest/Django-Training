from django import template

register = template.Library()


@register.filter(name="add_classes")
def add_classes(value, arg):
    css_classes = value.field.widget.attrs.get("class", "")
    css_classes = css_classes.split(" ") if css_classes else []
    args = arg.split(" ")
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    value.field.widget.attrs["class"] = " ".join(css_classes)
    return value
