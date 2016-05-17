#[Jinja2](http://jinja.pocoo.org/) notes

*jinja is a template engine for Python
*combines logic and HTML

logic is defined by {% ... %}
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

inheritance for templates is possible!
```
{% extends "base.html" %}
```

