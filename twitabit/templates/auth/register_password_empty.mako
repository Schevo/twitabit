<%inherit file="/layout/standard.mako"/>
<%namespace name="forms" file="register_forms.mako" />

<%def name="title()">
register
</%def>

<div class="error">
    You must choose a password to create an account.
</div>

${forms.register_form(c.name)}
