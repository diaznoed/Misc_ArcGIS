<%@ page import = "java.io.*,java.util.*" %>

<html>
   <head>
      <title>HTTP Report</title>
   </head>
   <body>
         <h2>Request</h2>
        <b>ClientIP:</b> <%= request.getRemoteAddr() %><br>
		<b>ClientHost:</b> <%= request.getRemoteHost() %><br>
        <b>URI:</b> request.getRequestURI() <br>
        <b>Method:</b>${pageContext.request.getMethod()} <br>
		<b>Protocol Scheme:</b><%= request.getScheme() %><br>
        <b>Server Port:</b><%= request.getServerPort() %> <br>

         <h2>HTTP Request Headers </h2>
         <table width = "100%" border = "1" align = "center">
            <tr bgcolor = "#949494">
               <th>Header Name</th>
               <th>Header Value(s)</th>
            </tr>
            <%
               Enumeration headerNames = request.getHeaderNames();
               while(headerNames.hasMoreElements()) {
                  String paramName = (String)headerNames.nextElement();
                  out.print("<tr><td>" + paramName + "</td>\n");
                  String paramValue = request.getHeader(paramName);
                  out.println("<td> " + paramValue + "</td></tr>\n");
               }
            %>
         </table>

        <h2>Server Info</h2>
        <b>Tomcat Version</b><%= application.getServerInfo() %><br>
        <b>Servlet Specification Version</b>: <%= application.getMajorVersion() %>.<%= application.getMinorVersion() %> <br>
        <b>JSP Version:</b> <%=JspFactory.getDefaultFactory().getEngineInfo().getSpecificationVersion() %><br>
		<b>Server Name:</b> <%=request.getServerName() %><br>

   </body>
</html>
