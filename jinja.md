#[Jinja2](http://jinja.pocoo.org/) notes

What is Jinja?
* Jinja is a template engine for Python
* It combines both logic and HTML
* take a look at [my blog] (www.github.com/mchenco/blog) under app/templates to see Jinja2 used with Flask

#logic is defined by {% ... %}
```
(% with messages = get_flashed_messages() %)
    {% if messages %}
        <ul>
            {% for message in messages %}
                <li> {{ message }} </li>
            {% endfor %}
        </ul>
    {% endif %}
{% endwith &}
```
Inheritance for templates is possible!
```
{% extends "base.html" %}
```
