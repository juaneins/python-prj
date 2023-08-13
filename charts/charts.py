import matplotlib.pyplot as pyplot


def generate_pie_chart():
    labels = ['a','b','c']
    values = [100,200,300]
    fig, ax = pyplot.subplots()
    
    ax.pie(values, labels=labels)
    pyplot.savefig('pie.png')
    pyplot.close()
