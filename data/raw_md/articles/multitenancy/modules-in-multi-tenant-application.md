---
uid: "404695"
title: 'Modules in a Multi-Tenant Application'
---

# Modules in a Multi-Tenant Application

## Standard Module Support

In [Tenant User interface](xref:404436#glossary) mode, a multi-tenant application supports all standard modules in the same way as a single-tenant XAF application.

[Host User Interface](xref:404436#glossary) mode does not support some of the standard modules. The list of unsupported modules includes all modules that need to store their own persistent types in the database. This is because the Host User Interface restricts the types that are allowed to be stored to only the types required to manage users and tenants, and [shared business objects](xref:405451). Below is the list of standard XAF modules that cannot be used in a multi-tenant application when it runs in Host User Interface mode:

- [Audit Trail](xref:112782)
- [Dashboards](xref:117449)
- [File Attachments](xref:112781)
- [Notifications](xref:113690)
- [Reports V2](xref:113591)
- [Scheduler](xref:112812)
- [State Machine](xref:113713)
- [TreeList Editors](xref:112836)

## Custom Module Support

Keep the following specifics in mind when you develop a custom module in a multi-tenant application:

- If a module registers its own persistent types to store in a database, this module cannot be used in Host User Interface mode.

- Assume that you have a module that registers its own persistent types and includes controllers that operate on these types. In such case, when you query an [ObjectSpace](xref:DevExpress.ExpressApp.IObjectSpace), always ensure that the required type is supported by this ObjectSpace instance. To do this, use the [IObjectSpace.CanInstantiate](xref:DevExpress.ExpressApp.IObjectSpace.CanInstantiate(System.Type)) method: `objectSpace.CanInstantiate(typeof(YourPersistentType))`.

- When you implement logic used to update a database in [Module Updater](xref:DevExpress.ExpressApp.Updating.ModuleUpdater), both the Host Database and all Tenant Databases will be updated. Keep in mind that modules cannot store their persistent types in the Host Database. 

- Custom modules/business classes/custom fields per user/tenant are unsupported in the current version. At present, we recommend that you load all modules and business classes, and use a Controller to disable features per user/tenant instead. See the following topic for more information: [](xref:404668). All tenants will have the same set of business classes and database tables in their own databases.

- The Host User Interface does not allow users to manage available modules/features or licensing packages/editions for associated tenants and their users at application runtime. For future development, please also take a moment to complete a short survey on your multi-tenancy requirements: [XAF UI & Web API Service: Your Vote Matters | DevExpress](https://www.devexpress.com/products/net/application_framework/survey.xml).


