---
uid: "113124"
seealso: []
title: User Authentication Without a Logon Window in Windows Forms Applications
owner: Ekaterina Kiseleva
---
# User Authentication Without a Logon Window in Windows Forms Applications

This topic details the steps performed from the time the [](xref:DevExpress.ExpressApp.Win.WinApplication) object has been created and initialized, until the moment an end-user has been authenticated to the application. There are two built-in Authentication Strategies in XAF. The [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authenticates end-users with the information typed in the logon window. The [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) does not require the logon window to be displayed. It takes the required information from the system's active directory. This topic details how end-users are authenticated when the built-in **AuthenticationActiveDirectory** strategy is used. You can customize the **AuthenticationActiveDirectory**, so that a logon window is displayed and the information typed in it is used for authentication. In this instance, read the [User Authentication Without a Logon Window in Windows Forms Applications](xref:113124) topic, to learn how the logon window is displayed.

## Authentication
{|
|-

! Stage Description
! Ways to Interfere
|-

| To start the authentication process, an [Object Space](xref:113707) is created to check whether a record defining the user requesting authentication exists in the application database. Before accessing the database, the compatibility of the module versions in the database and their actual versions is checked. If the versions in the database are greater than the actual ones, an exception is raised, which requires that you increase your application's version. If lower, the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event is raised. By default, this event is handled in XAF solutions. The event handler calls the Database Updater's **Update** method, which updates the database to the required version. However, this method is called when the application is run in debug mode. In release mode, an exception is raised (you can see the entire code in your application).
| Before the authentication process is started, you can access the LogonParameters object modified by the user who is logging on. For this purpose, handle the [XafApplication.LoggingOn](xref:DevExpress.ExpressApp.XafApplication.LoggingOn) event.

You can perform a custom process of checking the database and application compatibility. For this purpose handle the [XafApplication.CustomCheckCompatibility](xref:DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility) event. In this instance, you should raise the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event in this code as well, to update the database when required.

If you do not need the scenario implemented in the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event handler, which is generated automatically in your application, write a custom event handler. For instance, you can implement a custom **DatabaseUpdater** class and call its **Update** method in the **DatabaseVersionMismatch** event handler.

Use the [XafApplication.DatabaseUpdateMode](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode) property to set the required behavior for the updating database mechanism. For instance, you can set the **UpdateDatabaseAlways** value so that the database's version is updated each time the application runs.
|-

| When the **AuthenticationActiveDirectory** strategy is used, authentication is accomplished immediately after the application is started. A user is authenticated if their account has been found in the system, and the corresponding object in the database exists.
| If the default authentication performed by a built-in Authentication class does not satisfy your requirements, implement a custom class. For instance, inherit from one of the built-in authentication classes: **AuthenticationStandard** or **AuthenticationActiveDirectory**. Alternatively, inherit from the base [](xref:DevExpress.ExpressApp.Security.AuthenticationBase) class. In your class, override the **Authenticate** method. It returns the user object that is found in the database by the credentials specified by the end-user who is logging on.
|-

| The Application Model's layer with end-user customizations, stored in the _Model.User.xafml_ file is created. This file stores end-user customizations to the application, created during the previous application runs.
| To perform custom actions after the logging on procedure has finished, handle the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) event.
|}