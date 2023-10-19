<!DOCTYPE html>
<html>
<head>
<h1>
 Web framework
</h1>
</head>
<body style="font-family: Verdana, Arial, sans-serif">
   <h2> BACKGROUD </h2>
   <img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png" alt="Server-Side Back-end " />
   <h2> DESCRIPTION </h2>
   <p>
   <ol>
      This is a sub-project within AirBnB in which I began working with Flask and Jinja2.
      In this project, I began integrating the back-end storage engine with the web static HTML/CSS pages written earlier.

     Files 0 - 6 were introductory tasks familiarizing myself with using Flask.
     Files 7 forward involved gradually putting together more and more complex Jinja templates based on the HBnB HTML pages.
     The most complete Flask/Jinja app-template combo in this directory is defined in Flask module 100-hbnb.py and Jinja template 100-hbnb.html.

   To run the Flask app, execute the following command from the root directory of the project:
   <li><em>~ $ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb</em></li>
  </ol>
   <h2> RESOURCES </h2>
    <p><strong>Read or watch</strong>:</p>

   <ul>
   <li><a href="/rltoken/64SQpOGx46Ljp0zFJchESg" title="What is a Web Framework?" target="_blank">What is a Web Framework?</a> </li>
   <li><a href="/rltoken/NopQlHIr9J_9OPX9XRgfvw" title="A Minimal Application" target="_blank">A Minimal Application</a> </li>
   <li><a href="/rltoken/cQiIhbSdIcg1Ao1MICseBg" title="Routing" target="_blank">Routing</a> (<em>except &ldquo;HTTP Methods&rdquo;</em>)</li>
   <li><a href="/rltoken/DBM65T59nySd0ZRlZZ0CXw" title="Rendering Templates" target="_blank">Rendering Templates</a> </li>
   <li><a href="/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ" title="Synopsis" target="_blank">Synopsis</a> </li>
   <li><a href="/rltoken/ITzobwYP1Lc4KqEUUcYCGw" title="Variables" target="_blank">Variables</a> </li>
   <li><a href="/rltoken/ykUFuQSE9KD1M7WGY-4v4w" title="Comments" target="_blank">Comments</a> </li>
   <li><a href="/rltoken/NMLZom50ZVOxQlgYW3rnuQ" title="Whitespace Control" target="_blank">Whitespace Control</a> </li>
   <li><a href="/rltoken/5AGhzIt0zSpPJh9SFysdMQ" title="List of Control Structures" target="_blank">List of Control Structures</a> (<em>read up to &ldquo;Call&rdquo;</em>)</li>
   <li><a href="/rltoken/VJs151_hsE9g7Cw-Pz5bVg" title="Flask" target="_blank">Flask</a> </li>
   <li><a href="/rltoken/2y_hunzGCCvSot06EW67UQ" title="Jinja" target="_blank">Jinja</a> </li>
   </ul>
  </p>
 
   <h2 style="color: green; round-color:RED ">
        General Knowledge Test 
   </h2>
   <ol>
   <li>What is a Web Framework</li>
   <li>How to build a web framework with Flask</li>
   <li>How to define routes in Flask</li>
   <li>What is a route</li>
   <li>How to handle variables in a route</li>
   <li>What is a template</li>
   <li>How to create a HTML response in Flask by using a template</li>
   <li>How to create a dynamic template (loops, conditions…)</li>
   <li>How to display in HTML data from a MySQL database</li>
   <li>   ......    </li>

   <h2>Requirements</h2>

   <h3>Python Scripts</h3>

   <ul>
   <li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
   <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.4.3)</li>
   <li>All your files should end with a new line</li>
   <li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>HTML/CSS Files</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="/rltoken/_bfSTiq2t4otmyPespKhEg" title="W3C-Validator" target="_blank">W3C-Validator</a> (except for jinja template)</li>
<li>All your CSS files should be in the <code>styles</code> folder</li>
<li>All your images should be in the <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> or <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>All tags must be in uppercase</li>
<li>Current screenshots have been done on <code>Chrome 56.0.2924.87</code>. </li>
<li>No cross browsers </li>
</ul>

