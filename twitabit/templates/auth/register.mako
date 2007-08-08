<%inherit file="/layout/standard.mako"/>
<%namespace name="forms" file="register_forms.mako" />

<%def name="title()">
register
</%def>

${forms.register_form(c.name)}
