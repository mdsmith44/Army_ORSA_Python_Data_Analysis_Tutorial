#Display indices of any python sequence
from IPython.core.display import display, HTML
def display_indices(seq):
    #display indices of any python sequence x
    html_code = "<table><tr>"
    for i in range(len(seq)):
        html_code += "<td>{}</td>".format(i)
    html_code += "</tr><tr>"
    for x in seq:
        html_code += "<td>{}</td>".format(x)
    html_code += "</tr></table"
    display(HTML(html_code))