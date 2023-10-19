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

     Files 0 - 6 were introductory tasks familiarizing myself with using Flask. Files 7 forward involved gradually putting together more and more complex Jinja templates based on the HBnB HTML pages.
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
  <iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=F7-vdjIipfoZVexI&amp;list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <div data-react-class="videos/PlayerLibrary" data-react-props="{&quot;canManageVideos&quot;:false,&quot;videos&quot;:[{&quot;description&quot;:&quot;\u003cp\u003eWeb framework Flask in Python with Jinja\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;poster&quot;:&quot;https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/da28ac39534684d31cf0b30279a1510cd9a61e081cb9305fa1c8bb7fead2e121/da28ac39534684d31cf0b30279a1510cd9a61e081cb9305fa1c8bb7fead2e121.jpg?response-content-disposition=attachment%3B\u0026X-Amz-Algorithm=AWS4-HMAC-SHA256\u0026X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231019%2Fus-east-1%2Fs3%2Faws4_request\u0026X-Amz-Date=20231019T085559Z\u0026X-Amz-Expires=14400\u0026X-Amz-SignedHeaders=host\u0026X-Amz-Signature=29d9c98c87885a090410c38916c46082348c1f40fe346f184b91ebdfb2dae1b7&quot;,&quot;shortDescription&quot;:&quot;Web framework Flask in Python with Jinja&quot;,&quot;source&quot;:&quot;/video_releases/39.m3u8&quot;,&quot;title&quot;:&quot;Python: Flask the web framework&quot;}]}" data-react-cache-id="videos/PlayerLibrary-0"></div>

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

<pre><code>$ pip3 install Flask
</code></pre>  
 <li></li>
  <li></li>
 <li></li>
 <li></li>
  <li></li>
   <li></li>
   <li></li>
   <li></li>
   </ol>

   <h2 style="color: #FF645F; margin-left: 40px">
	     Tasks: MANDATORY
	</h2>
  <h2 style="color: white; background-color:#61b3e7">
	     0. Install MySQL
  </h2>
  <p> 
   First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
   <h4> Requirements: </h4>
   <ol>
   <li>MySQL distribution must be 5.7.x</li>
   <li>Please make sure you have your README.md pushed to GitHub.</li>
  </ol>
  </p>
  <h3 style="color: #FF645F; margin-left: 40px">
         1. Let us in!
  </h3>
  <p>
     create a user and password for both MySQL databases 
   <h4>REQUIREMENTS:</h4>
   <ul>
   <li> Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn.</li>
   <li> holberton_user has permission to check the primary/replica status of your databases.</li>
   <li> Add the public key to web-02 as you only added it to web-01 for this project</li>
   </ul>
   <h3 style="color: #FF645F; margin-left: 40px">
         2. If only you could see what I've seen with your eyes
  </h3>
  <p>  
   Create a database named tyrell_corp.
  <h4> Requirements: </h4>
  <li> Within the tyrell_corp database create a table named nexus6 and add at least one entry to it</li>
  <li>Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty. </li>
   </P>
 <h3> 3. Quite an experience to live in fear, isn't it? </h3>
 <p> On your primary MySQL server (web-01), create a new user for the replica server. </p>
 <h4> REQUIREMENTS </h4>
 <ol>
   <ul>
   <li>The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like</li>
   <li>replica_user must have the appropriate permissions to replicate your primary MySQL server.</li>
   <li>holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.</li>
  </ul>
  </ol>
 <h3>4. Setup a Primary-Replica infrastructure using MySQL</h3>

<h3> 5. MySQL backup </h3>

 </body>
</html>
