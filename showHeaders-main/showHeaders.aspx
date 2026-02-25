<!-- directives -->
<% @Page Language="C#" debug="true" trace="false" %>

<!-- code section -->
<script runat="server">

   
   private void Page_Load()
   {
		Response.Write("<h1>HTTP Report</h1>");
		
		Uri theUrl = Request.Url;
		Response.Write("<h2>Request</h2>" + Environment.NewLine);
		Response.Write("<b>Protocol</b>=" + Server.HtmlEncode(theUrl.Scheme)  + "<br>" + Environment.NewLine);
		Response.Write("<b>Port</b>=" + theUrl.Port  + "<br>" + Environment.NewLine);
		Response.Write("<b>Method</b>=" + Request.HttpMethod  + "<br>" + Environment.NewLine);
		Response.Write("<b>Client Address</b>=" + Request.UserHostAddress + "<br>" + Environment.NewLine);
		Response.Write("<b>User</b>=" + Request.LogonUserIdentity.Name + "<br>" + Environment.NewLine);
		Response.Write("<b>Authentication Type</b>=" + Request.LogonUserIdentity.AuthenticationType + "<br>" + Environment.NewLine);
				
		Response.Write("<h2>Request Headers</h2>" + Environment.NewLine);
		foreach (var key in Request.Headers.AllKeys)
			Response.Write("<b>" + key + "</b>=" + Request.Headers[key] + "<br>" + Environment.NewLine);
		
		Response.Write("<h2>Response Information</h2>" + Environment.NewLine);
		foreach (var key in Response.Headers.AllKeys)
			Response.Write("<b>" + key + "</b>=" + Response.Headers[key] + "<br>" + Environment.NewLine);
		Response.Write("<b>Cache-Control</b>=" + Response.CacheControl + "<br>" + Environment.NewLine);
		Response.Write("<b>Client still connected?</b>=" + Response.IsClientConnected.ToString() + "<br>" + Environment.NewLine);
		Response.Write("<b>HTTP Status</b>=" + Response.Status + "<br>" + Environment.NewLine);
		
		
		Response.Write("<h2>Server Information</h2>" + Environment.NewLine);
		NameValueCollection serverVariablesCollection = Request.ServerVariables;
		Response.Write("<b>Server Software</b>=" + serverVariablesCollection["SERVER_SOFTWARE"] + "<br>" + Environment.NewLine);
		Response.Write("<b>Server Address</b>=" + serverVariablesCollection["LOCAL_ADDR"] + "<br>" + Environment.NewLine);
		Response.Write("<b>Server Name</b>=" + serverVariablesCollection["SERVER_NAME"] + "<br>" + Environment.NewLine);
		Response.Write("<b>AppPoolId</b>=" + serverVariablesCollection["APP_POOL_ID"] + "<br>" + Environment.NewLine);
		Response.Write("<b>Server Certificate Issuer</b>=" + serverVariablesCollection["CERT_SERVER_ISSUER"] + "<br>" + Environment.NewLine);
		Response.Write("<b>Server Certificate Subject</b>=" + serverVariablesCollection["CERT_SERVER_SUBJECT"] + "<br>" + Environment.NewLine);
		
				
   }
</script>

<!-- Layout -->
<html>
   <head> 
      <title> Show Headers </title> 
   </head>
   
   <body>
			<form runat="server">
				<!-- ASP.NET controls go here -->
			</form> 
			

      
   </body>
   
</html>
