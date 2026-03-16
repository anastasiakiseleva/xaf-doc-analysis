---
uid: "403401"
title: 'Create a Standalone Web API Application'
owner: Eugenia Simonova
seealso:
- linkId: "403504"
- linkId: "403505"
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/04/06/consume-the-devexpress-backend-web-api-from-javascript-with-svelte-part-1.aspx?utm_source=DevExpress&utm_medium=Blog&utm_id=XAF&utm_term=part4&utm_content=oliver-apr2022
  altText: Consume the DevExpress Backend Web API from JavaScript with Svelte (Part 1. Set Up a New Project)
---
# Create a Standalone Web API Application

This topic contains step-by-step instructions on how to create an application with **Web API**. For more information on **Web API**, see the following topic: [Backend Web API Service](xref:403394).

1. Create a new project in Visual Studio. Select **DevExpress v<:xx.x:> Template Kit** and click **Next**.
    
    ![Select Template Kit, DevExpress](~/images/template-kit/template-kit-create-a-new-project.png)

1. Specify the project name and location and click **Create**.

1. In the invoked [Template Kit](xref:405447) window, select **XAF** and specify the Web API Service integration style in the **Blazor / Web API Service Options** section:

    * **Standalone (Separate Projects)** creates a separate Web API Service project.
    * **Integrated (Single Project)** integrates Web API Service to the ASP.NET Core Blazor project.

    ![Customize created project, DevExpress](~/images/template-kit/template-kit-security-standard-906.png)

1. Customize other options, if necessary: choose the [security options](xref:403413) for your application, select [additional modules](xref:118046), and so on. 

1. Click **Create Project**

1. [Create endpoints and test the Web API](xref:403551).
