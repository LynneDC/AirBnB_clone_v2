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
<p>Write a script that starts a Flask web application:</p>
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
<p>Write a script that starts a Flask web application:</p>
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
<p>Write a script that starts a Flask web application:</p>
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
<p>Write a script that starts a Flask web application:</p>
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
<p>Write a script that starts a Flask web application:</p>
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


