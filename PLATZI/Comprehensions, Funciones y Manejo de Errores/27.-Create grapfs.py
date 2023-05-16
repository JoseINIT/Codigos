import matplotlib.pyplot as plt
def generate_bar_chart(labels,value,):
    fig,ax=plt.subplots()
    ax.bar(labels,value)
    plt.show()
def generate_pie_chart(labels,value,):
    fig,ax=plt.subplots()
    ax.pie(value,labels=labels)
    ax.axis("equal")
    plt.show()
if __name__ == "__main__":
    labels = ["a", "b", "c","d"]
    value = [100, 200, 300,12]
    pendejos=["7","8","9 o mas"]
    generate_bar_chart(labels,value)
    generate_pie_chart(labels,value)