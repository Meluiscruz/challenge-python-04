def div(func):
    # You have to code here!
    def wrapper(*arg, **kwargs):
        answer_1 = f'<div>{func(*arg, **kwargs)}</div>'
        return answer_1

    return wrapper      

def article(func):
    # You have to code here!
    def wrapper(*arg, **kwargs):
        answer_2 = f'<article>{func(*arg, **kwargs)}</article>'
        return answer_2

    return wrapper   

def p(func):
    # You have to code here!
    def wrapper(*arg, **kwargs):
        answer_3 = f'<p>{func(*arg, **kwargs)}</p>'
        return answer_3

    return wrapper   


# Here you must apply the decorators, uncomment this later
@div
@article
@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
