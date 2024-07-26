# MyST Markdown Demos 💡

Here is a demo of MyST Markdown.



|    Training   |   Validation   |
| :------------ | -------------: |
|        0      |        5       |
|     13720     |      2744      |


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```{note} Notes require **no** arguments,
so content can start here.
```

```{warning} This is an example
of a warning directive.
```

```{tip} This is an example
of a tip directive.
```

```{caution} This is an example
of a caution directive.
```

```{attention} This is an example
of an attention directive.
```

```{hint} This is an example
of a hint directive.
```

```{important} This is an example
of an important directive.
```

```{figure} ../assets/logo.png
:height: 150px
:name: figure-example

Here is my figure caption!
```

	
This is an example of an
inline equation $z=\sqrt{x^2+y^2}$.

This is an example of a
math block

$$
z=\sqrt{x^2+y^2}
$$


This is an example of a
math block with a label

$$
z=\sqrt{x^2+y^2}
$$ (mylabel)

	
This is an example of a
math directive with a
label
```{math}
:label: eq-label

z=\sqrt{x^2+y^2}
```

Check out equation {eq}`eq-label`.


Wrap in-line code blocks in backticks: `boolean example = true;`.

```python
note = "Python syntax highlighting"
print(node)
```