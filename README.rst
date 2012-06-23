When using gitorious, it installs it own hooks into each git repository. So you
can't install the `post-receive hook of Trac's Git Plugin`_. However gitorious
provides `WebHooks`_. That is the ability to configure a URL that is called when
a certain repository was pushed. So you can use this CGI script as WebHook for
Trac's Git Plugin.

Configuration
-------------

Copy the CGI script into the cgi-bin directory of your trac environment and open
the CGI script with your favorite editor in order to change the constants
BRANCHES, TRAC_ENV and REPO_NAME, respective your setup::

    cp trac-web-hook.cgi <tracenv>/deploy/cgi-bin/
    vim <tracenv>/deploy/cgi-bin/trac-web-hook.cgi

Now you have to configure the CGI script in your web server. Therfore setup a
new virtual host, that is only local reachable. If you don't have Trac and
Gitorious running on the same machine you have to use an IP address reachable
from the server running Gitorious. But make sure that the port isn't reachable
from the internet, because no authentification is required to call the script::

    Listen 127.0.0.1:8000

    <VirtualHost 127.0.0.1:8000>
        ScriptAlias / <tracenv>/deploy/cgi-bin/trac-web-hook.cgi
    </VirtualHost>

Finally tell Gitorious to use the URL you have just configured, as WebHook
for your repository::

    project = Project.find_by_slug "<project>"
    repository = project.repositories.find_by_name "<repo>"
    hook = repository.hooks.build
    hook.user = repository.user  
    hook.url = "http://localhost:8000/"
    hook.save

.. _post-receive hook of Trac's Git Plugin: http://trac-hacks.org/wiki/GitPlugin#post-receivehookscripts
.. _WebHooks: http://gitorious.org/gitorious/pages/WebHooks
