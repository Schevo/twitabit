<%def name="post_form()">
% if c.remote_user:
    <form action="${h.url_for('post_bit', name=c.remote_user.name)}" method="post" accept-charset="utf-8">
        <textarea name="text"></textarea>
        <input type="hidden" name="_url" value="${h.url_for()}" />

        <div class="buttons">
            <input type="submit" name="post" value="post" />
        </div>
    </form>
% endif
</%def>