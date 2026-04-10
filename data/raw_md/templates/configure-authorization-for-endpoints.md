## Configure Authorization for Endpoints or Protect Business Object Data

You must define [Security System permissions](xref:113366) for business objects and properties you want to expose through a Web API Service (both built-in and custom endpoints). We do not recommend that you expose business object data to all users without security protection.

You can configure permissions using one of the following methods:

* In the code of the `ModuleUpdater` class (look for the _Updater.cs_ file, because there may be different locations depending on your project configuration).
* In the administrative UI powered by [XAF Blazor/WinForms](xref:401943) (this feature requires the Universal license).

For more information, refer to the following concepts and examples:

* [](xref:119065)
* [How to restrict inter-departmental data access using Security Permissions (EF Core)](https://supportcenter.devexpress.com/ticket/details/e4045/xaf-how-to-restrict-inter-departmental-data-access-using-security-permissions-ef-core)

