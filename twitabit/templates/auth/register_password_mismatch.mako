<%inherit file="/layout/standard.mako"/>
<%namespace name="forms" file="register_forms.mako" />

<%def name="title()">
register
</%def>

<div class="error">
    The passwords you entered did not match.
</div>

${forms.register_form(c.name)}
