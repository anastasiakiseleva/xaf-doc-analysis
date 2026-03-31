---
uid: "404436"
title: "Multi-Tenancy (Data per Tenant)"
seealso:
- linkId: "404667"
- linkId: "404669"
- linkId: "404670"
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/ef/core/miscellaneous/multitenancy
  altText: Multi-tenancy
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/overview
  altText: Architect multitenant solutions on Azure
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns
  altText: Multi-tenant SaaS database tenancy patterns
---

# Multi-Tenancy (Data per Tenant)

XAF includes an out-of-the box capability to implement multi-tenant or SaaS-ready applications for straightforward CRUD usage scenarios.

![Multi-Tenancy](~/images/multitenancy-landing.png)

>[!Tip]
> You can find the example of a multi-tenant application in our [Outlook Inspired Demo](xref:113577#net-winforms--blazor-outlook-inspired-demo-multi-tenancysaas-readyxref404669).

>[!Note]
> Please take a moment to complete a short survey about your multi-tenancy requirements: 
[https://www.devexpress.com/products/net/application_framework/survey.xml](https://www.devexpress.com/products/net/application_framework/survey.xml).

## Glossary

Before you start researching the multi-tenancy feature, we recommend that you take a moment to familiarize yourself with the following terms specific to multi-tenancy in XAF: 

Multi-Tenant Application
:   An application in which a single instance serves multiple independent organizations (tenants) that use the same codebase and business logic but operate on separate data sets.

Tenant
:   A separate database as well as a group of users that have rights to operate on this database. Each tenant has its own individually stored data sets, access permissions, and application configuration.

Host User Interface
:   A multi-tenant application's operation mode for tenant list management. This mode allows a user to create, delete, and edit tenants. 

    ![Host UI](~/images/multitenancy-host-ui.png)

Tenant User Interface
:   A multi-tenant application's operation mode where a tenant can specify available data sets, user access permissions, and application configuration.

    ![Tenant UI](~/images/multitenancy-tenant-ui.png)

Host Database
:   A database that is used in Host User Interface mode. This database stores all information about tenants, the global configuration of a multi-tenant application, and [shared business objects](xref:405451).

Tenant Database
:   A database that a multi-tenant application uses in Tenant User Interface mode. This database stores an individual tenant's business object data and configurations.

Super Administrator
:   A user account that is used to access the Host User Interface. This user has no access rights for Tenant User Interfaces.

## Best Practices and Limitations

- The same database should not store data that belongs to several separate tenants. All connection strings for Tenant Databases must be unique.
- The same database should not store data from the Host Database and one or more Tenant Databases. None of the Tenant Database connection strings can ever match the Host Database connection string.
- Multi-tenant XAF Blazor apps have the same scalability as regular single-tenant XAF Blazor apps. This means that the number of concurrent users is determined by the sum of concurrent users of all tenants plus concurrent users of the Host User Interface. For more information, refer to [](xref:403362).
- Modules that register their own persistent types do not work in Host User Interface mode. For more information, see [](xref:404695).
- Multi-tenant applications do not currently support [persistent validation rules](xref:DevExpress.Persistent.Validation.IRuleSource).
- Updating databases in a multi-tenant application has specific considerations. Refer to the following help topics for more information: 
    * <xref:405376>
    * [Update Database in Multi-Tenant Application](xref:113239#update-database-in-multi-tenant-application)
