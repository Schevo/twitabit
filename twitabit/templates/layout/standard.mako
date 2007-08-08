<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>

<head>
    <title>twit&middot;a&middot;bit: ${self.title()}</title>
    <link rel="stylesheet" href="/css/reset-fonts-grids.css" type="text/css" media="screen" title="no title" charset="utf-8">
    <link rel="stylesheet" href="/css/master.css" type="text/css" media="screen" title="no title" charset="utf-8" />
</head>

<body>

<div id="doc3" class="yui-t1">
    <div id="bd">
        <!-- body -->
        <div class="yui-b">
            <h1>twit&middot;a&middot;bit</h1>

            <p><a href="${h.url_for('all_bits')}">all bits</a></p>

            % if c.remote_user is not None:
                <p><a href="${h.url_for('user_bits', name=c.remote_user.name)}">your bits</a></p>

                <h2>your account</h2>
        
                Logged in as ${c.remote_user.name}.
            
                <form action="${h.url_for('signout')}" method="post" accept-charset="utf-8">
                    <div class="buttons">
                        <input type="submit" name="signout" value="sign out" />
                    </div>
                </form>
            % else:
                % if not c.hide_signin:
                    <h2>sign in</h2>
        
                    <form action="${h.url_for('signin')}" method="post">
                        <label for="name">name</label>
                        <input type="text" name="name" />
                        <label for="password">password</label>
                        <input type="password" name="password" />

                        <div class="buttons">
                            <input type="submit" name="signin" value="sign in" />
                            <input type="submit" name="register" value="register" />
                        </div>
                    </form>
                % endif
            % endif

            <h2>about</h2>

            <p>this is an example application to show how
            to use <a href="http://schevo.org/">Schevo</a> to build a
            web app.</p>
            
            <p>the scope of the app is intentionally simple, focusing on
            integration aspects rather than showing off how Schevo
            helps manage and tame complex database logic.</p>

        </div>
        <div id="yui-main">
            <div class="yui-b">
                <h1>${self.title()}</h1>

                ${self.body()}
            </div>
        </div>
    </div>
</div>

</body>

</html>