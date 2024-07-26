# Welcome to My Blank Project's documentation!
  
The purpose of the project is to serve as a template for creating a new project.
The idea is that you can substitute your own code and documentation into
the placeholders here.

```{toctree}
:maxdepth: 2
:caption: Contents
_notebook_build/_01_example_notebook.ipynb
_notebook_build/_01_python_jupyter_demo.ipynb
_notebook_build/_02_interactive_plot_example.ipynb
myst_markdown_demos.md
notebooks.md
apidocs/index
```

## Notes

- Note that I have included the notebooks here twice. This is just to
  demonstrate how you can create subsections with child pages in the table of
  contents. You can read more about this
  [here.](https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#using-toctree-to-include-other-documents-as-children)
- Note that you can segment your TOC in a fun way with emojis as done here:
  [MyST-Parser documentation](https://myst-parser.readthedocs.io/en/latest/index.html). See the `.md`
  source [here](https://github.com/executablebooks/MyST-Parser/blob/d448abf395c29bb649f81fba5c1a2bc49e195cc0/docs/index.md?plain=1)
  to see how to do this.
- Because we're using Sphinx with the MySt extention, we can use Markdown almost
  everywhere. However, we still need to use it at least on the `index.rst` file.
  Here is a link to a [RestructuredText
  Cheatsheet](https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst).
- I'm using `autodoc2` to create the API documentation. This is a fork of the
  original `autodoc` extension that allows you to use Markdown in your docstrings.
  You can read more about it [here](https://sphinx-autodoc2.readthedocs.io/en/latest/).
  The differences between this and the original `autodoc` are documented [here](https://sphinx-autodoc2.readthedocs.io/en/latest/autodoc_diff.html).


## Indices and tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`

