<%inherit file="/layout/standard.mako"/>
<%namespace name="forms" file="post_forms.mako" />

<%def name="title()">
all bits
</%def>

${forms.post_form()}

% for status in c.statuses:
    <div class="bit">
        <div class="text">${status.text}</div>
        <div class="user">
            <a href="${h.url_for('user_bits', name=status.user.name)}">${status.user.name}</a>
            <span class="when">@ ${status.when}</span>
        </div>
    </div>
% endfor
