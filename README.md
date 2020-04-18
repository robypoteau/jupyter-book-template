## Jupyter Online Book Template

Inspired by [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook), this project hopes to develop a simple way to generate online books made up of by Jupyter notebooks, to be displayed in GitHub pages.

In this project you can must create an ordering for your pages using the titles and the script will auto-generate the links between pages.

You can find the book [here](https://www.robopoto.com/jupyter-book-template/).


'''
jupyter nbconvert notebooks/*.ipynb
mv notebooks/*.ipynb ./docs/
'''
