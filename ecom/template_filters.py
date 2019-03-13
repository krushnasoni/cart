from django import template

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(image):
    import ast
    imgs = ast.literal_eval(image)
    print(imgs)
    for x in imgs :
        img = x
    return img