<h2>More Info</h2>

<h3>Install Flask</h3>

<p><em>$ pip3 install Flask</em></p>

<h2>Tasks</h2>
<h3 class="panel-title">
 0. Hello Flask!
</h3>
<h4>Write a script that starts a Flask web application:</h4>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
</div>

<h3 class="panel-title">
     1. HBNB
</h3>
<h4>Write a script that starts a Flask web application:</h4>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<h3 class="panel-title">
      2. C is fun!
</h3>
<h4>Write a script that starts a Flask web application:</h4>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
  <li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo; followed by the value of the <code>text</code> variable (replace underscore <code>_ </code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<h3 class="panel-title">
   3. Python is cool!
</h3>
<h4>Write a script that starts a Flask web application:</h4>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_ </code> symbols with a space <code></code>)</li>
<li><code>/python/&lt;text&gt;</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_ </code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<h3 class="panel-title">
    4. Is it a number?
</h3>
<h4>Write a script that starts a Flask web application:</h4>
<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_ </code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_ </code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<h3 class="panel-title">
      5. Number template
 </h3>

  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)
<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 
<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>  
<h3 class="panel-title">
    6. Odd or even?
</h3>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:
<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code> is <code>even|odd</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
<h3 class="panel-title">
   7. Improve engines
</h3>
<p>Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>

<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>

<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) <a href="/rltoken/_lTxhB5UgQ4nFRoS9ooI5g" title="tips" target="_blank">tips</a> or <code>close()</code> on the class <code>Session</code> <a href="/rltoken/xlPf9pDUFMb599rkoDElvg" title="tips" target="_blank">tips</a></li>
</ul>

<p>Update <code>State</code>: (<code>models/state.py</code>) - If it&rsquo;s not already present</p>

<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>
<h3 class="panel-title">
      8. List of states
</h3>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/2y_hunzGCCvSot06EW67UQ" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>
<h3 class="panel-title">
   9. Cities by states
 </h3>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/cities_by_states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/2y_hunzGCCvSot06EW67UQ" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code> + <code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<h3 class="panel-title">
    10. States and State
</h3>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/2y_hunzGCCvSot06EW67UQ" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li><code>/states/&lt;id&gt;</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li>If a <code>State</code> object is found with this <code>id</code>:

<ul>
<li><code>H1</code> tag: &ldquo;State: <state.name>&rdquo;</li>
<li><code>H3</code> tag: &ldquo;Cities:&rdquo;</li>
<li><code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li>Otherwise: 

<ul>
<li><code>H1</code> tag: &ldquo;Not found!&rdquo;</li>
</ul></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<h3 class="panel-title">
    11. HBNB filters
 </h3>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/hbnb_filters</code>: display a HTML page like <code>6-index.html</code>, which was done during the project <a href="/rltoken/EG-iGbr_iPTlHrQQSNho1g" title="0x01. AirBnB clone - Web static" target="_blank">0x01. AirBnB clone - Web static</a>

<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code> and <code>6-filters.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy files <code>icon.png</code> and <code>logo.png</code> from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
<li>Use <code>6-index.html</code> content as source code for the template <code>10-hbnb_filters.html</code>:

<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&amp;nbsp;</code></li>
</ul></li>
<li><code>State</code>, <code>City</code> and <code>Amenity</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A-&gt;Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql" title="10-dump" target="_blank">10-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<p>In the browser:</p>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231019T085559Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=88245362432118f074fa168f135944b1bd4ecc27f4b4fdc9d27550584cb8d594" alt="" loading='lazy' style="" />
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231019T085559Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=809ed7726c4cc593528df6ea90938d3de03a0aea303047499fbe57dd9135b020" alt="" loading='lazy' style="" />
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231019T085559Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=484210644e55f23daf52773bd70e1fa54bd18c631fe80415eb61d826d31327d4" alt="" loading='lazy' style="" />
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231019%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231019T085559Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4d2389e10fde6395578cb1e7600bfd78a00aab2ee76cb7c457a7b73feef54dbe" alt="" loading='lazy' style="" /></p>



