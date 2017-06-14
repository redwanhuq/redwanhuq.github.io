{%- extends 'basic.tpl' -%}
{% block input_group -%}
<div class="input_hidden">
{{ super() }}
</div>
{% endblock input_group %}

{%- block header -%}
{{ super() }}


<style type="text/css">
div.prompt {
	display: none;
}

div.rendered_html table, .rendered_html th, .rendered_html tr, .rendered_html td {
  font-size: 16px;
  border: 1px solid black;
}


</style>

{%- endblock header -%}