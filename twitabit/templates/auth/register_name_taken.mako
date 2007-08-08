<%inherit file="/layout/standard.mako"/>
<%namespace name="forms" file="register_forms.mako" />

<%def name="title()">
register
</%def>

<div class="error">
    The name <em>${c.name}</em> is already taken.
</div>

${forms.register_form('')}
