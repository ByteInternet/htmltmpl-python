#!/usr/bin/env python

import sys
import getopt
import easydoc

BGCOLOR = "#d8d0a4"
TEXTCOLOR = "black"
LINKCOLOR = "red"
METHODBG = "#d8e0d4"
TEMPLATE = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
  <html>
    <head>
      <title><TMPL_VAR name>: documentation</title>
      <meta name="author"
            content="<TMPL_VAR author-name> (<TMPL_VAR author-email>)"></meta>
      <meta name="keywords" content="Python,module,<TMPL_VAR name>"></meta>
      <meta name="description" content="<TMPL_VAR short>"></meta>
      <style type="text/css">
        <!--
body {
  font-family: "Helvetica CE", "Arial CE", Helvetica, Arial, sans-serif;
  background-color: <TMPL_VAR bgcolor>;
  color: <TMPL_VAR textcolor>;
}

a {
  color: <TMPL_VAR linkcolor>;
  font-weight: bold;
}

.methodbg {
  background-color: <TMPL_VAR methodbg>;
}
        -->        
      </style>
    </head>
    <body>
      <h1><TMPL_VAR name></h1>

      <!-- module info -->

      <p><strong><TMPL_VAR short></strong></p>
      <p>
        <strong>
          VERSION: <TMPL_VAR version>
          <br></br>
          AUTHOR: <TMPL_VAR author-name>
          (<a href="mailto:<TMPL_VAR author-email>"><TMPL_VAR author-email></a>)
          <br></br>
          WEBSITE: <a href="<TMPL_VAR website>"><TMPL_VAR website></a>
          <br></br>
          LICENSE: <a href="<TMPL_VAR license-url>"><TMPL_VAR license-name></a>
        </strong>
      </p>

      <TMPL_LOOP Detailed>
        <p><TMPL_VAR paragraph></p>
      </TMPL_LOOP>
      <hr></hr>

      <!-- module requirements -->

      <TMPL_IF Requires>
        <p><strong>REQUIRES:</strong></p>
        <TMPL_IF Requires>
          <ul>
            <TMPL_LOOP Requires>
              <li><TMPL_VAR require></li>
            </TMPL_LOOP>
          </ul>
        </TMPL_IF>
        <hr></hr>
      </TMPL_IF>

      <!-- table of functions -->

      <TMPL_IF Functions>
        <p><strong>FUNCTIONS:</strong></p>        
        <table border="0" cellpadding="3">
          <TMPL_LOOP Functions>
            <tr>
              <td>&nbsp; &nbsp; &nbsp; &nbsp;</td>
              <td>
                <a href="#function-<TMPL_VAR name>"><TMPL_VAR name></a>
                &nbsp; &nbsp;
              </td>
              <td><TMPL_VAR short></td>
            </tr>
          </TMPL_LOOP>
        </table>
        <hr></hr>
      </TMPL_IF>

      <!-- table of classes and methods -->

      <TMPL_IF Classes>
        <p><strong>CLASSES:</strong></p>
        <ul>
          <TMPL_LOOP Classes>
            <li>
              <p>
                <a href="#class-<TMPL_VAR name>"><TMPL_VAR name></a>:
                <TMPL_VAR short>
              </p>
              <TMPL_IF Methods>
                <table border="0" cellpadding="3">
                  <TMPL_LOOP Methods>
                    <tr>
                      <td>
                          &nbsp; &nbsp; &nbsp; &nbsp;
                      </td>
                      <td class="methodbg">
                        <a href="#method-<TMPL_VAR class>_<TMPL_VAR name>">
                          <TMPL_VAR name></a>
                        &nbsp; &nbsp;
                      </td>
                      <td><TMPL_VAR short></td>
                    </tr>
                  </TMPL_LOOP>
                </table>
              </TMPL_IF>
            </li>
          </TMPL_LOOP>
        </ul>
        <hr></hr>
      </TMPL_IF>


      <!-- documentation of functions -->


      <TMPL_LOOP Functions>
        
        <!-- function: <TMPL_VAR name> -->
        
        <h2>
          FUNCTION: <a name="function-<TMPL_VAR name>"></a><TMPL_VAR name>()
        </h2>
        <p><strong><TMPL_VAR short></strong></p>
        <TMPL_LOOP Detailed>
          <p><TMPL_VAR paragraph></p>
        </TMPL_LOOP>

        <!-- parameters of method <TMPL_VAR name> -->

        <p><strong>PARAMETERS:</strong></p>
        <pre><TMPL_VAR header></pre>
        <TMPL_IF Parameters>                
          <ul>
            <TMPL_LOOP Parameters>
              <li>
                <p><strong><TMPL_VAR name></strong></p>
                <p><strong><em><TMPL_VAR short></em></strong></p>
                <TMPL_LOOP Detailed>
                  <p><TMPL_VAR paragraph></p>
                </TMPL_LOOP>
              </li>
            </TMPL_LOOP>
          </ul>
        </TMPL_IF>
        <hr></hr>
      </TMPL_LOOP>
      <hr></hr>

      <!-- documentation of classes -->


      <TMPL_LOOP Classes>
        
        <!-- class: <TMPL_VAR name> -->
        
        <h2>CLASS: <a name="class-<TMPL_VAR name>"></a><TMPL_VAR name></h2>
        <p><strong><TMPL_VAR short></strong></p>
        <TMPL_LOOP Detailed>
          <p><TMPL_VAR paragraph></p>
        </TMPL_LOOP>

        <!-- table of methods of class <TMPL_VAR name> -->

        <TMPL_IF Methods>
          <p><strong>METHODS:</strong></p>
          <table border="0" cellpadding="3">
            <TMPL_LOOP Methods>
              <tr>
                <td>&nbsp; &nbsp; &nbsp; &nbsp;</td>
                <td class="methodbg">
                  <a href="#method-<TMPL_VAR class>_<TMPL_VAR name>">
                    <TMPL_VAR name></a>
                  &nbsp; &nbsp;
                </td>
                <td><TMPL_VAR short></td>
              </tr>
            </TMPL_LOOP>
          </table>
        </TMPL_IF>
        <hr></hr>

        <!-- documentation of methods of class <TMPL_VAR name> -->

        <TMPL_LOOP Methods>
          
          <!-- method <TMPL_VAR name> -->
          
          <h3>METHOD: <a name="method-<TMPL_VAR class>_<TMPL_VAR name>"></a>
            <TMPL_VAR name>()</h3>
          <p>
            <strong><em><TMPL_VAR short></em></strong>
            <small>(class
              <a href="#class-<TMPL_VAR class>"><TMPL_VAR class></a>)
            </small>
          </p>
          <TMPL_LOOP Detailed>
            <p><TMPL_VAR paragraph></p>
          </TMPL_LOOP>
          <TMPL_IF return>   ### Constructors do not have return value.
            <p><strong>RETURN VALUE:</strong></p>
            <p><TMPL_VAR return></p>
          </TMPL_IF>

          <!-- parameters of method <TMPL_VAR name> -->

          <p><strong>PARAMETERS:</strong></p>
          <pre><TMPL_VAR header></pre>                
          <TMPL_IF Parameters>                
            <ul>
              <TMPL_LOOP Parameters>
                <li>
                  <p><strong><TMPL_VAR name></strong></p>
                  <p><strong><em><TMPL_VAR short></em></strong></p>
                  <TMPL_LOOP Detailed>
                    <p><TMPL_VAR paragraph></p>
                  </TMPL_LOOP>
                </li>
              </TMPL_LOOP>
            </ul>
          </TMPL_IF>
          <hr></hr>

        </TMPL_LOOP>
        <hr></hr>

      </TMPL_LOOP>
    </body>
  </html>
