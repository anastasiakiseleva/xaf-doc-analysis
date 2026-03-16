---
uid: "404281"
title: "Test the Web API with Swagger or Postman"
owner: Vladimir Abadzhev
seealso:
- linkId: "403715"
---
# Test the Web API with Swagger or Postman

## Use the Swagger UI to Test the Web API

If your solution includes a **Web API** project, right-click the project in the **Solution Explorer** and choose **Debug | Start new instance** to run the **Web API** project. A browser displays the page with the available endpoints.

If your solution includes a startup **Blazor Server** project that contains the **Web API**, run the application. Add _/swagger_ to the application address (for example, _https://localhost:44318/swagger_ ) and press _Enter_ to display a page with available endpoints. 

Refer to the following link for more information on the page's UI: [Swagger UI](https://swagger.io/tools/swagger-ui/).

The default configuration starts the Web API service on different ports depending on the project:
{|
|-
! Project
! Default Port
! Example
|-

| **Web API** project
| 44319
| https://localhost:44319/swagger
|-

| **Blazor Server** project
| 44318
| https://localhost:44318/swagger
|}

![XAF Web API](~/images/create-web-api-swagger.png)

Test the Web API. Expand the **GET ApplicationUser** endpoint and click the **Try it out** button. The **Execute** button is displayed. Click this button to see the result.

![|Test the Web API Service|](~/images/create-web-api-result.gif)

## Use the Postman Tool to Test the Web API

You can also use the [Postman](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) tool to test the Web API. The Postman tool is more flexible and allows you to send complex requests with [parameters](https://learning.postman.com/docs/sending-requests/requests/#sending-parameters) to the **Web API** service. Refer to the following link for more information on how to utilize this tool: [Sending your first request](https://learning.postman.com/docs/getting-started/first-steps/sending-the-first-request/). 

>[!TIP]
> To test the **Web API** service hosted on _localhost_, install the Postman desktop agent as described in the following topic: [Installing the Postman desktop agent](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/#installing-the-postman-desktop-agent).

The image below shows a request to the _Contact_ business object filtered by _FirstName_ in the Postman Web UI (`https://web.postman.co/home`):

![Use Postman to create a Web API request](~/images/web-api-postman.png)

See the following topics for more information on [OData](https://learn.microsoft.com/en-us/odata/overview) query options:
* [Query options overview](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview)
* [Query options usage](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-usage)

If you enable authentication for your **Web API** service, specify the authorization settings for the Postman tool. See the following topic for details: [Specifying authorization details](https://learning.postman.com/docs/sending-requests/authorization/authorization/). If the **Web API** service uses the XAF JWT token from the "Authenticate" endpoint, copy it from the Swagger UI page as described in the following section: [Use the Swagger UI to Test the JWT Authentication](xref:403504#use-the-swagger-ui-to-test-the-jwt-authentication).
