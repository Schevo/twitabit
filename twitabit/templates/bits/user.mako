<%inherit file="/layout/standard.mako"/>
<%namespace name="forms" file="post_forms.mako" />

<%def name="title()">
bits by ${c.user.name}
</%def>

% if c.remote_user == c.user:
    ${forms.post_form()}
% endif

% for status in c.statuses:
    <div class="bit">
        <div class="text">${status.text}</div>
        <div class="user">
            ${status.user.name}
            <span class="when">@ ${status.when}</span>
        </div>
    </div>
% endfor