"""

def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "h", ["with-hidden",
                                                          "help",
                                                          "debug",
                                                          "template=",
                                                          "bgcolor=",
                                                          "textcolor=",
                                                          "linkcolor=",
                                                          "methodbg="])
    except:
        help("Invalid options.")

    # Process parameters.
    module = None
    output = None
    if len(args) == 0:
        help("Missing parameters.")
    elif len(args) == 2:
        module = args[0]
        output = args[1]
    else:
        help("Invalid number of parameters.")

    # Process options.
    with_hidden, debug = 0, 0
    bgcolor, textcolor, linkcolor = BGCOLOR, TEXTCOLOR, LINKCOLOR
    methodbg = METHODBG
    template = TEMPLATE    
    for x in optlist:
        opt, value = x
        if opt == "-h" or opt == "--help":
            help()
        elif opt == "--template":
            f = open(value)
            template = f.read()
            f.close()            
        elif opt == "--with-hidden":
            with_hidden = 1
        elif opt == "--debug":
            debug = 1
        elif opt == "--bgcolor":
            bgcolor = value
        elif opt == "--textcolor":
            textcolor = value
        elif opt == "--linkcolor":
            linkcolor = value
        elif opt == "--methodbg":
            methodbg = value          
    easy = easydoc.Easydoc(template, debug)
    out = open(output, "w")
    out.write(easy.process(module, bgcolor, textcolor, linkcolor, methodbg, with_hidden))
    out.close()

def help(error=""):
    print "easydoc for Python, version", easydoc.VERSION
    print "(c) 2001 Tomas Styblo, tripie@cpan.org"
    print
    if error: print error
    print
    print "easy <module> <output> [--template]"
    print "                       [--with-hidden]"
    print "                       [--bgcolor]"
    print "                       [--textcolor]"
    print "                       [--linkcolor]"
    print "                       [--methodbg]"
    print
    print "     <module>      : filename of the module to document"
    print "     <output>      : output file"
    print "     --template    : alternative template filename"
    print "     --with-hidden : include sections marked as @hidden"
    print "     --bgcolor     : background color"
    print "     --textcolor   : text color"
    print "     --linkcolor   : hyperlink color"
    print "     --methodbg    : background color of method names"
    sys.exit()

main()
