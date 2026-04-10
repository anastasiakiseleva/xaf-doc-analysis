---
uid: "113439"
seealso:
- linkId: "118741"
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t570966/how-to-migrate-to-the-new-middle-tier-implementation-after-upgrading-to-xaf-v17-2
  altText: How to Update the Middle Tier Implementation when Upgrading to XAF v17.2+
- linkId: "403550"  
title: Middle Tier Security with XPO
---

# Middle Tier Security with XPO

[!include[BypassClientSideSecurity](~/templates/BypassClientSideSecurity.md)] To prevent this, you can implement the Middle Tier application server that is an ASP.NET Core service between the client application and the database server. This Middle Tier Server filters out the secured data. In this case, clients cannot access the database server directly. The diagram below illustrates this configuration.

![A Diagram of an XAF Application with Middle Tier Security](~/images/ApplicationWithMiddleTier_main_diagram.png)

## Application Architecture Basics: Middle-Tier Security

The following images demonstrate how Blazor and WinForms applications with [Middle Tier Security](xref:113439) interact with the database:

> [!ImageGallery]
> ![Blazor application with the Middle Tier Application Server](~/images/ApplicationWithMiddleTier_blazor_diagram.png)
> ![WinForms application with the Middle Tier Application Server](~/images/ApplicationWithMiddleTier_diagram.png)
> ![Application without the Security System](~/images/NonSecureApplication_diagram.png)

### Load Data from the Database

1. The unsecure server-side @DevExpress.Xpo.Session loads data from the database according to the criteria based on [Security permissions](xref:113366).
2. The secure server-side @DevExpress.Xpo.Session copies objects from the unsecure server-side @DevExpress.Xpo.Session. If a field value does not meet the permission criterion, it is replaced with the default value in the copied objects. The copied objects are serialized and passed to the client-side @DevExpress.Xpo.Session.
3. The client-side @DevExpress.Xpo.Session deserializes these objects. The deserialized objects are available to users.

### Save Data to the Database

1. The client-side @DevExpress.Xpo.Session serializes objects and passes them to the secure server-side @DevExpress.Xpo.Session.
2. The secure server-side @DevExpress.Xpo.Session deserializes objects and copies their values (that meet Security permissions to the unsecure server-side @DevExpress.Xpo.Session.
3. The unsecure server-side @DevExpress.Xpo.Session saves the passed values into original objects in the database.

[!include[update-deployed-middle-tier-app](~/templates/update-deployed-middle-tier-app.md)]

## Important Notes

* [!include[](~/templates/middle-tier-ssl-note.md)]
* ASP.NET Core Blazor applications use the client-server model. You do not need to implement the additional Middle Tier server in these applications.
* The Middle Tier service and database can be installed on the same server. The application server can also be installed on a user workstation with the application, but this configuration does not improve security.
* Blazor application with Middle Tier security does not support Windows authentication.
* Integrated WebAPI services and Middle Tier security cannot be used simultaneously.
* If you use [custom permission requests](xref:113384), [custom logon parameters](xref:404264), or other types that should be serialized (for example, [non-persistent objects](xref:116516)), use the static [WebApiDataServerHelper.AddKnownType](xref:DevExpress.ExpressApp.Security.ClientServer.WebApi.WebApiDataServerHelper.AddKnownType(System.Type)) method to register them before a data server is initialized. Register these types on the server and client. Do not use this method to register [business classes](xref:113664).

[!include[SecuredApplications-ImportantNotes](~/templates/SecuredApplications-ImportantNotes.md)]