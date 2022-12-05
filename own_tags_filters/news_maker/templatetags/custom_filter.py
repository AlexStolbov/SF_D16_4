from django import template

register = template.Library()

forbidden_words = [
    'anyones',
    'many'
]


@register.filter
def censor(value: str):
    checked_words = value.split(' ')
    result = []
    for word in checked_words:
        if word in forbidden_words:
            new_word = word[0] + '*' * (len(word) - 2) + word[-1]
        else:
            new_word = word
        result.append(new_word)
    return ''.join(result)
