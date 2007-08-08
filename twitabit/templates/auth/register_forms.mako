<%def name="register_form(name)">
<form action="${h.url_for('register')}" method="post" accept-charset="utf-8">
    <label for="name">name</label>
    <input type="text" name="name" value="${name}" />
    <label for="password">password</label>
    <input type="password" name="password" />
    <label for="password2">password (again for verification)</label>
    <input type="password" name="password2" />

    <div class="buttons">
        <input type="submit" name="finish" value="finish" />
    </div>
</form>
</%def>